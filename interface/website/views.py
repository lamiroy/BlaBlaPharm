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

@views.route('/ajoutcand')
def ajoutcand():
    return render_template("ajoutcand.html")

@views.route('/ajoutpharma')
def ajoutpharma():
    return render_template("ajoutpharma.html")

@views.route('/visualisation')
def visualisation():
    cc = query_db('select * from Candidats')
    for i in range(len(cc)):
        cc[i]=list(cc[i])
    return render_template("visualisation.html" ,elem=cc)

@views.route('/algo')
def algo():
    return render_template("algo.html")

