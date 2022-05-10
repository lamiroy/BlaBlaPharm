#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:28:17 2022

@author: eliottpommier
"""

# -*- coding: utf-8 -*-
import sqlite3
try:
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    print("Connexion réussie à SQLite")
    sql1 = "INSERT INTO Candidats (Nom,Prenom,Addresse,Telephone,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences) VALUES ('Houël','Nicolas','1 rue Grandville Nancy','0715241587','1','1','0','1','1','0','1','1','1','0','1','0','1','0','1','0','1','0','1','0','Créateur du Jardin des Apothicaires')"
    count1 = cur.execute(sql1)
    print("1")
    sql2 = "INSERT INTO Candidats (Nom,Prenom,Addresse,Telephone,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences) VALUES ('Charas','Moyse','36 quai de la Bataille Nancy','0716191698','1','0','0','1','1','1','1','1','0','0','0','0','1','0','1','1','1','1','1','1','Premier pharmacien français')"
    count2 = cur.execute(sql2)
    print("2")
    sql3 = "INSERT INTO Candidats (Nom,Prenom,Addresse,Telephone,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences) VALUES ('Lémery','Nicolas','16 rue de Santifontaine Nancy','0716451715','0','1','1','1','0','1','0','1','0','0','0','1','1','0','0','1','1','1','0','1','A écrit La Pharmacopée universelle')"
    count3 = cur.execute(sql3)
    print("3")
    sql4 = "INSERT INTO Candidats (Nom,Prenom,Addresse,Telephone,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences) VALUES ('Baumé','Antoine','104 avenue Carnot Saint-Max','0717281804','0','0','1','1','0','1','1','1','0','1','0','1','1','1','1','0','0','1','0','1','Créateur de l’aréomètre Baumé')"
    count4 = cur.execute(sql4)
    print("4")
    sql5 = "INSERT INTO Pharmacies (Nom,Addresse,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences,Description_poste) VALUES ('Pharmacie de Mon Désert','15 rue de Mon Désert Nancy','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','Dois connaitre la différence entre du Doliprane et du Smecta','Le pharmacien devra vendre des médicaments')"
    count5 = cur.execute(sql5)
    print("5")
    sql6 = "INSERT INTO Pharmacies (Nom,Addresse,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences,Description_poste) VALUES ('Pharmacie du point central','35 rue saint-dizier Nancy','0','0','0','0','1','1','1','1','1','1','1','1','0','0','1','1','0','0','1','1','Au moins 40 ans de experiences','Le pharmacien devra nettoyer le matériel après que ses collègues ai travailler dessus')"
    count6 = cur.execute(sql6)
    print("6")
    sql7 = "INSERT INTO Pharmacies (Nom,Addresse,Lun8h_10h,Lun10h_12h,Lun14h_16h,Lun16h_18h,Mar8h_10h,Mar10h_12h,Mar14h_16h,Mar16h_18h,Mer8h_10h,Mer10h_12h,Mer14h_16h,Mer16h_18h,Jeu8h_10h,Jeu10h_12h,Jeu14h_16h,Jeu16h_18h,Ven8h_10h,Ven10h_12h,Ven14h_16h,Ven16h_18h,Competences,Description_poste) VALUES ('Pharmacie saint jean','1 avenue Foch Nancy','1','1','1','1','0','0','0','0','1','1','1','1','0','0','0','0','1','1','1','1','Aucunes','Le pharmacien sera le nouveau patron')"
    count7 = cur.execute(sql7)
    conn.commit()
    print("Enregistrement inséré avec succès dans la table Candidats et Pharmacies")
    cur.close()
    conn.close()
    print("Connexion SQLite est fermée")
except sqlite3.Error as error:
    print("Erreur lors de l'insertion", error)