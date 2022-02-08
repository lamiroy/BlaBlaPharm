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

couple=[]
pharma1=[["ph1","cand1"],["ph1","cand2"],["ph1","cand3"]]
pharma2=[["ph2","cand1"],["ph2","cand2"],["ph2","cand3"]]
pharma3=[["ph3","cand1"],["ph3","cand2"],["ph3","cand3"]]
pharma4=[["ph4","cand1"],["ph4","cand2"],["ph4","cand3"]]
pharma5=[["ph5","cand1"],["ph5","cand2"],["ph5","cand3"]]
couple.append(pharma1)
couple.append(pharma2)
couple.append(pharma3)
couple.append(pharma4)
couple.append(pharma5)



def tabScore(affectation,candidat):

    score=[]

    for ph in affectation:
        scorePh=[]
        for cand in candidat:
            scoreCandPh=0
            for i in range(len(ph)):
                if(ph[i] == cand[i] and cand[i] == 1):
                    scoreCandPh +=1
            scorePh.append(scoreCandPh)
        score.append(scorePh)

    #ici on a créé la matrice score avec pour chaque ligne=pharmacie et chaque colonne=score candidat=nbre créneau dispo mutuel


    return score

    meilleurChoix=[]

def maxProgLin(score,meilleurChoix):


    max=0
    indicei=0
    indicej=0

    for i in range(len(score)):
        for j in range(len(score[i])):
            if max < score[i][j]:
                max = score[i][j]
                indicei = i
                indicej = j


    meilleurChoix.append(couple[indicei][indicej])
    del score[indicei]
    del couple[indicei]
    for k in range(len(score)):
        del score[k][indicej]
        del couple[k][indicej]

    if score[0] != []:
        return maxProgLin(score,meilleurChoix)


    return meilleurChoix



print(tabScore(affectation,candidat))
print(maxProgLin(tabScore(affectation,candidat),[]))





