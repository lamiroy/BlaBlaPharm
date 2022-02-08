ph1=[0,0,1,0,1,1,1,0,1,0,0,0,1,1]
ph2=[0,0,0,0,1,0,1,0,0,0,1,0,1,1]
ph3=[0,0,1,0,0,1,1,0,1,0,0,0,1,0]
ph4=[0,1,1,1,1,1,0,1,1,0,0,0,1,1]
ph5=[0,0,0,0,1,0,1,0,0,0,1,0,0,1]

Candidat1=[1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Candidat2=[1,0,1,0,1,0,1,0,1,0,1,0,1,0]
Candidat3=[0,0,1,1,0,0,1,1,0,0,1,1,0,0]

affectation=[]

affectation.append(ph1)
affectation.append(ph2)
affectation.append(ph3)
affectation.append(ph4)
affectation.append(ph5)

candidat=[]
candidat.append(Candidat1)
candidat.append(Candidat2)
candidat.append(Candidat3)

def maxProgLin(affectation,candidat):

    score=[]
    max=0

    for t in range(len(candidat)):
        for i in range(len(affectation)):
            for j in range(len(affectation[i])):
                if candidat[t][j] == affectation[i][j]:
                    print(score[t])
                    score[t] = score[t] +1

    for k in range(len(score)):
        if score[k] > max:
            max = score[k]

    return max

print(maxProgLin(affectation,candidat))





