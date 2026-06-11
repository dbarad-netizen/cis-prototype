# Creative Intelligence System (CIS) — Prototype

A working prototype of a neutral intelligence layer for marketing measurement. CIS connects to the
tools that already generate signals, normalizes their native metrics onto one common 0–100 scale across
five domains (Context, Attention, Creative, Behavioral, Business), and synthesizes them into a single
explainable recommendation: **Scale, Optimize, Test, or Stop**.

## What's here

- **`index.html`** — the full interactive prototype. A single self-contained file (no build step, no
  backend, no dependencies). Everything runs in the browser and no data leaves the page.
- **`cis_one_pager.pdf`** — the accompanying strategy brief.

## What the prototype demonstrates

- **Mock live connectors** — each domain is fed by a named source tool (Adelaide, Peer39, System1,
  GA4, Snowflake). Connect them and the picture assembles; unconnected sources show as blind spots.
- **Normalization layer** — click *inspect* on any connected source to see its raw API payload and the
  exact math that maps native metrics onto the 0–100 scale.
- **Calibration** — the normalization weights are editable; change one and watch scores and
  recommendations recompute live.
- **Synthesis engine** — treats the five domains as a funnel, finds the bottleneck, and produces an
  explainable recommendation with a confidence score.
- **Campaign portfolio** — every sample campaign scored at once, live against the current calibration
  and market context.

> Note: connectors and data are simulated for demonstration. Production would use live API integrations
> and calibration weights learned from outcome data.

## Deploying

This is a static site — no build configuration needed.

**Vercel:** Add New → Project → Import this repo. Vercel auto-detects it as static and serves
`index.html` at the root. Done.

**Anything else:** any static host (GitHub Pages, Netlify, Cloudflare Pages) works the same way —
just point it at this folder.

## Running locally

Open `index.html` in any browser. That's it.
