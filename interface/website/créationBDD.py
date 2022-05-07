#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:11:25 2022

@author: eliottpommier
"""

import sqlite3
from sqlite3 import Error


def create_connection(db):
    c = None
    try:
        c = sqlite3.connect(db)
        return c
    except Error as e:
        print(e)

    return c


def create_table(conn, table):
    try:
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)


def main():
    db = r"database.db"


    candidats_table = """ CREATE TABLE Candidats (
    Nom TEXT PRIMARY KEY,
    Prenom TEXT,
    Addresse TEXT,
    Telephone TEXT,
    Lun8h_10h INTEGER,
    Lun10h_12h INTEGER,
    Lun14h_16h INTEGER,
    Lun16h_18h INTEGER,
    Mar8h_10h INTEGER,
    Mar10h_12h INTEGER,
    Mar14h_16h INTEGER,
    Mar16h_18h INTEGER,
    Mer8h_10h INTEGER,
    Mer10h_12h INTEGER,
    Mer14h_16h INTEGER,
    Mer16h_18h INTEGER,
    Jeu8h_10h INTEGER,
    Jeu10h_12h INTEGER,
    Jeu14h_16h INTEGER,
    Jeu16h_18h INTEGER,
    Ven8h_10h INTEGER,
    Ven10h_12h INTEGER,
    Ven14h_16h INTEGER,
    Ven16h_18h INTEGER,
    Competences TEXT
);"""
    
    pharmacies_table = """ CREATE TABLE Pharmacies (
    Nom TEXT PRIMARY KEY,
    Addresse TEXT,
    Lun8h_10h INTEGER,
    Lun10h_12h INTEGER,
    Lun14h_16h INTEGER,
    Lun16h_18h INTEGER,
    Mar8h_10h INTEGER,
    Mar10h_12h INTEGER,
    Mar14h_16h INTEGER,
    Mar16h_18h INTEGER,
    Mer8h_10h INTEGER,
    Mer10h_12h INTEGER,
    Mer14h_16h INTEGER,
    Mer16h_18h INTEGER,
    Jeu8h_10h INTEGER,
    Jeu10h_12h INTEGER,
    Jeu14h_16h INTEGER,
    Jeu16h_18h INTEGER,
    Ven8h_10h INTEGER,
    Ven10h_12h INTEGER,
    Ven14h_16h INTEGER,
    Ven16h_18h INTEGER,
    Competences TEXT,
    Description_poste TEXT
);"""


    # create a database connection
    c = create_connection(db)

    # create tables
    if c is not None:
        create_table(c, candidats_table)
        create_table(c, pharmacies_table)
        c.close()
    else:
        print("Erreur, la connexion n'a pas pu être établie")


if __name__ == '__main__':
    main()
