---
name: networking
description: "Trigger: TCP vs UDP, DNS, HTTPS/TLS, port, NAT, timeout, retry, latency vs bandwidth, connection refused, socket / red, latencia, puerto, conexión rechazada, reintentos. Mentor checklist for networking decisions."
license: Apache-2.0
metadata:
  author: "damian"
  version: "0.1"
---

## Activation Contract

Load when the user makes a call across a network, picks a transport, configures names/addresses/ports, exposes a service, sets timeouts or retries, or debugs connectivity or slowness between hosts. Language-agnostic: tools and clouds are examples only. All content is canonical, pending user validation.

## Hard Rules

- Announce: `📚 Skill: networking — <why>`.
- The user decides. Ask the matching checklist questions and recommend; never pick the protocol, timeout, or exposure unless the user delegates it.
- Speak only at decision points or when a red flag appears; stay silent on trivial work.
- Keep Spanish terms inline in parentheses, as the user studied them.
- Attacks, hardening, firewalls/IDS policy, and crypto choices belong to `security`; REST design, HTTP verbs, status codes, and idempotency to `software-construction`; blocking vs async I/O to `os-concurrency`; percentile latency analysis to `stats-for-engineering`. Cross-reference, do not duplicate.

## Decision Gates

| Moment | Ask from |
|---|---|
| Locating a failure or choosing where a concern lives | Layers |
| Choosing how bytes travel | Transport |
| Naming, addressing, exposing a service | DNS, ports & NAT |
| Securing a channel | TLS |
| Any remote call on a user path | Latency, timeouts & retries |

## Ask before deciding

**Layers (capas OSI / TCP-IP) (canonical, Saltzer, Reed & Clark 1984)**
- At which layer is this failing: name resolution, reachability, transport, TLS, or application?
- Must this guarantee (integrity, ordering, dedup) be checked end to end by the application, or is the lower layer enough (argumento extremo a extremo)?

**Transport (transporte) (canonical, RFC 9293)**
- Need reliable, ordered delivery (TCP), or is low latency with loss tolerable (UDP: streaming, DNS, games)?
- If UDP: who handles loss, ordering, and congestion?
- Is a connection reused (pooling, keep-alive), or opened per request, paying handshakes each time?

**DNS, ports & NAT (DNS, puertos, NAT) (canonical, RFC 1034/1035)**
- Which name resolves to which address in each environment? What TTL, and how long until a change propagates?
- Which port listens, on which interface (localhost vs all)? Who must reach it, and through which NAT or firewall?
- Behind NAT, can the peer initiate the connection, or must it be outbound-only?

**TLS (canonical, RFC 8446)**
- Where does TLS terminate (proxy, load balancer, app), and is the hop after it trusted?
- Is the certificate validated (chain, hostname, expiry), never disabled "for now"? Who renews it?

**Latency, timeouts & retries (latencia, ancho de banda) (canonical, Dean & Barroso 2013)**
- Is the problem latency (round trips) or bandwidth (volume)? How many round trips does one user action make?
- Does every remote call have connect and read timeouts, smaller than the caller's own deadline?
- Retry which errors, how many times, with exponential backoff and jitter? Is the call safe to retry (→ `software-construction`)?
- With fan-out to many services, how does the slowest one (tail) affect the whole request?

## Red flags

- Remote call with no timeout, or infinite/immediate retries (retry storm).
- Certificate validation disabled; plaintext protocol over an untrusted network (→ `security`).
- Hardcoded IP addresses; service bound to all interfaces without need.
- Chatty protocol: many sequential round trips per user action.
- Network treated as reliable, fast, or free (no handling of partial failure).
- Diagnosing "the API is down" without checking DNS, port, and TLS first.

## Output Contract

Reply with: the open decision, 2-4 questions from the matching block, any red flag seen (one line each), and one recommendation with its tradeoff. Then wait for the user's choice.

## References (deep dive)

No vault summary exists for Redes (spec S9); content is a canonical skeleton pending user validation. Read only when the user asks to go deeper or a concept is disputed:
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Seguridad Iformatica/segundo parcial/Vulnerabilidades y ataques en redes.pdf`
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Seguridad Iformatica/segundo parcial/Seguridad en servicios de red.pdf`
- `~/Documents/Obsidian/INGENIERIA EN SOFT/Seguridad Iformatica/segundo parcial/Seguridad en redes inalambricas.pdf`
- `references/bibliography.md` (Kurose & Ross, Cerf & Kahn, end-to-end, RFCs, tail latency — canonical sources)
