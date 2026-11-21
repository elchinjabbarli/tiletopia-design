# Google Stitch prompt'ları

Stitch'e yapıştırın; çıktıyı `stitch/export/<ekran>.html` olarak koyun.

## Ana prompt (tüm sistem)

```
Design a mobile puzzle-game UI for "Tiletopia", a tropical island
triple-tile matching game, portrait phone layout with iOS safe-area padding.

Palette (exact hex): wood #c98a4b, wood-dark #a96f38, cream #fff6e5,
cream-2 #ffedc9, sun/yellow #ffd23f, teal #2ec4b6, teal-dark #21867a,
coral #ff5f6d, orange #ff8f5e, ink text #5c3a1e, soft ink #7a4a21.
Background: vertical gradient #2ec4b6 -> #7fe3d0 (60%) -> #ffe9b8 with a soft
sun glow and low-opacity clouds.

Typography: system UI font, headings weight 900, buttons weight 800 with
letter-spacing .06em. Title clamp(40px,11vw,64px), section clamp(24px,7vw,32px),
HUD level clamp(20px,6vw,26px), buttons clamp(15px,4.2vw,19px), body 15px/1.6.

Components: pill buttons (radius 999px, min-height 54px) with a pressed
extruder shadow "0 6px 0 rgba(0,0,0,.14)"; primary gradient #ffb42e->#f59f1b
with dark text #6b3b10; secondary #2ec4b6->#26a89c text #06332e; rewarded
orange #ff8f5e->#f2603a white text; cream cards radius 18px shadow
"0 10px 24px rgba(42,84,66,.35)". 48px square icon buttons on cream
rgba(255,246,229,.92).

Screens needed: main menu (parrot mascot "Koko", big logo, primary
CONTINUE button), level map grid (6 columns of numbered tiles with star
ratings), in-game HUD (coins chip, level, pause), win overlay card with
stars and coins, lose overlay, rewarded-ad card with countdown and close.
Style: juicy, friendly, fruity, wooden-game feel; no dark mode.
```

## Ekran bazlı kısa prompt'lar

- **Menu:** `Main menu for "Tiletopia": teal-to-cream gradient sky, sun glow,
  parrot mascot, logo in cream with dark outline, primary pill button
  "CONTINUE" (#ffb42e->#f59f1b), small icon buttons for gift/rewarded ad,
  language, music, sound on cream circles.`
- **Level map:** `Level select grid, 6 columns, cream cells with wood frame
  (#c98a4b stroke #a96f38), level numbers weight 900, 0–3 gold stars
  (#ffd23f) below each, background gradient teal to cream.`
- **Game HUD:** `Portrait game screen top bar: left coin chip (cream pill,
  coin icon, count), centered level number, right pause icon button; fruit
  tiles on wood-framed cream squares stacked in layers over the gradient.`
- **Win overlay:** `Victory card on dimmed teal: cream card radius 18px,
  happy parrot mascot, three gold stars, coin reward row "22px weight 900",
  primary pill button NEXT.`
- **Rewarded ad:** `Rewarded-ad card: orange gradient button #ff8f5e->#f2603a,
  countdown "11px weight 900", dark close button rgba(0,0,0,.55) white text
  labeled "Ad".`

## Kabul kriterleri (Stitch çıktısı için)

1. Palet hex'leri birebir (DESIGN-SYSTEM.md §2).
2. Buton yüksekliği ≥54px; iconbtn 48px.
3. Safe-area padding korunmuş.
4. Metin ölçekleri §3 clamp tablosuna uygun.
5. Reklam eylemi hep turuncu rewarded varyantı; kapatma hep adclose.
