# Bibliography — stats-for-engineering

Canonical sources for content not covered by the vault (descriptive statistics for latency, experiment practice, simulation).
Status: [verified] = citation checked online; [known] = standard citation, not re-checked online (no web search was done for this skill, so every entry is [known]).

## Descriptive statistics and tail latency ("Estadística I", canonical)
- [known] Montgomery, D. C., & Runger, G. C. *Applied Statistics and Probability for Engineers* (Wiley; use current edition). Distributions, percentiles, histograms, engineering framing.
- [known] Dean, J., & Barroso, L. A. (2013). The Tail at Scale. *Communications of the ACM*, 56(2), 74–80. Why tail percentiles (p99) drive user-visible latency, not the mean.
- [known] Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21. Identical summary statistics, different data: plot before concluding.

## Hypothesis testing and p-values
- [known] Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, 70(2), 129–133. Six principles on what p does and does not mean.
- [known] Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum. Power, effect size, sample size.
- [known] Benjamini, Y., & Hochberg, Y. (1995). Controlling the False Discovery Rate. *Journal of the Royal Statistical Society B*, 57(1), 289–300. Multiple-comparison control.
- Vault source: Molina Arias, M. (2017). ¿Qué significa realmente el valor de p? *Rev Pediatr Aten Primaria*, 19, 377–381 (read in the vault PDF).

## Experiments and flaky tests
- [known] Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*. Cambridge University Press. Peeking, sample ratio mismatch, practical significance.
- [known] Luo, Q., Hariri, F., Eloussi, L., & Marinov, D. (2014). An Empirical Analysis of Flaky Tests. *FSE 2014*, 643–653. Causes and prevalence of flaky tests.

## Simulation ("Modelos de Simulación", canonical)
- [known] Law, A. M. *Simulation Modeling and Analysis* (McGraw-Hill; use current edition). Discrete-event simulation, replications, warm-up, validation.
- [known] Metropolis, N., & Ulam, S. (1949). The Monte Carlo Method. *Journal of the American Statistical Association*, 44(247), 335–341. Origin of Monte Carlo.
- [known] Little, J. D. C. (1961). A Proof for the Queuing Formula: L = λW. *Operations Research*, 9(3), 383–387. Basic queueing relation between load, throughput, and latency.
