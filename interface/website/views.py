from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask_login import login_required, current_user
from .models import Note
import random
import numpy as np
import sqlite3
from gurobipy import *
import pulp as pl
import time
from geopy import distance
from geopy.geocoders import Nominatim

views = Blueprint('views', __name__)

liste_vocabulaire = []
longueur_initiale = []
score = [0]

DATABASE = '//home/kali/Documents/BlaBlaPharm/interface/website//database.db' # le nom du fichier de votre base sqlite3

def get_db(): # cette fonction permet de créer une connexion à la base ou de récupérer la connexion existante
 db = getattr(g, '_database', None)
 if db is None:
  db = g._database = sqlite3.connect(DATABASE)
 return db

def query_db(query, args=(), one=False):
    conn = get_db()
    cur=conn.cursor()
    cur.execute(query,args)
    conn.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@views.teardown_request
def close_connection(exception):
    db=getattr(g, '_database', None)
    if db is not None:
        db.close()

@views.route('/')
def home():
    i = len(liste_vocabulaire)
    while i > 0 :
        liste_vocabulaire.pop()
        i-=1
    score[0]=0
    if(len(longueur_initiale)!=0):
        longueur_initiale.pop()
    return render_template("home.html", user=current_user)

@views.route('/ajoutcand', methods=['GET','POST'])
def ajoutcand():
    if request.method=='POST':
        nom = request.form.get('name')
        prenom = request.form.get('prenom')
        adresse = request.form.get('adress')
        telephone = request.form.get('telephone')
        competence = request.form.get('competence')
        check1 = request.form.get('flexCheckDefault1')
        check2 = request.form.get('flexCheckDefault2')
        check3 = request.form.get('flexCheckDefault3')
        check4 = request.form.get('flexCheckDefault4')
        check5 = request.form.get('flexCheckDefault5')
        check6 = request.form.get('flexCheckDefault6')
        check7 = request.form.get('flexCheckDefault7')
        check8 = request.form.get('flexCheckDefault8')
        check9 = request.form.get('flexCheckDefault9')
        check10 = request.form.get('flexCheckDefault10')
        check11 = request.form.get('flexCheckDefault11')
        check12 = request.form.get('flexCheckDefault12')
        check13 = request.form.get('flexCheckDefault13')
        check14 = request.form.get('flexCheckDefault14')
        check15 = request.form.get('flexCheckDefault15')
        check16 = request.form.get('flexCheckDefault16')
        check17 = request.form.get('flexCheckDefault17')
        check18 = request.form.get('flexCheckDefault18')
        check19 = request.form.get('flexCheckDefault19')
        check20 = request.form.get('flexCheckDefault20')
        
        query = "INSERT INTO Candidats (Nom,Prenom,Addresse,Telephone,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences) VALUES ("+nom+','+prenom+','+adresse+','+str(check1)+','+str(check2)+','+str(check3)+','+str(check4)+','+str(check5)+','+str(check6)+','+str(check7)+','+str(check8)+','+str(check9)+','+str(check10)+','+str(check11)+','+str(check12)+','+str(check13)+','+str(check14)+','+str(check15)+','+str(check16)+','+str(check17)+','+str(check18)+','+str(check19)+','+str(check20)+','+"NULL"+','+"NULL)"
        query2 = "INSERT INTO Candidats (Nom,Prenom,Addresse,Telephone,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        #query_db(query2,(nom,prenom,adresse,"NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL"))
        query_db(query2,(nom,prenom,adresse,telephone,str(check1),str(check2),str(check3),str(check4),str(check5),str(check6),str(check7),str(check8),str(check9),str(check10),str(check11),str(check12),str(check13),str(check14),str(check15),str(check16),str(check17),str(check18),str(check19),str(check20),competence))
        
    return render_template("ajoutcand.html")

@views.route('/ajoutpharma', methods=['GET','POST'])
def ajoutpharma():
    print("bite")
    if request.method=='POST':
        nom = request.form.get('name')
        adresse = request.form.get('adress')
        competence = request.form.get('compet')
        description = request.form.get('descrip')
        check1 = request.form.get('flexCheckDefault1')
        check2 = request.form.get('flexCheckDefault2')
        check3 = request.form.get('flexCheckDefault3')
        check4 = request.form.get('flexCheckDefault4')
        check5 = request.form.get('flexCheckDefault5')
        check6 = request.form.get('flexCheckDefault6')
        check7 = request.form.get('flexCheckDefault7')
        check8 = request.form.get('flexCheckDefault8')
        check9 = request.form.get('flexCheckDefault9')
        check10 = request.form.get('flexCheckDefault10')
        check11 = request.form.get('flexCheckDefault11')
        check12 = request.form.get('flexCheckDefault12')
        check13 = request.form.get('flexCheckDefault13')
        check14 = request.form.get('flexCheckDefault14')
        check15 = request.form.get('flexCheckDefault15')
        check16 = request.form.get('flexCheckDefault16')
        check17 = request.form.get('flexCheckDefault17')
        check18 = request.form.get('flexCheckDefault18')
        check19 = request.form.get('flexCheckDefault19')
        check20 = request.form.get('flexCheckDefault20')
        print("bite1")
        
        query3 = "INSERT INTO Pharmacies (Nom,Addresse,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences,Description_poste) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        print("bite2")
        query_db(query3,(nom,adresse,str(check1),str(check2),str(check3),str(check4),str(check5),str(check6),str(check7),str(check8),str(check9),str(check10),str(check11),str(check12),str(check13),str(check14),str(check15),str(check16),str(check17),str(check18),str(check19),str(check20),competence,description))
        print("bite3")

    return render_template("ajoutpharma.html")

