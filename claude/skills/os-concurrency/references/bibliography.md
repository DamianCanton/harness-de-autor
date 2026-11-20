# Bibliography — os-concurrency

Canonical sources for content not covered by the vault (hardware cost model, concurrency practice).
Status: [verified] = citation checked online; [known] = standard citation, not re-checked online (no web search was run for this skill).

## Course textbooks (behind the vault summaries)
- [known] Stallings, W. (2005). *Sistemas Operativos* (5th ed.). Pearson. Ch. 4 threads, Ch. 5 concurrency, Ch. 9 scheduling.
- [known] Tanenbaum, A. S. (2014). *Modern Operating Systems* (4th ed.). Pearson. Ch. 2 processes/threads, Ch. 3 memory, Ch. 6 deadlocks, Ch. 8 multiprocessors.
- [known] Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.

## Computer architecture (canonical block: memory hierarchy, caches, latency, CPU vs I/O bound)
- [known] Hennessy, J. L., & Patterson, D. A. (2019). *Computer Architecture: A Quantitative Approach* (6th ed.). Morgan Kaufmann. Memory hierarchy, locality, cache coherence.
- [known] Drepper, U. (2007). What Every Programmer Should Know About Memory. Red Hat. Cache lines, false sharing, NUMA effects.
- [known] Dean, J. "Latency Numbers Every Programmer Should Know" (popularized list, e.g. Norvig, P., Teach Yourself Programming in Ten Years). Orders-of-magnitude latency by tier.
- [known] Amdahl, G. M. (1967). Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities. *AFIPS Spring Joint Computer Conference*, 483–485. Limit of parallel speedup.

## Concurrency and deadlock
- [known] Dijkstra, E. W. (1965). Cooperating Sequential Processes (EWD123). Semaphores, mutual exclusion; banker's algorithm appears in Dijkstra's EWD series.
- [known] Coffman, E. G., Elphick, M., & Shoshani, A. (1971). System Deadlocks. *ACM Computing Surveys*, 3(2), 67–78. The four necessary conditions.
- [known] Herlihy, M., & Shavit, N. (2008). *The Art of Multiprocessor Programming*. Morgan Kaufmann. Locks, atomics, memory models.
- [known] Lee, E. A. (2006). The Problem with Threads. *IEEE Computer*, 39(5), 33–42. Why shared-state threads are hard to reason about.

## Distributed systems
- [known] Lamport, L. (1978). Time, Clocks, and the Ordering of Events in a Distributed System. *Communications of the ACM*, 21(7), 558–565.
- [known] Birrell, A. D., & Nelson, B. J. (1984). Implementing Remote Procedure Calls. *ACM TOCS*, 2(1), 39–59.

## Modern concepts (cited in the vault summary)
- [known] Lipp, M. et al. (2018). Meltdown: Reading Kernel Memory from User Space. *USENIX Security*.
- [known] Kocher, P. et al. (2019). Spectre Attacks: Exploiting Speculative Execution. *IEEE S&P*.
