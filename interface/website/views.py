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
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


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
        if(check1):
            print("check1")
        if(check2):
            print("check2")
        
        query = "INSERT INTO Candidats VALUES ("+nom+','+prenom+','+adresse+','+str(check1)+','+str(check2)+','+str(check3)+','+str(check4)+','+str(check5)+','+str(check6)+','+str(check7)+','+str(check8)+','+str(check9)+','+str(check10)+")"
        query_db(query)
        print(nom,prenom,adresse,check1,check2)
        
    return render_template("ajoutcand.html")

@views.route('/ajoutpharma')
def ajoutpharma():
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