@views.route('/visualisation')
def visualisation():
    cc = query_db('select * from Candidats')
    for i in range(len(cc)):
        cc[i]=list(cc[i])
    dd = query_db('select * from Pharmacies')
    for i in range(len(dd)):
        dd[i]=list(dd[i])
    return render_template("visualisation.html" ,elem=cc ,element=dd)

@views.route('/algo',methods=['GET','POST'])
def algo():
    if request.method=='POST':
        c = query_db('select Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h from Candidats ')
        for i in range(len(c)):
            c[i]=list(c[i])
        ddd = query_db('select Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h from Pharmacies')
        for i in range(len(ddd)):
            ddd[i]=list(ddd[i])
        print("ddd")
        print(ddd)
        nbpharmacie=len(ddd)
        mo=[]
        for elem in ddd:
            for e in elem:
                mo.append(e)
        

        adrcand = query_db('select addresse from Candidats')
        for i in range(len(adrcand)):
            adrcand[i]=adrcand[i][0]
        adrpharma = query_db('select addresse from Pharmacies')
        for i in range(len(adrpharma)):
            adrpharma[i]=adrpharma[i][0]
        print("ici cest la liste des addresses candidats")
        print(adrcand)
        print("ici cest la liste des addresses pharmacie")
        print(adrpharma)
        print("distance vv pablo")
        #print(type(adrcand[0]))
        #print("location")
        #print(location.latitude)
        #print(location.longitude)
        #print(geodesic(string(adrcand[0]),string(adrpharma[0])).km)  
        print(c)
        print("belo bito")
        print(mo)
        nbcandidat=len(c)
        start = time.time()

        u=0

        m = Model()
        m.params.NonConvex = 2

        #exemple
        #c=np.array([[1,0,1],[0,1,1],[0,1,0],[0,0,1],[1,1,1]])
        #mo=np.array([0,1,1,0,0,1,1,1,0,1,1,1])

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
        #n=4
        n=nbpharmacie
        p=4*5
        #mint=5
        mint=nbcandidat
        mult=n*p

        #distance
        '''
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
        d_p4_d3=1000
        d_p4_d4=100
        d_p4_d5=100
        '''
        #location = geolocator.geocode(adrcand[0])
        #location2 = geolocator.geocode(adrpharma[0])
        #print("important")
        #print(distance.distance((location.latitude,location.longitude), (location.latitude,location.longitude)).m)
        '''
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
        '''
        distance2=np.zeros((nbpharmacie+nbcandidat,nbpharmacie+nbcandidat))
        print("nbpharma")
        print(nbpharmacie)
        print(len(adrpharma))
        print(nbcandidat)
        #print(len(adrcand))
        print(distance2[0])
        geolocator = Nominatim(user_agent="Geolocator2")
        for i in range(len(distance2)):
            for j in range(len(distance2[0])):
                if (i<nbpharmacie) and (j<nbpharmacie):
                    location = geolocator.geocode(adrpharma[i])
                    location2 = geolocator.geocode(adrpharma[j])
                    distance2[i][j]=distance.distance((location.latitude,location.longitude), (location2.latitude,location2.longitude)).km
                elif (i>=nbpharmacie) and (j>=nbpharmacie):
                    distance2[i][j]=0
                elif (j>=nbpharmacie):
                    #print("erreur ici")
                    #print(i)
                    #print(j)
                    location = geolocator.geocode(adrpharma[i])
                    location2 = geolocator.geocode(adrcand[j-nbpharmacie])
                    print(adrpharma[i])
                    print(adrcand[j-nbpharmacie])
                    print(distance.distance((location.latitude,location.longitude), (location2.latitude,location2.longitude)).km)
                    distance2[i][j]=distance.distance((location.latitude,location.longitude), (location2.latitude,location2.longitude)).km
                else:
                    location = geolocator.geocode(adrpharma[j])
                    location2 = geolocator.geocode(adrcand[i-nbpharmacie])
                    distance2[i][j]=distance.distance((location.latitude,location.longitude), (location2.latitude,location2.longitude)).km
        print(distance2) 
        print("fuckfuckfuck")
        print(mo)
        
        for i in range(len(mo)):
            if mo[i]==None or mo[i]=='None':
                mo[i]=0
        print(mo)
        maxdist=0
        for i in range(len(c)):
            for j in range(len(c[i])):
                if c[i][j]=='None':
                    c[i][j]=0
        print(c)
        for ligne in distance2:
            for elem in ligne:
                if elem>maxdist:
                    maxdist=elem

        nbtrajetmax=0
        for k in mo:
            if k==1:
                nbtrajetmax+=2

        coef=nbtrajetmax*maxdist

        #definition des variables
        print(n)
        print(p)
        x=np.zeros((mint,n*p),Var)
        print("cest ici x ")
        print(len(x))
        print(len(x[0]))
        for i in range(1,mint+1):
            for j in range(1,mult+1):
                nom="x"+str(i)+"_"+str(j)
                x[i-1][j-1]=m.addVar(name=nom,vtype='B')

        #expression problème de base
        sommeProb=0

        for i in range (0,n):
            for j in range (0,mint):
                for k in range (0,p):
                    sommeProb+=coef*x[j][i*p+k]*mo[i*p+k]

        #expression problème de distance


        for i in range(mint):
            for j in range(n):
                sommeProb-=x[i][j*p]*distance2[j][n+i]  #k=0

            for k in range(1,p):
                for j in range(n):
                    for l in range(n):
                        sommeProb-=x[i][j*p+(k-1)]*x[i][l*p+k]*(distance2[j][l]-distance2[l][n+i]) #cas ou 2 creneau se suivent

            for k in range(1,p):
                for l in range(n):
                    sommeProb-=2*x[i][l*p+k]*distance2[l][n+i] # cas ou le pharmacien n'a pas de creneau juste avant
            for k in range(0,p-1):
                for j in range(n):
                    for l in range(n):
                        sommeProb+=x[i][j*p+(k+1)]*x[i][l*p+k]*distance2[l][n+i] #on enleve le retour si 2 creneau se suivent
            for k in range(0,p-1):
                for j in range(n):
                    for l in range(n):
                        sommeProb+=x[i][j*p+(k+1)]*x[i][l*p+k]*distance2[l][n+i] #on enleve le retour si 2 creneau se suivent
            

        m.setObjective(sommeProb , GRB.MAXIMIZE)

        #premiere contrainte
        sommePremContr=0

        for k in range (0,p):
            for i in range (0,n):
                for ki in range (0,n):
                    for j in range (0,mint):
                        sommePremContr+=x[j][i*ki+k]
                    m.addConstr(sommePremContr <= mo[i*ki+k], "c"+str(u))
                    u=u+1
                    sommePremContr = 0

        #deuxième contrainte
        sommeDeuxContrX=0
        sommeDeuxContrMO=0

        
        for i in range(0,n):
            for j in range (0,mint):
                sommeDeuxContrMO=0
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
        print("cest v")
        print(m.getVars())
        print(len(x))
        print(len(x[0]))
        print("fini")
        print(n)
        print(p)
        resul=np.zeros((mint,n*p),Var)
        print(len(resul))
        print(len(resul[0]))
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

        distfinaleparcouru=0
        for i in range(mint):
            for j in range(n):
                distfinaleparcouru+=resul[i][j*p]*distance2[j][n+i]  #k=0

            for k in range(1,p):
                for j in range(n):
                    for l in range(n):
                        distfinaleparcouru+=resul[i][j*p+(k-1)]*resul[i][l*p+k]*(distance2[j][l]-distance2[l][n+i]) #cas ou 2 creneau se suivent

            for k in range(1,p):
                for l in range(n):
                    distfinaleparcouru+=2*resul[i][l*p+k]*distance2[l][n+i] # cas ou le pharmacien n'a pas de creneau juste avant

            for k in range(0,p-1):
                for j in range(n):
                    for l in range(n):
                        distfinaleparcouru+=-resul[i][j*p+(k+1)]*resul[i][l*p+k]*distance2[l][n+i] #on enleve le retour si 2 creneau se suivent
        

        #for v in m.getVars():
        #    print(v.varName, v.x)
        end = time.time()
        testdebile=0
        def test(vari):
            for i in range(len(resul)):
                for j in range(len(resul[i])):
                    '''if resul[i][j]==1:
                        if mo[j//p*p+j%p]==0 or c[i][j%p]==0:
                            print("agabouga")
                            print(i)
                            print(j)
                            #return False
                    '''
                    print(resul[i][j]==1.0)

                    if j==8  and resul[i][j]==1.0:
                        vari+=1
                    if j==28  and resul[i][j]==1.0:
                        vari+=1
                    if  j==48 and resul[i][j]==1.0:
                        vari+=1
            return vari
        print(test(testdebile))
        print("mo")
        print(mo)
        print("c")
        print(c)
        print(resul)
        print(nbcrefin)
        print(nbcrepha)
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
        print(testdebile)
        print("% des creneaux ont été attribués")
        print(" ")
        print("Distance total parcourue:")
        print(distfinaleparcouru)
        print("kilomètres")
        return render_template("affalgo.html",resultat=resul,nbcandidatt=nbcandidat,mo=mo,c=c)
    return render_template("algo.html")

