#!/usr/bin/env python3
"""Kontrola UTM parametrů v ChatGPT Ads před spuštěním reklam (jen čte).

Pravidlo (skill/chatgpt-ads/SKILL.md, pravidlo 12): každá sestava má plnou UTM šablonu
  utm_source=chatgpt&utm_medium=cpc&utm_campaign=<slug>&utm_content=<klíč-sestavy>&utm_term={ad_id}
Šablony z kampaně, sestavy a reklamy se podle dokumentace OpenAI (2026-09) kombinují a u stejného klíče
vyhrává konkrétnější úroveň. Ověřený vzor je celá šablona na sestavě, proto kampaň i reklama bez šablony.
target_url bez utm_* a bez rezervovaných parametrů.

Použití:
  python3 scripts/utm_check.py --account acme
  python3 scripts/utm_check.py --account acme --campaign-id cmpn_...

Kontroluje aktivní i pozastavené objekty (pozastavené se později spouští), archivované přeskakuje.
Exit 0 = bez chyb (varování nevadí), 1 = aspoň jedna CHYBA (neaktivovat), 2 = nešlo načíst data.
Data bere z tohoto CLI (`run.sh campaigns --json`, `campaign-detail --with-children --json`).
Přispěl PLACEMENT.cz.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from urllib.parse import parse_qs, urlsplit

REQUIRED = ("utm_source", "utm_medium", "utm_campaign", "utm_content")
EXPECTED = {"utm_source": "chatgpt", "utm_medium": "cpc"}
RESERVED_EXACT = {"oppref", "obref"}
APP_DIR = os.environ.get("CHATGPT_ADS_APP_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@dataclass
class Finding:
    level: str  # "CHYBA" | "VAROVÁNÍ"
    where: str
    message: str


def _template(obj: dict) -> str:
    lpc = obj.get("landing_page_configuration") or {}
    return (lpc.get("query_string_template") or "").strip().lstrip("?")


def _params(query: str) -> dict:
    return parse_qs(query, keep_blank_values=True)


def _reserved(keys) -> list:
    return sorted(k for k in keys if k.lower() in RESERVED_EXACT or k.lower().startswith("oai"))


def _active(obj: dict) -> bool:
    return (obj.get("status") or "").lower() != "archived"


def evaluate(campaign: dict) -> list:
    """Zkontroluje strom jedné kampaně (výstup `campaign-detail --with-children --json`)."""
    out: list = []
    cname = f'kampaň „{campaign.get("name")}“ ({campaign.get("id")})'
    if _template(campaign):
        out.append(Finding("VAROVÁNÍ", cname,
                           f"kampaňová šablona není prázdná ({_template(campaign)}); "
                           "šablony se kombinují (sestava přebije kampaň); ověřený vzor je celá šablona na sestavě"))
    seen_content: dict = {}
    for g in campaign.get("_ad_groups") or []:
        if not _active(g):
            continue
        gname = f'sestava „{g.get("name")}“ ({g.get("id")})'
        tpl = _template(g)
        if not tpl:
            out.append(Finding("CHYBA", gname,
                               "nemá žádnou UTM šablonu; návštěvy v GA4 spadnou do (direct) nebo (not set)"))
        else:
            p = _params(tpl)
            missing = [k for k in REQUIRED if k not in p]
            blank = [k for k in REQUIRED if k in p and not any(v.strip() for v in p[k])]
            if missing:
                out.append(Finding("CHYBA", gname, "chybí " + ", ".join(missing) + f" (šablona: {tpl})"))
            if blank:
                out.append(Finding("CHYBA", gname, "prázdná hodnota u " + ", ".join(blank)))
            for k, want in EXPECTED.items():
                if k in p and p[k] and p[k][0].strip() and p[k][0] != want:
                    out.append(Finding("VAROVÁNÍ", gname, f"{k}={p[k][0]}, konvence je {k}={want}"))
            res = _reserved(p.keys())
            if res:
                out.append(Finding("CHYBA", gname, "rezervované parametry v šabloně: " + ", ".join(res)))
            content = (p.get("utm_content") or [""])[0].strip()
            if content:
                seen_content.setdefault(content, []).append(g.get("name"))
        for a in g.get("_ads") or []:
            if not _active(a):
                continue
            aname = f'reklama „{a.get("name")}“ ({a.get("id")}) v {gname}'
            atpl = _template(a)
            if atpl:
                amissing = [k for k in REQUIRED if k not in _params(atpl)]
                if amissing:
                    out.append(Finding("CHYBA", aname, "vlastní šablona reklamy bez " + ", ".join(amissing)))
                else:
                    out.append(Finding("VAROVÁNÍ", aname,
                                       "reklama má vlastní šablonu; přebije stejné klíče sestavy, ověř výsledek v GA4"))
            url = (a.get("creative") or {}).get("target_url") or ""
            if url:
                q = _params(urlsplit(url).query)
                if any(k.lower().startswith("utm_") for k in q):
                    out.append(Finding("VAROVÁNÍ", aname, "target_url už obsahuje utm_* parametry, v GA4 hrozí zdvojení"))
                ures = _reserved(q.keys())
                if ures:
                    out.append(Finding("CHYBA", aname, "target_url obsahuje rezervované parametry: " + ", ".join(ures)))
    for content, names in seen_content.items():
        if len(names) > 1:
            out.append(Finding("VAROVÁNÍ", cname,
                               f"utm_content={content} sdílí více sestav ({', '.join(str(n) for n in names)}); "
                               "v GA4 je nerozlišíš"))
    return out


def parse_json_output(text: str, what: str):
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError) as e:
        head = (text or "").strip().splitlines()[:3]
        raise ValueError(f"{what}: výstup CLI není JSON ({e}); začátek: {' | '.join(head)}") from None


def _cli(account: str, *args: str):
    run = os.path.join(APP_DIR, "run.sh")
    if not os.path.isfile(run):
        raise ValueError(f"nenalezen {run} (nastav CHATGPT_ADS_APP_DIR na složku s run.sh)")
    res = subprocess.run([run, "--account", account, *args, "--json"],
                         capture_output=True, text=True, timeout=300)
    if res.returncode != 0:
        raise ValueError(f"{' '.join(args)} skončil kódem {res.returncode}: {res.stderr.strip()[-400:]}")
    return parse_json_output(res.stdout, " ".join(args))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Kontrola UTM v ChatGPT Ads před spuštěním")
    ap.add_argument("--account", required=True)
    ap.add_argument("--campaign-id", action="append", help="lze opakovat; bez něj všechny nearchivované kampaně")
    args = ap.parse_args(argv)
    findings: list = []
    try:
        ids = args.campaign_id
        if not ids:
            camps = _cli(args.account, "campaigns")
            items = camps if isinstance(camps, list) else camps.get("data", [])
            ids = [c["id"] for c in items if _active(c)]
        for cid in ids:
            tree = _cli(args.account, "campaign-detail", "--campaign-id", cid, "--with-children")
            groups = [g for g in (tree.get("_ad_groups") or []) if _active(g)]
            n_ads = sum(1 for g in groups for a in (g.get("_ads") or []) if _active(a))
            print(f'• {tree.get("name")} ({cid}): {len(groups)} sestav, {n_ads} reklam')
            findings += evaluate(tree)
    except ValueError as e:
        print(f"NEŠLO NAČÍST: {e}", file=sys.stderr)
        return 2
    errors = [f for f in findings if f.level == "CHYBA"]
    for f in sorted(findings, key=lambda f: (f.level != "CHYBA", f.where)):
        print(f"{f.level:9} {f.where}: {f.message}")
    if errors:
        print(f"\n❌ Chyb: {len(errors)}. NEAKTIVOVAT, dokud se neopraví.")
        return 1
    print(f"\n✅ UTM v pořádku (varování: {len(findings)}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
