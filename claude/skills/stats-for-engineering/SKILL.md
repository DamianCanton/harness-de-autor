---
name: stats-for-engineering
description: "Trigger: benchmark comparison, A/B test, flaky test rate, p-value, confidence interval, sample size, p99 latency, Monte Carlo / estadística, comparar rendimiento, muestra, métricas. Mentor checklist for statistics."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user draws a conclusion from data: comparing two builds/benchmarks, reading an A/B test, judging a failure or flaky-test rate, sizing a sample, summarizing latency, building a metrics dashboard, fitting a trend, or simulating a system. Language-agnostic.

## Hard Rules

- Announce: `📚 Skill: stats-for-engineering — <why>`.
- The user decides. Ask the matching questions and recommend; never pick the test, threshold (alpha), or conclusion unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Test design and flaky-test handling belong to `se-testing-verification`; queue/concurrency mechanics to `os-concurrency`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Summarizing a metric | Describe first |
| Reporting an estimate from a sample | Estimation |
| "Is A better than B?" | Hypothesis test |
| Categories, 3+ groups, or a trend | Categorical, ANOVA, regression |
| Planning data collection | Sample size |
| Cannot measure, must model | Simulation |

## Ask before deciding

**Describe first (canonical)**
- Is it long-tailed? Then which percentile (p95/p99), not the mean, matters to the user?
- What does the dashboard aggregate hide (per-segment, per-time)?

**Estimation (estimación)**
- Is the sample random and representative, or just convenient?
- Is the estimator unbiased (insesgado) and low-variance? Do we report an interval (nivel de confianza, error muestral), not a lone number?
- Is the population finite and the sample at least 5% of it (corrección por población finita)?

**Hypothesis test (prueba de hipótesis)**
- What are H0 and H1 in plain words, and which one must the data contradict? Fixed alpha chosen before looking?
- Which is worse here: a false alarm (error tipo I) or a missed real effect (error tipo II)? What power (potencia) is affordable?
- Independent or paired samples (apareadas)? Equal variances or t de Welch? One- or two-sided, decided beforehand?
- Is the effect big enough to matter (significancia práctica vs estadística)? Does the interval agree?

**Categorical, ANOVA, regression**
- Chi-square (chi-cuadrado): goodness of fit or independence? Every expected frequency at least 5, else merge categories?
- Comparing 3+ groups: why not many pairwise tests (inflated error)? ANOVA plus post hoc (Tukey-Kramer); are normality and equal variances plausible?
- Regression (regresión): are linearity, constant variance (homocedasticidad), independent errors, and normal residuals checked in a residual plot?
- Correlation vs causation (causalidad)? What does R² explain; is extrapolating sane?

**Sample size (tamaño muestral)**
- What margin of error, confidence, and variance estimate (pilot, range/6)? For a proportion with no prior, plan for p = 0.5?
- What smallest difference must we detect, and what can we afford?

**Simulation (canonical)**
- Is a Monte Carlo (random sampling) enough, or is the system queue-like (arrivals, service, utilization) needing discrete-event simulation?
- How many replications and warm-up; are inputs validated against real measurements?

## Red flags

- Mean-only latency or success rate with no spread, percentile, or n.
- "Significant" claimed with no effect size, interval, or sample size.
- Accepting H0 because p > 0.05; or reading p as the probability H0 is true.
- Many comparisons or repeated peeking with no error correction (A/B stopped early).
- Rerunning a benchmark until it passes; one run per variant.
- Chi-square with expected counts below 5; ANOVA with clearly unequal variances.
- Trend extrapolated; correlation sold as cause; alpha or sidedness chosen after seeing p.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Estadistica II/P1/Resumen Estadistica II.md` (sampling, CLT, estimators, CI, tests, errors, one/two samples)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Estadistica II/P2/Resumen Estadistica II P2.md` (chi-square, ANOVA, regression, correlation, worked exercises)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Estadistica II/P1/fuentes-markdown/Qué significa realmente el valor p.md` (p-value misreadings)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Estadistica II/P1/fuentes-markdown/Error tipo I y II.md`, `Tests de hipótesis estadísticas.md`, `Distribución Chi Cuadrado χ2.md`, `publicacion.md` (estimator properties)
- `references/bibliography.md` (percentiles, power, experiments, simulation — canonical sources)
