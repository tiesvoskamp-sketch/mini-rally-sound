# Mini Rally Sound

Virtueel turbo-4 rallygeluid voor de Mini via AUX. Geen dongle nodig: het toerental wordt geschat uit
de versnellingsmeter + GPS van de iPhone.

- `app.html` — de bron (één bestand: geluidsmotor, schatting toerental/versnelling, interface).
  Wordt ook als Claude-artifact gepubliceerd: https://claude.ai/artifact/XD1FHzVb5Kmr7bYEkASjvK
  (daar alleen simulatie + demo: artifacts krijgen geen toegang tot bewegingssensor en GPS).
- `build.py` — maakt `docs/index.html` (volledige pagina) voor hosting, nodig voor gebruik in de auto.

## Hoe het werkt
1. Zwaartekracht wordt uit de versnellingsmeter gefilterd → horizontale versnelling.
2. 'Vooruit' wordt geleerd door die versnelling te vergelijken met GPS-snelheidsveranderingen.
3. Snelheid = GPS (1×/s) aangevuld met de versnellingsmeter (60×/s).
4. Gas-schatting = (versnelling + rol/luchtweerstand) / max. versnelling bij die snelheid × gevoeligheid.
5. Handbak-modus: opschakelen = korte dip in versnelling tijdens optrekken; terugschakelen bij lage toeren
   of als je harder trekt dan de huidige versnelling kan.
6. Geluid: vuurpulsen van 4 cilinders → uitlaatresonanties → verzadiging → filter, plus inlaat, turbo,
   blow-off-flutter, knallen bij gas los, rechte-tandwielen-gejank.

## Beperkingen
- Geschat toerental, niet echt: stilstaand gas geven met koppeling in hoort de app niet.
- Safari moet open en op de voorgrond blijven (scherm blijft aan via wake lock).
- Echte toerental-data → OBD-dongle (BLE) + native iOS-app.
