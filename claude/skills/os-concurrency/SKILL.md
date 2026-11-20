---
name: os-concurrency
description: "Trigger: race condition, deadlock, lock, thread vs process, async vs threads, blocking I/O, memory leak, performance bottleneck / concurrencia, condición de carrera, lento, memoria. Mentor checklist for OS and concurrency."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user shares mutable state across threads/processes/requests, picks a concurrency model, locks, hits a hang or slowdown, does file or network I/O, sets resource limits, or chooses containers/VMs. Language-agnostic: never tie a concept to one runtime.

## Hard Rules

- Announce: `📚 Skill: os-concurrency — <why>`.
- The user decides. Ask the matching questions and recommend; never pick the model, lock strategy, or limit unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Security, data design, networking, and architecture belong to `security`, `db-design`, `networking`, `software-architecture`; cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| State shared between threads/requests | Shared state |
| Adding a lock / waiting on a resource | Locking & deadlock |
| Choosing threads, processes, or async | Concurrency model |
| Slow, hung, or out of memory | Performance & memory |
| Reading/writing files, durability | File I/O |
| Containers, VMs, multi-node | Isolation & distribution |

## Ask before deciding

**Shared state (condición de carrera)**
- Who else can touch this data at the same time? Does the result depend on interleaving (read-modify-write)?
- What exactly is the critical section (sección crítica), and is it as small as possible?

**Locking & deadlock (exclusión mutua, interbloqueo)**
- Is a plain mutex enough, or is this ordering (condition variable), N-at-a-time (semaphore), or many-readers/one-writer?
- Do locks nest? Is there one global acquisition order? Can a holder wait for something slow (I/O, network) while locked?
- Which Coffman condition can I remove: mutual exclusion, hold-and-wait, no preemption, circular wait (espera circular)? Is there a timeout?

**Concurrency model (hilos, procesos)**
- CPU-bound or I/O-bound? (Parallelism helps the first; waiting-without-blocking helps the second.)
- Need shared memory (threads) or isolation and fault containment (processes)? What does a context switch cost here?
- Does any call block the thread or event loop (syscall, sync I/O)? Is thread/pool size bounded?

**Performance & memory (memoria virtual)**
- Is the working set larger than RAM? Any sign of swapping or thrashing?
- Is the time in CPU, memory, disk, or waiting? Measured or guessed?
- Which resource limit applies (memory, file descriptors, threads, CPU quota) and what happens at the limit?

**File I/O (sistema de archivos)**
- Must the write survive a crash? Is it flushed/synced, or only in the OS cache?
- Is a partial write possible? Write to temp then atomic rename?
- Are descriptors always closed, including on error paths?

**Isolation & distribution (virtualización, contenedores)**
- VM (own kernel, strong isolation) or container (shared kernel, namespaces + cgroups)? Which isolation is actually required?
- Multi-node: loosely coupled means no shared memory or clock; which failures (message loss, partial failure) must be handled?
- Remote call: blocking or async, reliable or not, idempotent on retry?

**Hardware cost model (canonical, Hennessy & Patterson)**
- Which tier is this data in (cache, RAM, SSD, network)? Latency differs by orders of magnitude.
- Does shared data written by several cores cause cache-line contention (false sharing)? Is access sequential (locality)?

## Red flags

- Shared mutable state with no lock, atomic, or owner; check-then-act without atomicity.
- Holding a lock across I/O or a callback; locks taken in different orders.
- Sleep/polling used instead of a condition or event; unbounded threads or queues.
- Blocking call inside an async handler or event loop.
- Write assumed durable without flush; handle or lock never released; unmeasured optimization; container without limits.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Sistemas Operativos/Parcial 1/Resumen - Sistemas Operativos.md` (hardware, processes, threads, concurrency, scheduling, deadlocks, NUMA/MESI, Android file systems, containers)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Sistemas Operativos/Parcial 2/Resumen 2 sistemas operativos.md` (memory management, virtual memory policies, file systems FAT/NTFS/ext, distributed, security)
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Sistemas Operativos/Parcial 2/fuentes-markdown/` (converted readings: Módulo 3 Lecturas 1-4, Módulo 4 Lecturas 1-4)
- `references/bibliography.md` (canonical sources)
