# Tiletopia Design System — v1.0.0

Otoriter kaynak: oyunun implementasyonu (`tiletopia-dev`, v1.0.0). Bu belge
piksel değerleriyle birlikte tasarım kararlarının tümünü kaydeder; yeni ekranlar,
varyantlar ve Google Stitch tasarımları bu sistemden türetilir.

## 1. Marka kimliği

- **Ad:** Tiletopia (tüm dillerde aynı yazım)
- **Konsept:** tropik ada — üçlü-tile eşleştirme bulmacası; rehber karakter Koko
  (papağan). Tüm görsel dil: tatlı "juicy" meyve doku + ahşap + deniz.
- **Etiketlendiği sürüm:** v1.0.0 (manifest, SW cache `tiletopia-v1.0.0`,
  game.js banner, HTML comment — hepsi birebir aynı sürümü taşır)

## 2. Palet (hex) — CSS değişkenlerinden birebir

| Token | Hex | Kullanım |
| --- | --- | --- |
| `--wood` | `#c98a4b` | tile çerçevesi, ahşap |
| `--wood-dark` | `#a96f38` | tile kenar / gölge hattı |
| `--cream` | `#fff6e5` | panel dolgu, chip zemin |
| `--cream-2` | `#ffedc9` | tile iç yüzey (radial üstü) |
| `--sun` | `#ffd23f` | vurgu, yıldız, hint glow `#ffd23f` |
| `--sun-dark` | `#b87712` | sun tipografi kenarı |
| `--teal` | `#2ec4b6` | sayfa zemini, btn--secondary üstü |
| `--teal-dark` | `#21867a` | secondary alt, koyu dalga |
| `--coral` | `#ff5f6d` | watermelon / lose vurgusu |
| `--orange` | `#ff8f5e` | rewarded buton üstü |
| `--ink` | `#5c3a1e` | ana metin |
| `--ink-soft` | `#7a4a21` | ikincil metin / başlık |

**Kanvas arkaplan gradyanı** (renderer.ts:161): `#2ec4b6 → #7fe3d0 (%60) →
#ffe9b8` dikey; üstte yumuşak güneş `rgba(255,247,214,.9→0)` radial; bulutlar
`rgba(255,255,255,.22)`.

**Buton gradyanları**: primary `#ffb42e→#f59f1b` (metin `#6b3b10`);
secondary `#2ec4b6→#26a89c` (metin `#06332e`); rewarded `#ff8f5e→#f2603a`
(beyaz metin); ghost `rgba(255,246,229,.92)` + alt-gölge hattı
`rgba(120,84,40,.18)`.

## 3. Tipografi

- Yığın: `"Segoe UI", system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif`
- Ağırlık politikası: gövde 700, başlık/etiket 900, buton 800 + `letter-spacing: .06em`
- Ölçek (clamp, 360–768 arası ölçeklenir):

| Rol | Boyut |
| --- | --- |
| Logo/başlık | `clamp(40px, 11vw, 64px)` |
| Kazan kart başlığı | `clamp(24px, 7vw, 32px)` |
| HUD seviye sayısı | `clamp(20px, 6vw, 26px)` |
| Bar başlığı | `clamp(18px, 5vw, 24px)` |
| Buton | `clamp(15px, 4.2vw, 19px)` |
| Gövde | 15px / satır 1.6 |
| Chip/küçük etiket | 14px |
| Küçük not | 12.5px |
| HUD etiket | 12px + `ls .08em` |

## 4. Boyut & ızgara

- Köşe yarıçapı: **18px** paneller; butonlar tam **999px** (hap); tile `w*.17`.
- Gölge: `0 10px 24px rgba(42,84,66,.35)` (yeşilimsi düşük gölge);
  buton ekstruder gölgesi `0 6px 0 rgba(0,0,0,.14)` — "taşınır hissi".
- 44px dokunma hedefi: `min-height: 54px` buton, `48×48` iconbtn — iOS HIG
  ve App Store incelemesi için güvenli.
- Safe-area: `env(safe-area-inset-*)` dört kenara; HUD close `bottom:
  calc(env(safe-area-inset-bottom) + 2px)` gibi offset'ler korunur.
