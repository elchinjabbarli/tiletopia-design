# tiletopia-design

Tiletopia'nın tasarım katmanı — marka, design sistemi ve Google Stitch
tasarım akışı. Oyunun kendisi [tiletopia](https://github.com/elchinjabbarli/tiletopia)
(public build) ve [tiletopia-dev](https://github.com/elchinjabbarli/tiletopia-dev)
(private kaynak) repo'larındadır.

## Ne var burada

- **[DESIGN-SYSTEM.md](DESIGN-SYSTEM.md)** — otoriter tasarım kaydı: palet
  (hex), tipografi ölçeği, ızgara/safe-area, bileşen kuralları, ekran
  envanteri, asset envanteri, Stitch kabul kriterleri.
- **`brand/`** — App Store pazarlama ikonu (1024, alpha'sız, köşe yuvarlaması
  yok) + tam iOS ikon seti (`png/` 20→1024). Kaynak `icon-1024.svg`.
- **`ui/`** — 20 UI ikonu + Koko karakterinin iki durumu (SVG kaynak + PNG).
- **`assets/`** — 12 özgün meyve sprite (SVG kaynak + PNG).
- **`screens/`** — v1.0.0 ekranlarının doğrulanmış PNG referansları.
- **`stitch/`** — Google Stitch tasarım akışı: `svg/` kaynaklar, `export/`
  Stitch çıktılarının geldiği yer, `PROMPTS.md` hazır promptlar.

Version: 1.0.0 — design repo, oyunun v1.0.0 sürümünden türetilmiştir.

## Stitch kullanımı

`stitch/PROMPTS.md` içindeki prompt'ı Google Stitch'e verin; çıktıyı
`stitch/export/` altına koyun. Kabul kriterleri DESIGN-SYSTEM.md §9'da:
palet hex birebir, buton yüksekliği ≥54px, safe-area korunmuş.

## Lisans / özgünlük

Tüm sanat eseri, karakter, ikon, metin ve kod bu proje için sıfırdan
üretilmiştir. Oynanış türü (üçlü-tile eşleştirme) fikir düzeyinde yaygın bir
türdür; Triple Tile'e ait hiçbir varlık, isim, görsel veya ses kopyalanmamış,
taklit edilmesi amaçlanmamıştır.
