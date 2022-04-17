from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, VI, Expressions, Delivery, Invoicing, Ordering, Remuneration, Sales, WorkEvents
import random
import numpy as np

views = Blueprint('views', __name__)

liste_vocabulaire = []
longueur_initiale = []
score = [0]


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
    return render_template("visualisation.html")

@views.route('/algo')
def algo():
    return render_template("algo.html")

