# Co jsme se naučili z 8 českých účtů (PLACEMENT.cz)

> Poznatky z provozu ChatGPT Ads na osmi účtech, **1. 9. – 4. 10. 2026**: 5 e-shopů, 3 služby,
> 428 351 zobrazení, 10 217 prokliků, ~3 718 € útraty, 65 konverzí podle platformy.
> Klienti jsou anonymizovaní (A–F). Jmenovitě jen naše vlastní účty: **Placement.cz** (agentura včetně
> webinářů) a **Království zdraví** (e-shop s doplňky stravy).
>
> **Je to pozorování, ne statistika.** Každý účet má jiný obor, rozpočet i nastavení. Kde je něco
> domněnka, je to tak napsané. Čísla v Kč, EUR přepočteno kurzem 24,5 Kč.
>
> Skill tenhle soubor čte jako doplněk k playbooku. Kde se s playbookem rozchází, platí data níž
> jen pro český a slovenský trh a pro uvedené období.

## 1. Celkový obrázek

| Účet | Útrata | CTR | Cena kliku | Konverze (platforma) |
|---|---|---|---|---|
| Klient A · nábytek na míru | 5 280 Kč | 5,01 % | 3,15 Kč | 18 poptávek |
| Klient C · e-shop, zahrada | 15 225 Kč | 4,36 % | 4,33 Kč | 10 nákupů (+20 po zobrazení) |
| Klient D · e-shop, elektronika | 3 201 Kč | 2,84 % | 4,99 Kč | 3 nákupy |
| Klient B · e-shop, oblečení | 10 635 Kč | 2,66 % | 6,77 Kč | 5 nákupů |
| Klient E · e-shop, sport | 5 194 Kč | 2,05 % | 8,26 Kč | 4 nákupy |
| Království zdraví · doplňky stravy | 12 466 Kč | 1,81 % | 15,40 Kč | 20 nákupů (GA4: 5) |
| Klient F · lokální služba | 7 089 Kč | 0,91 % | 25,41 Kč | neměří se (bez pixelu) |
| Placement.cz · agentura | 32 012 Kč | 0,86 % | 29,37 Kč | 5 konverzí |

**Pozorování:** nejvyšší CTR a nejlevnější klik měly účty s konkrétním produktem nebo službou
(kuchyně na míru, záhony), nejnižší B2B služby. Domněnka k B2B: reklamy vidí jen
uživatelé plánů Free a Go (dokumentace OpenAI), rozhodovatelé ve firmách často používají placené plány.

## 2. Kontextové fráze (context hints)

| Zjištění | Data |
|---|---|
| **Nákupní dotazy fungovaly nejlíp** | Klient C, fráze typu „najdi mi záhon“, „kde koupit záhon“, „doporuč mi záhon na zeleninu“ (30 frází): 67 299 zobrazení, CTR 4,64 %, klik 4,05 Kč. Nejlepší velká sestava e-shopů. |
| **Krátké klíčovky > dlouhé situace a popisy** | Stejné reklamy, jiné fráze. Klient B (bundy): klíčovky 12 072 zobrazení, CTR 3,25 % vs. situace 5 664, CTR 2,56 %. Klient E: 2,31 % vs. 1,85 %. Dlouhé věty platforma páruje skoupěji. |
| **Otázky vs. klíčovky: nerozhodnuto** | Království zdraví, hořčík, stejná reklama: 17.–23. 9. otázky 1 901 zobrazení / klíčovky 0, 24.–29. 9. otázky 435 / klíčovky 2 337. Doručování se mezi sestavami přelévá po dnech. Test hodnoťte po 3–4 týdnech, nikdy z jednoho týdne. |
| **Úzké > široké** | Placement.cz: 8 konkrétních situací („hledám PPC agenturu pro e-shop“) CTR 0,92 %, klik 1,00 € vs. 36 témat („Google Ads“, „PPC reklama“) CTR 0,74 %, klik 1,54 €. Fráze „Google Ads“ znamená kohokoli, kdo s ChatGPT řeší Google Ads, ne toho, kdo hledá agenturu. |
| **Poradenské dotazy: levné, ale skoro bez zobrazení** | Klient C, „jak založit záhon“, „čím ho naplnit“ (9 sestav, strop 2 Kč): za 17 dní 743 zobrazení, CTR 6,06 %, klik 1,88 Kč, 1 nákup. Poradenské sestavy měly i nižší strop, takže nevíme, co z toho omezilo zobrazení. |
| **Bez reportu dotazů a bez vylučování** | Nevidíte, na jakou konverzaci se reklama ukázala. Jediná páka na relevanci je, jak úzce situaci popíšete. Jedna sestava = jeden záměr. |

## 3. Texty reklam

