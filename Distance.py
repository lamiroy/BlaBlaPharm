from gurobipy import *
import pulp as pl
import numpy as np
import time

start = time.time()

u=0

m = Model()
m.params.NonConvex = 2

#exemple
c=np.array([[1,0,1],[0,1,1],[0,1,0],[0,0,1],[1,1,1]])
mo=np.array([0,1,1,0,0,1,1,1,0,1,1,1])

nbcrecan=0
for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j] == 1:
            nbcrecan+=1

nbcrepha=0
for i in range(len(mo)):
    if mo[i] == 1:
        nbcrepha+=1

nbcrefin=0

distancetotal=0

#taille du model
n=4
p=3
mint=5
mult=n*p

#distance
d_p1_p1=0   #RESTE A 0
d_p1_p2=100
d_p1_p3=100
d_p1_p4=100
d_p1_d1=10
d_p1_d2=100
d_p1_d3=100
d_p1_d4=100
d_p1_d5=100

d_p2_p2=0   #RESTE A 0
d_p2_p3=100
d_p2_p4=100
d_p2_d1=10
d_p2_d2=100
d_p2_d3=100
d_p2_d4=100
d_p2_d5=100

d_p3_p3=0   #RESTE A 0
d_p3_p4=100
d_p3_d1=10
d_p3_d2=100
d_p3_d3=100
d_p3_d4=100
d_p3_d5=100

d_p4_p4=0   #RESTE A 0
d_p4_d1=10
d_p4_d2=100
d_p4_d3=100
d_p4_d4=100
d_p4_d5=100


distance=np.array([
[d_p1_p1,d_p1_p2,d_p1_p3,d_p1_p4,d_p1_d1,d_p1_d2,d_p1_d3,d_p1_d4,d_p1_d5],
[d_p1_p2,d_p2_p2,d_p2_p3,d_p2_p4,d_p2_d1,d_p2_d2,d_p2_d3,d_p2_d4,d_p2_d5],
[d_p1_p3,d_p2_p3,d_p3_p3,d_p3_p4,d_p3_d1,d_p3_d2,d_p3_d3,d_p3_d4,d_p3_d5],
[d_p1_p4,d_p2_p4,d_p3_p4,d_p4_p4,d_p4_d1,d_p4_d2,d_p4_d3,d_p4_d4,d_p4_d5],
[d_p1_d1,d_p2_d1,d_p3_d1,d_p4_d1,0,0,0,0,0],
[d_p1_d2,d_p2_d2,d_p3_d2,d_p4_d2,0,0,0,0,0],
[d_p1_d3,d_p2_d3,d_p3_d3,d_p4_d3,0,0,0,0,0],
[d_p1_d4,d_p2_d4,d_p3_d4,d_p4_d4,0,0,0,0,0],
[d_p1_d5,d_p2_d5,d_p3_d5,d_p4_d5,0,0,0,0,0]])

#definition des variables
x=np.zeros((mint,n*p),Var)
for i in range(1,mint+1):
    for j in range(1,mult+1):
        nom="x"+str(i)+"_"+str(j)
        x[i-1][j-1]=m.addVar(name=nom)

#expression problème de base
sommeProb=0

for i in range (0,n):
    for j in range (0,mint):
        for k in range (0,p):
            sommeProb+= 100*x[j][i*p+k]*mo[i*p+k]

#expression problème de distance
for i in range(mint):
    for j in range(n):
        sommeProb-=x[i][j*p]*distance[j][n+i]  #k=0

    for k in range(1,p):
        for j in range(n):
            for l in range(n):
                sommeProb-=x[i][j*p+(k-1)]*x[i][l*p+k]*(distance[j][l]-distance[l][n+i]) #cas ou 2 creneau se suivent

    for k in range(1,p):
        for l in range(n):
            sommeProb-=x[i][l*p+k]*distance[l][n+i] # cas ou le pharmacien n'a pas de creneau juste avant


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


#calcul solution
m.optimize()

#mise en forme matricielle de la solution
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

#affichage de la solution
for i in range(len(resul)):
    for j in range(len(resul[i])):
        if resul[i][j] == 1:
            nbcrefin+=1
            #distancetotal+=distance[i][j]



#for v in m.getVars():
#    print(v.varName, v.x)
end = time.time()
print(resul)
print(" ")
print("la solution a été trouvée en :")
print(end-start)
print(" ")
print("Parmi les pharmaciens:")
print((nbcrefin/nbcrecan)*100)
print("% des creneaux ont été attribués")
print(" ")
print("Parmi les pharmacies:")
print((nbcrefin/nbcrepha)*100)
print("% des creneaux ont été attribués")
print(" ")
print("Distance total parcourue:")
print(distancetotal)
print("mètres")
