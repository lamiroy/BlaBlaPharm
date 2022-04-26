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
    Address TEXT,
    CreLunMat INTEGER,
    CreLunApr INTEGER,
    CreMardMat INTEGER,
    CreMardApr INTEGER,
    CreMerMat INTEGER,
    CreMerApr INTEGER,
    CreJeuMat INTEGER,
    CreJeuApr INTEGER,
    CreVenMat INTEGER,
    CreVenApr INTEGER
);"""
    
    pharmacies_table = """ CREATE TABLE Pharmacies (
    Nom TEXT PRIMARY KEY,
    Address TEXT,
    CreLunMat INTEGER,
    CreLunApr INTEGER,
    CreMardMat INTEGER,
    CreMardApr INTEGER,
    CreMerMat INTEGER,
    CreMerApr INTEGER,
    CreJeuMat INTEGER,
    CreJeuApr INTEGER,
    CreVenMat INTEGER,
    CreVenApr INTEGER
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
