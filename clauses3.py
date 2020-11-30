import sys
import re

####### CLAUSE2 + ADDITIONAL CLAUSE SET #######
# properties a, c, d, e & f

#### Read from QCP file ####
f = open(sys.argv[1],"r")
first = f.readline()
n = int(re.search(r'\d+', first).group()) # order n value

nclauses = 0
nvars = 0

### Create dictionary to map C_ijk to unique value ###
dict = {}
value = 1
for r in range(n):
    for c in range(n):
        for k in range(n):
            dict[r,c,k] = value
            value+=1

### fixed clause ###
fixedClause = [] 

for r in range(n):
    next = f.readline() # read line from input file
    lst = next.split(' ')
    for c in range(len(lst)):
        if (lst[c] != '.') and (lst[c] != '.\n')and (lst[c] != '\n'):
            k = int(lst[c])-1
            term = dict[r,c,k]
            fixedClause.append(term)
            nclauses+=1

f.close()

### property a: each cell of the square contains a number in [n] ###
clausesA = []
term = 0
for r in range(n):
    for c in range(n):
        for k in range(n):
            term = dict[r,c,k]
            clausesA.append(term)
        clausesA.append(0) #Indication to jump to newline
        nclauses+=1
#print(clausesA)

### property c: no row has 2 cells containing the same number ###
clausesC = []
term = 0
for r in range(n):
    for k in range(n):
        for c1 in range(n):
            for c2 in range(c1+1,n):
                term1 = dict[r,c1,k] # C_ij1k
                term2 = dict[r,c2,k] # # C_ij2k
                clausesC.append(term1)
                clausesC.append(term2)
                clausesC.append(0) # indicates end of clause
                nclauses+=1
#print(clausesC)

### property d: no column has 2 cells containing the same number ###
clausesD = []
term = 0
for c in range(n):
    for k in range(n):
        for r1 in range(n):
            for r2 in range(r1+1,n):
                term1 = dict[r1,c,k] # C_i1jk
                term2 = dict[r2,c,k] # C_i2jk
                clausesD.append(term1)
                clausesD.append(term2)
                clausesD.append(0) # end of clause
                nclauses+=1
#print(clausesD)

### property e: every number in [n] appears in every row ###
clausesE = []
term = 0
for r in range(n):
    for k in range(n):
        for c in range(n):
            term = dict[r,c,k]  #change in column
            clausesE.append(term)
        clausesE.append(0) # end of clause
        nclauses+=1
#print(clausesE)

### property f: every number in [n] appears in every column ###
clausesF = []
term = 0
for c in range(n):
    for k in range(n):
        for r in range(n):
            term = dict[r,c,k] #change in row
            #print(term)
            clausesF.append(term)
        clausesF.append(0) # end of clause
        nclauses+=1
#print(clausesF)


### Writing output to the .cnf file ###
nvars = (clausesD[-2])
with open(sys.argv[2], 'w') as f:
    print( "p cnf", nvars, nclauses, file = f) #first line
    for i in fixedClause: #fixed clauses
        print(i, 0, file = f)

    for i in clausesA: # set of clauses for property a
        print(i, end = " ", file = f)
        if i == 0:
            print("", file = f)
    
    for i in clausesC: # set of clauses for property c
        print(-i, end = " ", file = f)
        if i == 0:
            print("", file = f)
    
    for i in clausesD: # set of clauses for property d
        print(-i, end = " ", file = f)
        if i == 0:
            print("", file = f)

    for i in clausesE: # set of clauses for property e
        print(i, end = " ", file = f)
        if i == 0:
            print("", file = f)

    for i in clausesF: # set of clauses for property f
        print(i, end = " ", file = f)
        if i == 0:
            print("", file = f)








