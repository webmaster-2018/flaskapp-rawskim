#!/usr/bin/env python
# -- coding: utf-8 --

from flask import Flask
from flask import render_template, request, flash, redirect, url_for, abort
from modele import *
from forms import *

app = Flask(__name__)

# widok domyślny


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/lista")
def lista():
    uczen = Uczen.select()
    return render_template('lista.html', uczen=uczen)


@app.route("/lista_klas")
def lista_klas():
    klasa = Klasa.select()
    return render_template('lista_klas.html', klasa=klasa)


@app.route("/dodaj", methods=['GET', 'POST'])
def dodaj():

    form = DodajForm()
    form.klasa.choices = [(k.id, k.klasa)
                          for k in Klasa.select()]
    form.plec.choices = [(p.id, p.plec_nazwa)
                           for p in Plec.select()]

    if form.validate_on_submit():
        u = Uczen(imie=form.imie.data,
                    nazwisko=form.nazwisko.data,
                    plec=form.plec.data,
                    klasa=form.klasa.data)
        u.save()

        flash("Dodano ucznia: {} {}".format(
            form.imie.data, form.nazwisko.data))
        return redirect(url_for('lista'))

    return render_template('dodaj.html', form=form)

@app.route("/dodaj_klasy", methods=['GET', 'POST'])
def dodaj_klasy():

    form = DodajKlasaForm()

    if form.validate_on_submit():
        k = Klasa(klasa=form.klasa.data,
                  rok_naboru=form.rok_naboru.data,
                  rok_matury=form.rok_matury.data
        )
        k.save()

        flash("Dodano klasę: {}".format(
            form.klasa.data))
        return redirect(url_for('lista_klas'))

    return render_template('dodaj_klasy.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def get_or_404(id):
    try:
        s = Uczen.get_by_id(id)
        return s
    except Uczen.DoesNotExist:
        abort(404)