| Zjištění | Data |
|---|---|
| **Titulek, který zní jako doporučení** | Klient C, stejný text „Postavíte za jedno odpoledne“: „Doporučujeme tento záhon“ CTR 5,10 % (38 993 zobrazení, klik 3,65 Kč) vs. „Záhony“ 4,57 %. „[materiál] záhon / [materiál], návod v balení“ 1,55 %, klik 11,41 Kč. |
| **Vlastnost produktu > „od výrobce“** | Klient B, stejná sestava: „Membránové bundy“ 3,88 % vs. „Bundy od výrobce“ 0,83 % (klik 5,04 vs. 20,09 Kč). „Od výrobce“ prohrálo u bund, mikin i obuvi, vyhrálo jen u kalhot (4,05 % vs. 3,61 %). |
| **Konkrétní výhoda > cena a sleva** | Klient A: „Kuchyň na míru / 3D návrh zdarma. …“ 5,02 %. Klient D: „Smart hodinky česky / Volání z ruky, kompletně česky.“ 3,30 % vs. „Chytré hodinky / … Skladem od … Kč.“ 2,59 %. Agentura (webináře): sleva „1 990 Kč místo 2 770 Kč“ 0,46 %, „Webinář PPC za 990 Kč“ 0 kliků ze 164 zobrazení. |
| **Stejné pořadí ve dvou zemích** | Placement.cz CZ i SK: „Umíme reklamu v ChatGPT? / Právě se na ni díváte.“ 0,98 % a 1,01 % > „Vy tu ještě neinzerujete?“ 0,69 % a 0,76 % > „Jsme tady dřív než většina“ 0,66 % a 0,65 %. |
| **U stejného produktu intuice selhává** | Království zdraví: „Betaglukan na tři měsíce“ 2,24 % porazil „Betaglukan z hlívy“ 1,57 %, ale „Céčko na dva měsíce“ 0,46 % prohrálo s „Lipozomální vitamín C“ 1,53 %. Malé vzorky (stovky zobrazení). Nechte běžet 2–3 varianty. |

Doporučené délky: titulek ~16 znaků, text ~32. Klient F měl titulky ~30 a texty ~70 znaků a CTR 0,91 %
(spolu s automatickou nabídkou, takže příčinu nelze oddělit).

## 4. Cena kliku, strop a noc

- **Cena kliku je hlavně výsledek CTR.** Cena za tisíc zobrazení je v rámci účtu skoro stejná, takže
  cena kliku ≈ CPM ÷ (1 000 × CTR). Klient A: 6,43 € za tisíc, CTR 5,01 % → 0,13 €. agentura Placement.cz:
  10,32 €, CTR 0,86 % → 1,20 €. Lepší zadání a text zlevní klik víc než nižší nabídka.
- **Pevný strop ceny za klik funguje a vyšší strop klik zdraží.** Klient A zvedl strop z 3,0–3,9 na
  4,5–5 Kč (2. 10.) a klik podražil z 3,03 na 3,73 Kč při stejné CTR. Klient C: sestava se stropem
  3,66 Kč → klik 4,05 Kč, sestava se stropem 12,75 Kč → klik 18 Kč, CTR 1,3 %, vypnuto po 2 dnech.
- **Bez stropu se rozpočet propálí v noci.** Podíl útraty mezi 0 a 6 h (pražského času): Království zdraví 39 %
  (klik v noci 0,94 € vs. 0,52 € přes den), agentura Placement.cz 22 %, Klient A s pevným
  stropem 1 %. API nemá časové plánování. Proč platforma utrácí po půlnoci, nevíme.
- **Tři e-shopy, klik z 15–25 Kč na 3–6 Kč za tři týdny** (B 22,95 → 3,69, C 14,82 → 3,35, E 25,07 → 5,58 Kč
  týdně). Současně rostla CTR (C 1,63 → 5,41 %). Co pomohlo: nižší pevný strop, krátké nákupní fráze,
  titulek s výhodou, vypnutí slabých reklam po ~100 klicích.

## 5. Měření

- **Konverze platformy neberte bez Analytics.** Království zdraví do 4. 10.: platforma 20 nákupů,
  GA4 (přes `oppref`) 5 objednávek. Pixel bez `event_id` počítal jednu objednávku až 4× (Shoptet posílá
  nákup víckrát). Oprava: `event_id` = číslo objednávky. Klient B: platforma hlásila nákup před
  spuštěním kampaně, GA4 0 nákupů z 196 návštěv za prvních 15 dní.
- **Proklik není návštěva.** Království zdraví 2.–6. 9.: na web dorazilo ~40 % prokliků (Google Ads na
  stejném webu 78 %). Příčinu nevíme.
- **Návštěvy s `oppref`** ve vstupní URL v GA4 = skutečné návštěvy z reklam. Musí se shodovat
  s návštěvami `chatgpt / cpc`, jinak nefungují UTM. Kontrolu dělejte po 48–72 h, GA4 se zpožďuje.
