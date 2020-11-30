# A Quasigroup Completion Problem (QCP) to Conjunctive Normal Form (CNF) Converter
Three QCP to CNF converters are implemented, different from the subset of Latin Squares properties they encompass. 
These converters take in any .qcp file as input, generate a set of correct clauses — which are different for each 
converter — and output the respective .cnf file. The .cnf file is then used in the SAT Solver, ​Clasp​, to check whether 
the Latin squares completion problem is satisfiable or unsatisfiable.


### INSTRUCTIONS ON RUNNING MY IMPLEMENTATION OF THE QCP TO CNF CONVERTER
To obtain the cnf file, run one of the clauses python files:
- clauses1.py = the minimal subset of clauses (property a, c, & d)
- clauses2.py = clauses1.py + property e
- clauses3.py = clauses2.py + property f

```
 python3 clauses<#>.py A2-qcp-instances/<qcp file> outputs/<cnf file>
```

E.g. The following command runs clauses1 with input q_20_04.qcp and outputs the results to c1_q_20_04.cnf

```
 python3 clauses1.py A2-qcp-instances/q_20_04.qcp outputs/c1_q_20_04.cnf
```
---

### Installing the SAT Solver, Clasp. 
- To install on Linux: 
```
sudo apt-get update
sudo apt-get install -y clasp
```

- On MAC, you can install Clasp by:
```
brew install clasp
```
---

### To run the (pre-existing) output .cnf files on Clasp for satisfiability checking:
```
clasp outputs/<cnf file>
```

E.g. The following command executes c2_q_10_01.cnf to the SAT Solver:
```
clasp outputs/c2_q_10_01.cnf
```


** The .cnf files of order 24, 30 and 32 have been removed from the outputs folder because of their large file sizes **
** To generate them, simply run the clauses with their respective qcp files as input **
