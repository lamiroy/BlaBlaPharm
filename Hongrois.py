import numpy as np



disponibiliteEmploy1=[[(8,10)],[],[],[],[],[(10,16)],[(3,4)]]
disponibiliteEmploy2=[[(8,12)],[(10,14)],[],[],[],[],[]]
disponibiliteEmploy3=[[],[],[],[],[],[],[]]
besoinBoss1=[[(8,10)],[],[(1,2)],[],[],[(8,17)],[]]
besoinBoss2=[[],[],[],[],[],[],[]]
besoinBoss3=[[],[],[],[],[],[],[]]
nbemploy=3
nbboss=3    

boss=[besoinBoss1,besoinBoss2,besoinBoss3,besoinBoss3,besoinBoss3]
employ=[disponibiliteEmploy1,disponibiliteEmploy2,disponibiliteEmploy3,disponibiliteEmploy3,disponibiliteEmploy3]



def dispo(besoin,dispo):
    heuretot=0
    for i in range(7):
        for couple in besoin[i]:
            a,b=couple
            for empcouple in dispo[i]:
                c,d=empcouple
                if min(d,b)>=max(a,c):
                    heuretot+=min(b,d)-max(a,c)
    return heuretot


def ligne(M):
    print("voici M "+str(M)+"\n")
    n=len(M)
    Z=[]
    nbzero=0
    zero=[[],[]]
    for i in range(n):
        li=[]
        for j in range(n):
            if M[i][j]==0:
                nbzero+=1
                a=1
                b=1
                for k in range(n):
                    if M[i][k]==0 and k!=j:
                        a+=1
                    if M[k][j]==0 and k!=i:
                        b+=1
                li.append((a,b))
            else:
                li.append((0,0))
        Z.append(li)
    while nbzero>0:
        print("Et Z "+ str(Z) + "\n" )
        #print(nbzero)
        maxl=1
        e=(0,0)
        maxc=1
        f=(0,0)
        k1=0
        k2=0
        for i in range(n):
            for j in range(n):
                if i not in zero[0] and j not in zero[1]:
                    c,d=Z[i][j]
                    if c!=0 and d!=0:
                        if c>maxl:
                            maxl=c
                            e=(i,j)
                            k1+=1
                        if d>maxc:
                            maxc=d
                            f=(i,j)
                            k2+=1
        aa,bb=e
        dd,ee=f
        if k1>=1:
            aa,bb=e
            zero[0].append(aa)
            nbzero-=(maxl-1)
        if k2>=1:
            zero[1].append(ee)
            nbzero-=(maxc-1)           
        if k1>0 and k2>0:
            if e==f:
                nbzero-=1
            else:
                nbzero-=2
        if k1>0 or k2>0 and not (k1>0 and k2>0):
            nbzero-=1
        for i in range(len(Z)):
            for j in range(len(Z[0])):
                if i==aa or j==ee:
                    Z[i][j]=(0,0)

        print(zero)
    print(zero)
    



def hongroisDispo(boss,employ):
    n=len(boss)
    M=np.zeros((n,n))
    #creation matrice
    for i in range(n):
        for j in range(n):
            M[i][j]=168-dispo(boss[i],employ[j])   #168 pour 7*24 pb de minimalisation au lieu de maximisation

    M=np.array([[6,5,6,3,2],[2,3,7,2,2],[3,5,4,3,4],[7,7,8,8,5],[6,7,7,5,3]])       
    #algo hongrois
    for i in range(n):
        min=168
        for k in M[i]:
            if k<min:
                min=k
        for j in range(n):
            M[i][j]-=min
    for i in range(n):
        min=168
        for k in M[:,i]:
            if k<min:
                min=k
        for j in range(n):
            M[j][i]-=min
    

    zero=[[],[]]
    for i in range(n):
        for j in range(n):
            if M[i][j]==0 and i not in zero[0] and j not in zero[1]:
                zero[0].append(i)
                zero[1].append(j)
    print(M)
    print(zero)
    s=0
    while not(len(zero[0])==n and len(zero[1])==n):
        minnonbarre=168
        #recupere min non barré
        for i in range(n):
            for j in range(n):
                if i not in zero[0] and j not in zero[1]:
                    if M[i][j]<minnonbarre:
                        minnonbarre=M[i][j]
        #sinon enlever le mininmumum non barré à toutes les lignes non barés                
        for i in range(n):
            if i not in zero[0]:
                for j in range(n):
                    M[i][j]-=minnonbarre
        #ajoute le min non barré à toute les colonnes barées
        for j in range(n):
            if j in zero[1]:
                for i in range(n):
                    M[i][j]+=minnonbarre

        zero=[[],[]]
        for i in range(n):
            for j in range(n):
                if M[i][j]==0 and i not in zero[0] and j not in zero[1]:
                    zero[0].append(i)
                    zero[1].append(j)
        if s<2:
            print(M)
            print(zero)
            s+=1
    
    
    for i in range(n):
        print("Le patron " + str(zero[0][i])+ " est affecté à l'employé "+str(zero[1][i]))

        

    


ligne([[4,2,3,1,0],[0,0,4,0,0],[0,1,0,0,1],[2,1,2,3,0],[3,3,3,2,0]])
#hongroisDispo(boss,employ)