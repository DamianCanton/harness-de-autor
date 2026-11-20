# Bibliography — software-construction

Canonical sources for content not covered by the vault (idempotency/statelessness, defensive programming, review, CI, refactoring).
Status: [verified] = citation checked online; [known] = standard citation, not re-checked online (no web search done for this skill).

## REST
- [known] Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral dissertation, University of California, Irvine. Ch. 5 "Representational State Transfer (REST)": client-server, stateless, cacheable, uniform interface, layered system.
- [known] Fielding, R., & Reschke, J. (2014). RFC 7231: HTTP/1.1 Semantics and Content. IETF. Defines safe and idempotent methods and status code semantics (successor: RFC 9110, 2022).

## Construction practice
- [known] McConnell, S. (2004). *Code Complete* (2nd ed.). Microsoft Press. Defensive programming (Ch. 8), naming (Ch. 11), collaborative construction/reviews (Ch. 21), refactoring (Ch. 24).
- [known] Fowler, M. (1999/2018). *Refactoring: Improving the Design of Existing Code* (2nd ed. 2018). Addison-Wesley. Behavior-preserving transformations under tests.
- [known] Fowler, M. (2006). Continuous Integration. martinfowler.com. Integrate frequently with an automated build.

## Component-based UI (vault-backed; cited by the vault)
- [known] React documentation (react.dev), "Thinking in React" and "Sharing State Between Components" — single source of truth, lifting state up.
