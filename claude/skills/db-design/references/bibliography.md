# Bibliography — db-design

Canonical sources for content not covered by the vault ("Base de Datos II": transactions, isolation, concurrency, indexing, query plans, denormalization).
Status: [verified] = citation checked online; [known] = standard citation, not re-checked online.

## Relational model and normalization
- [known] Codd, E. F. (1970). A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*, 13(6), 377–387.
- [known] Codd, E. F. (1972). Further Normalization of the Data Base Relational Model. In *Data Base Systems*, Courant Computer Science Symposia 6, Prentice-Hall, 33–64.
- [known] Chen, P. P. (1976). The Entity-Relationship Model: Toward a Unified View of Data. *ACM TODS*, 1(1), 9–36.

## Transactions, ACID, recovery
- [known] Gray, J., & Reuter, A. (1993). *Transaction Processing: Concepts and Techniques*. Morgan Kaufmann.
- [known] Haerder, T., & Reuter, A. (1983). Principles of Transaction-Oriented Database Recovery. *ACM Computing Surveys*, 15(4), 287–317. Origin of the ACID acronym.

## Isolation levels and anomalies
- [known] Berenson, H., Bernstein, P., Gray, J., Melton, J., O'Neil, E., & O'Neil, P. (1995). A Critique of ANSI SQL Isolation Levels. *SIGMOD '95*, 1–10. Dirty/non-repeatable/phantom reads, lost update, snapshot isolation.

## Concurrency control
- [known] Bernstein, P. A., Hadzilacos, V., & Goodman, N. (1987). *Concurrency Control and Recovery in Database Systems*. Addison-Wesley. Serializability, two-phase locking, deadlock, timestamp/optimistic methods.
- [known] Kung, H. T., & Robinson, J. T. (1981). On Optimistic Methods for Concurrency Control. *ACM TODS*, 6(2), 213–226.

## Indexing and query plans
- [known] Bayer, R., & McCreight, E. (1972). Organization and Maintenance of Large Ordered Indexes. *Acta Informatica*, 1(3), 173–189. B-trees.
- [known] Selinger, P. G., et al. (1979). Access Path Selection in a Relational Database Management System. *SIGMOD '79*, 23–34. Cost-based optimizer and plan choice.

## General textbooks
- [known] Silberschatz, A., Korth, H. F., & Sudarshan, S. *Database System Concepts* (7th ed., McGraw-Hill, 2019). The vault's ERD and relational-model readings follow this vocabulary (not re-checked).
- [known] Garcia-Molina, H., Ullman, J. D., & Widom, J. *Database Systems: The Complete Book* (2nd ed., Pearson, 2008).
