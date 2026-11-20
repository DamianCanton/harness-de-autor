# Bibliography — software-architecture

Canonical sources (architecture is not a course subject, spec S9), except component/deployment views, which come from the vault note `Taller de Analisis y diseño de Software/P2/Resumen_Taller_Diseño_P2.md` §5.
Status: [verified] = citation checked online on 2026-11-19; [known] = standard citation, not re-checked online.

## Foundations
- [verified] Perry, D. E., & Wolf, A. L. (1992). Foundations for the Study of Software Architecture. *ACM SIGSOFT Software Engineering Notes*, 17(4), 40–52. DOI 10.1145/141874.141884. Architecture = elements, form, rationale.
- [verified] Garlan, D., & Shaw, M. (1993). An Introduction to Software Architecture. In V. Ambriola & G. Tortora (Eds.), *Advances in Software Engineering and Knowledge Engineering* (Vol. 1, pp. 1–39). World Scientific. Also CMU-CS-94-166 (1994). Catalogue of styles: pipes and filters, layered, event-based, repositories.
- [verified] Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley. ISBN 978-0-13-688609-9. Quality attribute scenarios and tactics.

## Views and documentation
- [verified] Kruchten, P. (1995). Architectural Blueprints — The "4+1" View Model of Software Architecture. *IEEE Software*, 12(6), 42–50. DOI 10.1109/52.469759. Logical, development, process, physical views + scenarios.
- [verified] Nygard, M. (2011, November 15). Documenting Architecture Decisions. Cognitect blog. Origin of Architecture Decision Records (title, context, decision, status, consequences — section names taken from secondary sources).

## Quality model
- [verified] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (2nd ed., November 2023). Nine product quality characteristics.
- [known] The nine 2023 characteristic names: functional suitability, performance efficiency, compatibility, interaction capability (was usability), reliability, security, maintainability, flexibility (was portability), safety (new). Names not checked against the standard text — validate.

## Styles
- [verified] Cockburn, A. (2005). Hexagonal Architecture (Ports and Adapters). alistair.cockburn.us/hexagonal-architecture/. Application drivable by users, programs, tests, or scripts, isolated from devices and databases.
- [verified] Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall. ISBN 978-0-13-449416-6. The Dependency Rule: source dependencies point inward.
- [known] Martin, R. C. (2011, September 30). Screaming Architecture. blog.cleancoder.com. Top-level structure should reveal the use cases, not the framework.
- [verified] Lewis, J., & Fowler, M. (2014, March 25). Microservices. martinfowler.com/articles/microservices.html. Characteristics, not a formal definition.
- [known] Fowler, M. (2015). MonolithFirst. martinfowler.com/bliki/MonolithFirst.html.
- [verified] Conway, M. E. (1968). How Do Committees Invent? *Datamation*, 14(4), 28–31. System structure mirrors the communication structure of the organization (Conway's law).
