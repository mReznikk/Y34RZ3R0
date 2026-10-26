# Year Zero longread — typography research: big phrases (22 Oct 2026)

Measured in the browser at a 1440px viewport on each reference (computed font size, weight, tracking, line positions).

## What the references do

| Reference | Big phrases (measured) |
|---|---|
| fightclub-vg.tilda.ws/eng | Headings 130–140px (9–9.7vw), tracking ≈ −0.07em, 3 lines: line 2 indented ≈30%, weights alternate 600/700, last line on a red bar. Dialogue 44px (3.1vw) alternating left/right. Pinned list at 100px. ≈2 big phrases per screen. |
| war.artmilitonian.com | 140px (9.7vw) headline, one word per line, each word doubled solid + 1px outline. Figures at the same size. A phrase in 6 short caps chunks at 68px, 20–40% opacity, key figure more opaque. |
| after-life.ru/1 | Title words scattered at 100px with drifting duplicate copies. Centred stack, one word per line at 70px («ГОВОРЯТ, / ДУША / ВЕСИТ / 21 ГРАММ»). Counter at 120px. ≈3 per screen. |
| war.artmilitonian.com/oct10 | Date one word per line at 95px (6.6vw) in red; «141 countries / support Ukraine» stacked in outline at 60px. |
| abbaband.tilda.ws | Names at 100px mixing weights within a word (initial 700, rest 300); song-title walls at 90px caps; ≈2.4 per screen. |
| punkrock.tilda.ws/en | Section words 140–180px (10–12.5vw) with small 50px stacked labels overlapping; vertical title 118px. |
| linkinparkband.tilda.ws | Section titles only 40px caps, split into 2–3 lines arriving from off-screen copies; «A THOUSAND [disc] SUNS» at 100px. |

## Rules taken from them
- Display at 7–9vw against ~18px body (≈7× contrast); 1.5–3 big phrases per screen in argument-heavy stretches.
- A phrase is 2–4 short lines, one idea per line; lines staggered (indent ≈12–26%) or centred as a stack.
- Treatment changes inside a phrase: heavy condensed vs wide hairline, solid vs outline, one key word in signal colour or on a bar.
- Lines arrive one at a time (from alternating sides, stepped, or with a converging outline copy) and settle before reading position.

## Applied in «Проявка» (HTML prototype)
19 headers, conclusions and questions lifted out of their paragraphs, wording and order unchanged. Five rotating treatments: stagger, question, stack, ghost, mix. Phrases fit their widest line to the column; on phones they wrap at 34px. Body text untouched.
