# Firecrawl Scrape Engine Eval

We're evaluating three candidate scrape engines — A, B, and C — before deciding which to ship to production. Your job is to assess the eval methodology, understand the results, and form an opinion on whether we should ship Engine C.

A teammate ran the eval and left their writeup in `RESULTS.md`. Take a look at the numbers, dig into the code, and come ready to discuss.

## The situation

We have three scrape engines deployed to Vercel. Each one takes a URL and returns a markdown representation of the page. We've run them against a 500-URL eval set and a 100-URL production sample. We have ground truth annotations for 300 of the eval URLs.

The results are in `RESULTS.md`. We're inclined to ship Engine C based on those numbers, but we want a second opinion before we do.

## Repo layout

```
├── data/
│   ├── seed_urls.json              # 500 eval URLs with category tags
│   ├── prod_sample_urls.json       # 100 production sample URLs
│   ├── cache_a/                    # Pre-generated Engine A outputs
│   ├── cache_b/                    # Pre-generated Engine B outputs
│   ├── cache_c/                    # Pre-generated Engine C outputs
│   └── ground_truth/               # 300 ground truth .md files
├── eval/
│   ├── metrics.py                  # F1, F0.5, completeness, latency, error rate
│   ├── llm_judge.py                # LLM-based quality scoring
│   ├── run_eval.py                 # Main eval runner
│   ├── judge_cache.json            # Pre-populated judge scores
│   └── results/leaderboard.json   # Pre-committed results (drives RESULTS.md)
└── data/ground_truth_generator.py  # Script used to generate GT files
```

## Setup

```bash
cp .env.example .env
# Fill in ENGINE_A_URL, ENGINE_B_URL, ENGINE_C_URL, BEARER_TOKEN
# (values provided separately — ANTHROPIC_API_KEY is only needed for make eval-fresh, see below)
pip install -r requirements.txt
```

## Running the eval

```bash
make eval
```

This calls the three Vercel engines live and scores against the pre-committed judge cache — no Anthropic API calls needed.

**Note:** The engines only respond to URLs in `data/seed_urls.json` and `data/prod_sample_urls.json`. Requests for other URLs return 404.

**Note:** `eval/results/leaderboard.json` and `eval/judge_cache.json` are pre-committed. `make eval` uses the cached judge scores. `make eval-fresh` re-runs the LLM judge live against all 1800 (engine, URL) pairs — this requires `ANTHROPIC_API_KEY` in `.env`, takes ~2 hours, and is **not required** for the session.

LLM-based judges are inherently noisy: individual scores can shift by ±1 point on re-runs, and aggregate means can vary by ±0.3–0.5 points between runs. Keep that in mind when interpreting the numbers in `RESULTS.md`.

## What to bring to the session

- Your read on the eval methodology
- Any issues you spotted with how the results were computed or presented
- A recommendation on whether to ship Engine C, and why
