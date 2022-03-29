from gurobipy import *
import pulp as pl
import numpy as np

u=0

m = Model()

c=np.array([[1,0,1],[0,1,1],[0,1,0],[0,0,1],[1,1,1]])

mo=np.array([0,1,1,0,0,1,1,1,0,1,1,1])



n=4
p=3
mint=5

#variables
x11 = m.addVar(name="x11")
x12 = m.addVar(name="x12")
x13 = m.addVar(name="x13")
x14 = m.addVar(name="x14")
x15 = m.addVar(name="x15")
x16 = m.addVar(name="x16")
x17 = m.addVar(name="x17")
x18 = m.addVar(name="x18")
x19 = m.addVar(name="x19")
x110 = m.addVar(name="x110")
x111 = m.addVar(name="x111")
x112 = m.addVar(name="x112")
x21 = m.addVar(name="x21")
x22 = m.addVar(name="x22")
x23 = m.addVar(name="x23")
x24 = m.addVar(name="x24")
x25 = m.addVar(name="x25")
x26 = m.addVar(name="x26")
x27 = m.addVar(name="x27")
x28 = m.addVar(name="x28")
x29 = m.addVar(name="x29")
x210 = m.addVar(name="x210")
x211 = m.addVar(name="x211")
x212 = m.addVar(name="x212")
x31 = m.addVar(name="x31")
x32 = m.addVar(name="x32")
x33 = m.addVar(name="x33")
x34 = m.addVar(name="x34")
x35 = m.addVar(name="x35")
x36 = m.addVar(name="x36")
x37 = m.addVar(name="x37")
x38 = m.addVar(name="x38")
x39 = m.addVar(name="x39")
x310 = m.addVar(name="x310")
x311 = m.addVar(name="x311")
x312 = m.addVar(name="x312")
x41 = m.addVar(name="x41")
x42 = m.addVar(name="x42")
x43 = m.addVar(name="x43")
x44 = m.addVar(name="x44")
x45 = m.addVar(name="x45")
x46 = m.addVar(name="x46")
x47 = m.addVar(name="x47")
x48 = m.addVar(name="x48")
x49 = m.addVar(name="x49")
x410 = m.addVar(name="x410")
x411 = m.addVar(name="x411")
x412 = m.addVar(name="x412")
x51 = m.addVar(name="x51")
x52 = m.addVar(name="x52")
x53 = m.addVar(name="x53")
x54 = m.addVar(name="x54")
x55 = m.addVar(name="x55")
x56 = m.addVar(name="x56")
x57 = m.addVar(name="x57")
x58 = m.addVar(name="x58")
x59 = m.addVar(name="x59")
x510 = m.addVar(name="x510")
x511 = m.addVar(name="x511")
x512 = m.addVar(name="x512")


#for i in range (0,n*p):
#    mo[i] = m.addVar(name="mo"+str(i))

#for j in range (0,mint):
#    for k in range (0,p):
#        print("c"+str(j)+str(k))
#        c[j,k] = m.addVar(name="c"+str(j)+str(k))


x=np.array([[x11,x12,x13,x14,x15,x16,x17,x18,x19,x110,x111,x112],[x21,x22,x23,x24,x25,x26,x27,x28,x29,x210,x211,x212],[x31,x32,x33,x34,x35,x36,x37,x38,x39,x310,x311,x312],[x41,x42,x43,x44,x45,x46,x47,x48,x49,x410,x411,x412],[x51,x52,x53,x54,x55,x56,x57,x58,x59,x510,x511,x512]])

#expression problème
sommeProb=0

for i in range (0,n):
    for j in range (0,mint):
        for k in range (0,p):
#            print(x[j][i*p+k])
#            print(mo[i*p+k])
            sommeProb+= x[j][i*p+k]*mo[i*p+k]

print(sommeProb)
m.setObjective(sommeProb , GRB.MAXIMIZE)

#premiere contrainte
sommePremContr=0

for k in range (0,p):
    for i in range (0,n):
        for p in range (0,n):
            for j in range (0,mint):
                sommePremContr+=x[j][i*p+k]
            m.addConstr(sommePremContr <= mo[i*p+k], "c"+str(u))
            u=u+1
            sommePremContr = 0

#deuxième contrainte
sommeDeuxContrX=0
sommeDeuxContrMO=0

for j in range (0,mint):
    for i in range(0,n):
        for k in range (0,p):
            sommeDeuxContrX+=x[j][i*p+k]
            sommeDeuxContrMO+=mo[i*p+k]
    m.addConstr(sommeDeuxContrX <= sommeDeuxContrMO, "c"+str(u))
    u=u+1
    sommeDeuxContrX=0
    sommeDeuxContrMO=0

#cinquième contrainte
sommeCinqContrX=0

for k in range (0,p):
    for j in range (0,mint):
        for i in range (0,n):
            sommeCinqContrX+=x[j][i*p+k]
        m.addConstr(sommeCinqContrX <= c[j][k], "c"+str(u))
        u=u+1
        sommeCinqContrX = 0

m.optimize()

resul=np.zeros((mint,n*p))
k=0
ii=0
jj=0
for v in m.getVars():
    resul[ii][jj]=v.x
    k+=1
    jj+=1
    if k>=n*p:
        k=0
        ii+=1
        jj=0

#for v in m.getVars():
#    print(v.varName, v.x)

print(resul)


##quatrième contrainte
sommeQuatrContrX=0
sommeQuatrContrC=0

for j in range (0,mint):
    for i in range (0,n):
        for k in range (0,p):
            sommeQuatrContrX=x[j][i*p+k]
            sommeQuatrContrC=c[j][k]
    m.addConstr(sommeQuatrContrX <= sommeQuatrContrC, "c"+str(u))
    u=u+1
    sommeQuatrContrX=0
    sommeQuatrContrC=0
##


##troisième contrainte
sommeTroisContrX=0
sommeTroisContrMO=0

for i in range (0,n):
    for j in range (0,mint):
        for k in range (0,p):
            sommeTroisContrX+=x[j][i*p+k]
            sommeTroisContrMO+=mo[i*p+k]
    m.addConstr(sommeTroisContrX <= sommeTroisContrMO, "c"+str(u))
    u=u+1
    sommeTroisContrX=0
    sommeTroisContrMO=0
##


