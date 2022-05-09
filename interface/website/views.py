from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask_login import login_required, current_user
from .models import Note
import random
import numpy as np
import sqlite3

views = Blueprint('views', __name__)

liste_vocabulaire = []
longueur_initiale = []
score = [0]

DATABASE = '/Users/eliottpommier/Documents/2A_TELECOM/PIDR/BlaBlaPharm/interface/website/database.db' # le nom du fichier de votre base sqlite3

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

@views.route('/algo')
def algo():
    return render_template("algo.html")

