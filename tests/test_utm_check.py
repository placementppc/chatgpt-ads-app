"""Testy kontroly UTM (scripts/utm_check.py) — jen logika nad stromem kampaně, bez API."""
import importlib.util
import os
import sys

_SPEC = importlib.util.spec_from_file_location(
    "utm_check", os.path.join(os.path.dirname(__file__), "..", "scripts", "utm_check.py"))
utm = importlib.util.module_from_spec(_SPEC)
sys.modules["utm_check"] = utm  # dataclass s `from __future__ import annotations` potřebuje modul v sys.modules
_SPEC.loader.exec_module(utm)

FULL = "utm_source=chatgpt&utm_medium=cpc&utm_campaign=podzim&utm_content={key}&utm_term={{ad_id}}"


def _group(key, tpl=None, ads=None, status="active"):
    return {"id": f"adgrp_{key}", "name": key, "status": status,
            "landing_page_configuration": {"query_string_template": FULL.format(key=key) if tpl is None else tpl},
            "_ads": ads or []}


def _levels(findings):
    return [f.level for f in findings]


def test_full_template_is_clean():
    camp = {"id": "cmpn_1", "name": "Podzim", "_ad_groups": [_group("a"), _group("b")]}
    assert utm.evaluate(camp) == []


def test_missing_template_is_error():
    camp = {"id": "cmpn_1", "name": "Podzim", "_ad_groups": [_group("a", tpl="")]}
    assert _levels(utm.evaluate(camp)) == ["CHYBA"]


def test_missing_utm_content_is_error():
    camp = {"id": "cmpn_1", "name": "Podzim",
            "_ad_groups": [_group("a", tpl="utm_source=chatgpt&utm_medium=cpc&utm_campaign=podzim")]}
    assert "CHYBA" in _levels(utm.evaluate(camp))


def test_reserved_param_in_target_url_is_error():
    ad = {"id": "ad_1", "name": "A1", "status": "active",
          "creative": {"target_url": "https://example.com/?oppref=x"}}
    camp = {"id": "cmpn_1", "name": "Podzim", "_ad_groups": [_group("a", ads=[ad])]}
    assert "CHYBA" in _levels(utm.evaluate(camp))


def test_shared_utm_content_is_warning():
    camp = {"id": "cmpn_1", "name": "Podzim", "_ad_groups": [_group("a"), _group("a")]}
    assert _levels(utm.evaluate(camp)) == ["VAROVÁNÍ"]


def test_archived_objects_are_skipped():
    camp = {"id": "cmpn_1", "name": "Podzim", "_ad_groups": [_group("a", tpl="", status="archived")]}
    assert utm.evaluate(camp) == []


def test_parse_json_output_error_is_readable():
    try:
        utm.parse_json_output("not json", "campaigns")
    except ValueError as e:
        assert "campaigns" in str(e)
    else:
        raise AssertionError("expected ValueError")
