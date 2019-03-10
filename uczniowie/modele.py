#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza_plik = 'baza.db'
baza = SqliteDatabase(baza_plik) 

### MODELE #
class BazaModel(Model):
    class Meta:
        database = baza

class Plec(BazaModel):
    plec_nazwa = CharField(null=False)

class Klasa(BazaModel):
    klasa = TextField(null=False)
    rok_naboru = DateField()
    rok_matury = DateField()

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = ForeignKeyField(Plec)
    klasa = ForeignKeyField(Klasa)
