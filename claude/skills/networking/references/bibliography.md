# Bibliography — networking

Canonical sources (no vault summary for Redes, spec S9).
Status: [verified] = citation checked online on 2026-11-19; [known] = standard citation, not re-checked online.

## Textbooks
- [verified] Kurose, J. F., & Ross, K. W. (2021). *Computer Networking: A Top-Down Approach* (8th ed.). Pearson (US edition published July 2020, © 2021; ISBN 978-0-13-668155-7).
- [known] Tanenbaum, A. S., Feamster, N., & Wetherall, D. J. (2021). *Computer Networks* (6th ed.). Pearson.

## Architecture of the Internet
- [verified] Cerf, V. G., & Kahn, R. E. (1974). A Protocol for Packet Network Intercommunication. *IEEE Transactions on Communications*, COM-22(5), 637–648. Origin of TCP/IP internetworking (gateways, end-to-end error checking, timeouts).
- [verified] Saltzer, J. H., Reed, D. P., & Clark, D. D. (1984). End-to-End Arguments in System Design. *ACM Transactions on Computer Systems*, 2(4), 277–288. Place functions at the endpoints; lower layers only as optimization.
- [known] Zimmermann, H. (1980). OSI Reference Model — The ISO Model of Architecture for Open Systems Interconnection. *IEEE Transactions on Communications*, 28(4), 425–432. (Standard: ISO/IEC 7498-1.)

## Protocol specifications
- [verified] Eddy, W. (Ed.). (2022). *Transmission Control Protocol (TCP)*. RFC 9293, STD 7. IETF. Obsoletes RFC 793.
- [verified] Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3*. RFC 8446. IETF. DOI 10.17487/RFC8446.
- [verified] Fielding, R., Nottingham, M., & Reschke, J. (Eds.). (2022). *HTTP Semantics*. RFC 9110, STD 97. IETF.
- [known] Mockapetris, P. (1987). *Domain Names — Concepts and Facilities* (RFC 1034) and *Implementation and Specification* (RFC 1035). IETF.
- [known] Postel, J. (1980). *User Datagram Protocol*. RFC 768. IETF.
- [known] Srisuresh, P., & Egevang, K. (2001). *Traditional IP Network Address Translator (Traditional NAT)*. RFC 3022. IETF.

## Latency, congestion, retries
- [verified] Dean, J., & Barroso, L. A. (2013). The Tail at Scale. *Communications of the ACM*, 56(2), 74–80. Tail latency dominates fan-out services; tail-tolerant techniques.
- [known] Jacobson, V. (1988). Congestion Avoidance and Control. *ACM SIGCOMM Computer Communication Review*, 18(4), 314–329. Retransmission timeouts and backoff.