- **Pixel na webu může patřit jinému účtu** ze stejného tenantu a navenek vypadá v pořádku.
  Ověření: `pid` v requestu na `bzr.openai.com/v1/sdk/events` porovnat s výpisem `pixels` účtu.
- **Před spuštěním vždy `scripts/utm_check.py --account <name>`** (exit ≠ 0 = nespouštět).

## 6. Produktové kampaně (první týden, 29. 9. – 5. 10. 2026)

| Kampaň | Zobrazení | CTR | Klik | Nákupy |
|---|---|---|---|---|
| Klient D · elektronika | 2 119 | 3,11 % | 5,56 Kč | 1 |
| Klient B · oblečení, po kategoriích, strop 6 Kč | 13 041 | 2,65 % | 7,56 Kč | 1 |
| Klient C · katalog nad 400 Kč (jen 5. 10.) | 3 170 | 2,02 % | 8,69 Kč | 0 |
| Království zdraví · jen vlastní značka | 3 769 | 0,90 % | 1,39 € | 0 |
| Klient B · celý katalog bez stropu (vypnuto) | 3 381 | 0,65 % | 60,42 Kč | 0 |
| Klient E · sport | 47 | – | – | 0 |

- **Ve stejném účtu měly produktové kampaně zatím nižší CTR a stejný nebo dražší klik než textové**
  (B 7,56 vs. 4,16 Kč, C 8,69 vs. 3,41 Kč, D 5,56 vs. 5,18 Kč, Království zdraví 1,39 vs. 0,62 €).
- **Pozorování, příčina neznámá:** po spuštění produktové kampaně dostaly textové kampaně stejného
  účtu méně zobrazení (B: 8 256 → 2 745 za týden). U klienta E ale klesly i bez ní.
- **Stav produktů API nevrací.** Je jen v Ads Manageru: Kampaně → Produkty → zrušit výchozí filtr
  „Imprese > 0“ (jinak zamítnuté produkty nevidíte). Stavy: Schváleno · Kontrola vyžaduje pozornost
  (řeší podpora) · Neschváleno (opravit feed) · Zamítnuto.
- **Doplňky stravy skoro neprojdou.** Království zdraví: z 84 produktů prošlo 5, a to nápoje.

### Když feed neprojde: ruční testovací feed

1. Claude porovná feed se specifikací a zásadami: HTML entity v popisech, zdravotní a účinková
   tvrzení, délky textů, povinná pole.
2. Vyrobí ruční feed z vybraných produktů s čistým popisem (název, složení, balení, bez tvrzení).
3. Nahrát jako **samostatný** feed, původní zůstane.
4. Porovnat stav produktů v záložce Produkty.

Výsledek u nás: Království zdraví 30. 9., 17 produktů bez jakýchkoli tvrzení → 17/17 „Kontrola vyžaduje
pozornost“, stejně jako s původními texty. Test tedy ukázal, že **nejde o texty, ale o kategorii**, a řeší
se to s podporou OpenAI. Rychlý způsob, jak tyhle dvě příčiny oddělit.

## 7. Účet a provoz

- **Účet jde založit i na osobní Gmail.** Jednou nám zakládání skončilo hláškou „You don't have permission
  to create ad accounts in your tenant“, pomohlo pozvání z jiného účtu. Proč, nevíme; jindy osobní Gmail prošel.
- **Reklamy na jinou doménu čekají na prověření.** Když reklama vede jinam než na web účtu (i na subdoménu),
  OpenAI doménu nejdřív prověří (HTTP 425 při aktivaci). U nás přes 2 hodiny; po přepnutí webu účtu na tu doménu
  hned prošly. Samostatný účet pro subdoménu nutný není, reklamy na subdoménu běžely i z účtu hlavní domény.
- **Názvy účtu nejsou kosmetika.** Změna názvu značky pozastaví doručování do schválení, změna právního
  názvu spustí nové ověření firmy.
- **API klíč patří na `api.ads.openai.com`.** Vypadá jako běžný klíč OpenAI; proti `api.openai.com`
  vrací 401/429 a svádí k závěru, že je rozbitý.
- **Doručování umí na den vypadnout** bez zjevné příčiny (Království zdraví 2.–3. 10.: 21 zobrazení
  za den při aktivní kampani a volném rozpočtu). Druhý den zase normálně.

## 8. Jak bychom začínali dnes

1. Jedna kampaň, 15 € denně, s datem konce.
2. Jedna sestava = jeden konkrétní záměr, 20–30 krátkých nákupních frází („najdi mi…“, „kde koupit…“).
3. Nízký pevný strop ceny za klik.
4. 3–5 reklam s různými argumenty, výhoda v titulku, žádná cena.
5. Pixel s `event_id`, konverzní událost připojená ke kampani, plné UTM na každé sestavě, `utm_check.py`.
6. Vyhodnotit po ~100 klicích na sestavu, nákupy v Analytics přes `oppref`.
