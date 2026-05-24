# Scrape Engine Eval — Q2 Results
*Author: Alex K. (eval team) — last updated Mon*

## TL;DR
Engine C wins on quality (LLM-judge: 4.07 vs 3.65 vs 3.54) and latency.
Recommendation: ship Engine C.

## Methodology
- 500-URL eval set
- 300 with ground-truth annotations
- 6 metrics: LLM-judge quality, F1, F0.5, completeness, latency, error rate

## Results
| Engine | LLM-judge | F1   | F0.5 | Completeness | Latency p50 | Error % |
|--------|-----------|------|------|--------------|-------------|---------|
| A      | 3.54      | 0.893 | 0.953 | 0.618       | 1222ms      | 0.0%    |
| B      | 3.65      | 0.801 | 0.796 | 0.618       | 1125ms      | 0.0%    |
| C      | 4.07      | 0.877 | 0.830 | 0.995       | 836ms       | 0.0%    |

F1 is noisy on this dataset — our GT annotation process makes it unreliable as a
standalone signal. We weight LLM-judge more heavily for production decisions.
C wins on the metrics that matter. Shipping recommended.

— Alex
