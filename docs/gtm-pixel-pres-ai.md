# Pixel OpenAI do Google Tag Manageru pomocí AI

Postup, kterým nasazujeme pixel ChatGPT Ads (OpenAI) přes Google Tag Manager bez programátora:
AI agent (u nás Claude s přístupem do prohlížeče) to v GTM naklikne, člověk zkontroluje a schválí.
Vyzkoušeno na e-shopu na Shoptetu (září 2026). S jinými agenty než Claude jsme to nezkoušeli.

Obecná pravidla měření (souhlas s cookies, CSP, obrázkový tag, CAPI) jsou v
[playbooku, kapitola 5](../skill/chatgpt-ads/chatgpt-ads-campaign-playbook.md#5-measurement-details-that-bite).

## Než začnete

1. **V Ads Manageru založte zdroj dat (pixel) a konverzní událost** a událost **připojte ke kampani**
   (Nástroje → Konverze). Z CLI: `pixels`, `event-setting-create`, `campaign-update --conversion-event-setting-id`,
   kontrola `conversion-check`.
2. Poznamenejte si **ID pixelu** (`pixels`).
3. AI pracuje v okně prohlížeče, kde jste **přihlášení do GTM vy**. Hesla ani přístupy mu nedávejte.

## Zadání pro AI (zkopírujte a doplňte)

```text
Otevři Google Tag Manager kontejneru našeho webu <doména>.
1. Přidej vlastní HTML tag "OpenAI Ads – init" na všechny stránky s pixelem <ID pixelu>
   podle oficiálního kódu z developers.openai.com/ads/measurement-pixel.
   Pokud web používá cookie lištu, nastav souhlas podle playbooku (consent false před init).
2. Přidej tag "OpenAI Ads – order_created" na událost nákupu a jako event_id pošli
   číslo objednávky (proměnná z dataLayer, např. transaction_id).
3. Nic nepublikuj. Ukaž mi náhled změn a čekej na moje schválení.
4. Po publikaci ověř na webu, že události odcházejí na správný pixel.
```

## Tag na nákup (vzor, který u nás běží)

Vlastní HTML tag, spouštěč = událost nákupu z dataLayer (na Shoptetu `purchase`).
`{{DLV - transaction_id}}` je proměnná vrstvy dat s číslem objednávky (`eventModel.transaction_id`
nebo `ecommerce.transaction_id`, podle webu).

```html
<script>
(function () {
  var t = {{DLV - transaction_id}};
  if (typeof oaiq !== "function") return;
  if (t) {
    oaiq("measure", "order_created", { type: "contents" }, { event_id: "order_" + t });
  } else {
    oaiq("measure", "order_created", { type: "contents" });
  }
})();
</script>
```

**Proč `event_id`:** e-shopové platformy umí poslat událost nákupu víckrát (opakované načtení
děkovací stránky, víc pushů do dataLayer). Bez `event_id` se každé odpálení počítá jako nákup.
U nás platforma nahlásila 4 nákupy, skutečně proběhla 1 objednávka. OpenAI podle `event_id`
duplicity slučuje (pixel + název události + id).

Hodnotu objednávky (`amount`) jsme zatím neposílali, jednotky jsme neověřili. Bez ní uvidíte
počet konverzí, ne hodnotu a ROAS.

## Kontrola po publikaci

1. **Správný účet.** Pixel na webu může patřit jinému reklamnímu účtu a navenek vypadá v pořádku.
   V konzoli prohlížeče na webu:

   ```js
   performance.getEntriesByType("resource").map(r => r.name).filter(u => u.includes("bzr.openai.com"))
   ```

   `pid` v adrese musí sedět s ID pixelu z `pixels` vašeho účtu.
2. **Události chodí.** `conversion-events --pid <ID pixelu>` ukáže poslední zachycené události.
3. **Po první objednávce:** platforma má hlásit 1 konverzi, ne víc. Porovnejte s Analytics
   (návštěvy s `oppref` ve vstupní URL) po 48–72 hodinách.

## Bezpečnost

- AI publikuje verzi v GTM až po vašem výslovném schválení.
- Starou verzi kontejneru jde kdykoli vrátit: GTM → Verze → předchozí verze → Publikovat.
- Na kód tagu se dívejte stejně jako na kód od člověka: co odesílá a kam.
