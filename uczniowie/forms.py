#!/usr/bin/env python
# -- coding: utf-8 --

from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, BooleanField
from wtforms import SelectField, FormField, FieldList
from wtforms.validators import Required

blad_1 = 'To pole jest wymagane'

class DodajForm(FlaskForm):
    imie = StringField('Imie: ', validators=[Required(message="blad_1")])
    nazwisko = StringField('Nazwisko: ', validators=[Required(message="blad_1")])
    plec = SelectField('Płec: ', coerce=int)
    klasa = SelectField('Klasa: ', coerce=int)

    id = HiddenField()

class DodajKlasaForm(FlaskForm):
    klasa = StringField('Nazwa klasy: ', validators=[
                          Required(message="blad_1")])
    rok_naboru = StringField('Rok naboru: ', validators=[
                          Required(message="blad_1")])
    rok_matury = StringField('Rok matury: ', validators=[
                          Required(message="blad_1")])
