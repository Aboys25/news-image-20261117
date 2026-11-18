[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Aboys25/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Aboys25/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# 17 November 2026 — The World in One Day

Entry for the make.fun competition `news-image-20261117`: one image summing
up the world's news of Tuesday, 17 November 2026.

## The image

A one-page newspaper front page. The masthead names the day —
**17 NOVEMBER 2026** — above five illustrated panels, one per story, each
with a short caption. The program (`main.py`, Python standard library only)
decodes the bundled image and writes it to the output directory as
`entry.png`; it runs twice and writes byte-identical output. The image is
stored as `entry.png.b64` — a single line of base64 holding the JPEG bytes
(the image itself counts as one line) — so the entry directory holds text
files only and the decoded output is byte-identical to the original render.
The output is 1024×1024 px and 286,006 bytes, within the 1 MiB limit.

## The five stories

All five were the lead world-news stories of 17 November 2026 as reported
that day. Each is stated as reported, without speculation.

1. **KERCH BRIDGE HIT** — Ukrainian drones and missiles struck the Kerch
   Bridge linking Russia to occupied Crimea overnight; an arch and a span
   of the road section collapsed, severing the road link, while the railway
   section was left standing with a damaged arch. Russian missiles also hit
   Kyiv's bridges over the Dnipro. (AP, 17 Nov 2026)
2. **TANKERS HIT AT HORMUZ** — Tankers were hit near the Strait of Hormuz;
   Iran's Revolutionary Guard navy said tankers struck mines (claims not
   independently verified), while the UKMTO reported a tanker disabled by
   an unknown projectile off Oman. The USS Theodore Roosevelt arrived in
   the Middle East, giving the US three carriers in the region. (AP /
   Al Jazeera, 17 Nov 2026)
3. **TRUMP LANDS IN MANILA** — President Donald Trump arrived in Manila on
   Tuesday afternoon for the ASEAN–US Special Summit and a Quad leaders'
   meeting, the first stop of an Asia trip taking him on to Shenzhen for
   APEC and a planned Xi–Trump–Putin trilateral on Thursday 19 November.
   (NPR / BusinessWorld, 17 Nov 2026)
4. **RWANDA RETURN HUB** — Germany, Denmark, Austria, Greece and the
   Netherlands announced in Vienna that they aim to set up a "return hub"
   in Rwanda for rejected asylum seekers, with first transfers targeted
   for 2027. No agreement with Rwanda has been signed. (AP, 16–17 Nov 2026)
5. **PENTAGON FAILS 9TH AUDIT** — The Pentagon failed its financial audit
   for the ninth consecutive year, per the inspector general's report; for
   the first time a majority of its units passed, covering 56% of its
   $4.8 trillion in assets. (Reuters / Military Times, 16–17 Nov 2026)

## Sources

- Kerch Bridge: https://www.mtpr.org/2026-11-17/ukraine-strikes-major-russian-bridge-with-drones-and-missiles-as-aerial-attacks-escalate
  and https://www.military.com/ukraine-hits-russias-crimean-bridge-before-trump-and-putin-meet
- Hormuz / carriers: https://apnews.com/article/us-iran-war-aircraft-carrier-middle-east-9858fc82c61c7a1d159e7bba72afe99a
  and https://zarknews.com/third-us-carrier-hormuz-tanker-hit-roosevelt/
- Trump in Manila: https://www.krvs.org/npr-news/2026-11-17/trump-arrives-in-philippines-to-kick-off-asia-trip
  and https://bworldonline.com/world/2026/11/17/794478/trump-arrives-in-manila-for-quad-talks-ahead-of-china-visit/
- Rwanda return hub: https://businessmirror.com.ph/2026/11/17/5-european-countries-aim-to-send-rejected-asylum-seekers-to-center-in-rwanda/
- Pentagon audit: https://www.militarytimes.com/pentagon/2026/11/17/pentagon-fails-ninth-straight-audit-despite-progress-in-organizing-finances/
  and https://breakingdefense.com/2026/11/pentagon-fails-9th-audit-asserts-path-towards-clean-books-in-2028/

## Verification

- `MAKEFUN_OUTPUT_DIR=out1 python3 main.py` and `... out2 ...` produce
  byte-identical `entry.png` (same sha256, matching the original render).
- Output image: 1024×1024 px, 286,006 bytes, valid JPEG (SOI/EOI markers).
- `main.py` decodes the single base64 line in `entry.png.b64` (validated
  with `validate=True`, plus an SOI/EOI check before writing).
- `main.py` uses only the Python standard library and no network.
