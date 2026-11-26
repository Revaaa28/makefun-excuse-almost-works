# Candidates — The Excuse That Almost Works

Competition: `u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5`
Task: one line a gamer texts the boss to skip work on GTA 6 launch week, at most 20 words.
Gate: `/output/entry.txt`, UTF-8, 1–140 chars, not only whitespace.

## Judge brief criteria (in order — this is the ranking order)

1. On-subject: an excuse a gamer sends a boss to skip work on GTA 6 launch week, one line, ≤ 20 words. Loses to any excuse on the subject.
2. Believable to a tired manager: a real, specific, boring workplace detail rather than a wild story.
3. Funny on its own terms: the laugh comes from the excuse's own logic or detail, not a joke bolted on the end.
4. Reads like a text sent in a hurry: one line, plain words, no setup, no explanation, no signature.
5. Fresh angle: not a dead grandmother, a flat tyre, or a sudden fever.

A long excuse sounds rehearsed; a rehearsed one is already a confession.

## Candidates (all one line, ≤ 20 words)

| # | Text | Words | Chars |
|---|------|-------|-------|
| 1 | Have to wait in for a delivery, they only gave a nine to five window. | 15 | 69 |
| 2 | The plumber's coming between nine and twelve to fix the leak under the sink, I have to be in. | 19 | 94 |
| 3 | My new mattress gets delivered between eight and one and someone has to sign for it. | 16 | 83 |
| 4 | The council's resurfacing our street today and they've blocked my driveway in. | 13 | 76 |
| 5 | The internet guy's coming to fix the router sometime before lunch, I have to be home. | 16 | 83 |
| 6 | My landlord's sending someone to check the damp in the bathroom this morning, I have to let them in. | 19 | 99 |
| 7 | The lift in my building broke and I'm on the twelfth floor with a bad knee. | 16 | 74 |
| 8 | My passport appointment got moved to this morning and I have to bring the originals in person. | 17 | 93 |
| 9 | Sorry, my car failed its MOT and the garage can only fit me in first thing tomorrow. | 16 | 82 |
| 10 | The electrician's rewiring the fuse box, he said keep the power off till he's done. | 14 | 80 |

## Manual ranking (criteria in stated order — no judge API used)

**Criterion 1 — on-subject, ≤ 20 words:** all ten pass. Shorter reads less rehearsed, so #1 (15), #4 (13) and #10 (14) start ahead of #2/#6 (19).

**Criterion 2 — believable, specific, boring:** #2 (plumber + leak under the sink) and #6 (landlord + damp check) are the most boring-real. #1 (delivery window) and #3 (mattress delivery) are close behind — waiting in for a delivery is the most ordinary excuse a manager hears. #7 (lift + bad knee) is specific but the knee invites a follow-up question. #9 (MOT failure) is believable but sits in the car-trouble family. #10 is weak here: power off at home is no reason to miss an office shift.

**Criterion 3 — funny from its own logic:** #1 wins outright. The laugh is the excuse itself: a "delivery" with a nine-to-five window on GTA 6 launch week is obviously the game, and the whole work day is the window — the manager almost believes it precisely because waiting in for a delivery is boring, while the office knows exactly what is being delivered. #4 is second: "they've blocked my driveway in" is a vivid, self-contained image. #3's mattress is mildly funny (a mattress needs a signature; a game parcel does too). #2, #5, #6, #8 are believable but carry no laugh of their own. #10's logic backfires: with the power off he couldn't play GTA either.

**Criterion 4 — hurried text, no setup/explanation/signature:** #1 starts mid-thought ("Have to wait in…") — no "Sorry boss", no preamble. #4 and #7 are equally blunt. #2 and #6 explain themselves ("I have to be in / let them in") and read rehearsed. #9 opens with "Sorry," which is setup.

**Criterion 5 — fresh angle:** #1 (delivery window), #3 (mattress), #4 (council resurfacing), #7 (lift) are all fresh. #9 is car trouble — adjacent to the banned flat-tyre family. #5 (router) is fresh but thin.

## Pairwise check vs a strong rival

The strong rival shape is the best generic entry: "Sorry, my boiler broke and the engineer can only come today." It is believable (criterion 2) and short, but it has no GTA subtext and no laugh of its own (criteria 3 and 5 are empty).

- #1 vs that rival: wins on 3 (the delivery-window joke IS the GTA hook, without naming the game — naming it would kill believability under criterion 2) and on 5 (fresh angle), and on 4 (no "Sorry", starts mid-thought). The rival only ties on 2. **#1 beats the rival.**
- #4 vs that rival: wins on 3 (blocked driveway image) and 5, ties on 2, but "council resurfacing" is a same-day surprise a manager may doubt — slightly weaker than #1 on 2.
- #2 vs that rival: ties on 2, loses on 3 and 4 (long, explanatory). Loses overall.
- #3 vs that rival: ties on 2, small win on 3 (mattress signature), but the laugh is weaker than #1's.

## Ranking

1. **#1** — Have to wait in for a delivery, they only gave a nine to five window.
2. #4 — The council's resurfacing our street today and they've blocked my driveway in.
3. #3 — My new mattress gets delivered between eight and one and someone has to sign for it.
4. #2 — The plumber's coming between nine and twelve to fix the leak under the sink, I have to be in.
5. #7 — The lift in my building broke and I'm on the twelfth floor with a bad knee.
6. #6 — My landlord's sending someone to check the damp in the bathroom this morning, I have to let them in.
7. #5 — The internet guy's coming to fix the router sometime before lunch, I have to be home.
8. #8 — My passport appointment got moved to this morning and I have to bring the originals in person.
9. #9 — Sorry, my car failed its MOT and the garage can only fit me in first thing tomorrow.
10. #10 — The electrician's rewiring the fuse box, he said keep the power off till he's done.

## Chosen line (v1)

> Have to wait in for a delivery, they only gave a nine to five window.

15 words, 69 characters. One line, plain words, no setup, no explanation, no signature.
The delivery is never named — that is the point: the manager almost believes it because
waiting in for a delivery is the most boring real excuse there is, and the office knows
what launch-week parcel needs a nine-to-five window.

## Revision note (v1 → v2, made in-session after validation)

Weak spot found in v1 on re-read: the manager's obvious reply is "leave it with a
neighbour" — v1 gives no reason the gamer himself must stay home. v2 closes that hole
inside the excuse's own logic, without naming GTA and without adding a bolted-on joke:

> Have to wait in for a delivery, they gave a nine to five window and someone has to sign.

19 words, 88 characters. "Someone has to sign" is why he cannot leave — it strengthens
criterion 2 (believability: a specific, boring, verifiable-sounding constraint) at the
cost of one small clause on criterion 4, a trade the criteria order supports (2 outranks 4).
The GTA subtext survives untouched: the signature parcel on launch week is the game.