- Sahne iskeleti: `#ui-root` pointer-events none; `.scene` absolute inset 0 +
  `padding: 16px` (+safe-area max'lı yatay) — tek sütun, merkez.

## 5. Bileşen kuralları

- **`.btn`** — hap form, 3px aşağı `:active` (dokunma geri bildirimi), ikon
  `1.2em`. Varyantlar: `--primary` (oyunun ana CTA), `--secondary`, `--ghost`
  (panel üstünde nötr), `--rewarded` (turuncu; reklam ödül eylemi **her zaman**
  bu varyant), `--adclose` (reklam kartı kapatma; `rgba(0,0,0,.55)` + beyaz).
- **`.iconbtn`** — 14px radius krem kare, 28px ikon; duraklat/geri/kapat.
- **`.chip`** — krem zemin, ikon + metin (para, seviye göstergeleri).
- **`.bar`** — üst şerit başlığı; `h2` beyaz + `text-shadow 0 2px 8px rgba(0,0,0,.25)`.
- **Overlay kartı** — krem panel, başlık 900 + `ls .04em`, Koko/Lose art
  `clamp(110px, 26vw, 150px)` + `drop-shadow(0 8px 14px rgba(0,0,0,.2))`.
- **Tile** (renderer) — çerçeve `#c98a4b` stroke `#a96f38`; iç radial
  `#fff6e5→#ffedc9`; katman gölgesi `rgba(30,60,60, .18 + layer*.04)`;
  hint glow `shadowColor #ffd23f blur 14`.

## 6. Ekran envanteri (v1.0.0'da canlı)

1. **Menu** — logo `clamp(120px,30vw,180px)` Koko, birincil CONTINUE/PLAY,
   alt küçük PLAY (görünüm profili), ikonbtn'lar (reklam ödül, dil, müzik,
   ses).
2. **Levels** — 6 sütun `auto-fill minmax(72px)` grid; hücre `clamp(18px,5vw,24px)`
   numara; yıldız durakları.
3. **Settings** — satırlık ayar (toggle ikonlu) + info sağda `14px`.
4. **About** — Koko `clamp(120px,30vw,180px)`, gövde 15px/1.6 `#243c36`,
   fine print 12.5px `#47625a`.
5. **Game HUD** — sol chip (para), merkez seviye, sağ iconbtn duraklat; tray
   alt bölge (renderer çizer: koyu `rgba(122,74,33,.28)` plaka).
6. **Win/Lose overlay** — kart + Koko/Lose art + yıldız sırası + coins
   `22px/900` + `small 13px #8a6a3d`.
7. **Ad overlay** — kart + kalan süre `11px/900`, rewarded buton, adclose.
8. **Tutorial coach** — vurgulu tile + yönlendirme metni (Level 1).

## 7. Asset envanteri (kaynak SVG'ler `stitch/svg/`)

- **Meyveler (12):** banana, coconut, dragonfruit, kiwi, lychee, mango,
  papaya, passionfruit, pineapple, starfruit, strawberry, watermelon —
  tam kare viewBox, oyun tahtasında ~64–94px çizilir.
- **UI ikonları (20):** ad, back, close, coin, gift, hint, lang, music-on/off,
  pause, play, restart, shuffle, slot, sound-on/off, star, star-off, trophy,
  undo.
- **Karakter (2):** koko-idle (menu), koko-happy (win ekranı).
- **İkon seti:** `brand/png/` — iOS 20–1024px tam set (1024 pazarlama ikonu
  alpha'sız, merkez compositions, köşe yuvarlaması yok — iOS otomatik yapar).

## 8. Çeviri metin stili (TR/EN)

Kısa, kibar, eylem odaklı; "Koko" varsa kişi adı aynen taşınır. Fine-print
(about/ilk açılış) iki dilde de bulunur: gizlilik (çerez yok, veri cihazda
kalır) ve sorumluluk reddi. Reklam etiketi: "Reklam" / "Ad" chip'i adclose
butonunda görünür kalır.

## 9. Stitch akışı

1. Google Stitch'te yeni bir design request: prompt'a bu dosyanın §2–§5
   (palet + tipografi + boyut + bileşen) yapıştır.
2. Üretilen ekran/lar `stitch/export/` içine konur (HTML+CSS ya da SVG).
3. `tools/compare.mjs` (tiletopia-dev) mevcut canlı UI ile piksel/renk
   farkını raporlar; sapmalar ya sisteme ya oyna geri geri döner.
4. Kabul kriteri: palet hex'leri birebir; buton yükseklik ≥54px; safe-area
   korunmuş; metin ölçekleri §3 tablosunda.

## 10. Lisans

Bu repo `tiletopia-dev` (private) ürününden türetilmiştir; tüm sanat eseri,
kod ve metinler bu proje için özgün üretilmiştir. Triple Tile benzeri
oynanış, fikir düzeyinde benzerlik taşır; adlar, görseller, sesler, metinler
ve kaynak kod kopyalanmamıştır — hukuki plajya yoktur.
