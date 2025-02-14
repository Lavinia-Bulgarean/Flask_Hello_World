from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__) 
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

app = Flask(__name__) 
@app.route("/cnam")
def MaPremiereAPI():
    return render_template("cnam.html")
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>" #cOmm2

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2
    if result % 2 == 0:
        message = "La somme est paire."
    else:
        message = "La somme est impaire."
    return f"<h2>La somme de vos valeurs est : {result}</h2><p>{message}</p>"

@app.route('/somme_toutes/<path:valeurs>', methods=['GET'])
def somme_toutes(valeurs):
    # Convertir la chaîne de caractères en liste de nombres
    liste_valeurs = [int(x) for x in valeurs.split('/')]
    
    # Calculer la somme des valeurs
    total = sum(liste_valeurs)
    
    return f"<h2>La somme de toutes vos valeurs est : {total}</h2>"

@app.route('/valeur_max/<path:valeurs>', methods=['GET'])
def valeur_max(valeurs):
    # Convertir la chaîne de caractères en liste d'entiers
    liste_valeurs = [int(x) for x in valeurs.split('/')]
    
    # Initialiser la variable max avec la première valeur de la liste
    max_valeur = liste_valeurs[0]
    
    # Boucle pour parcourir les valeurs et trouver la valeur maximale
    for valeur in liste_valeurs:
        if valeur > max_valeur:
            max_valeur = valeur  # Mise à jour de la valeur maximale

    return f"<h2>La valeur maximale saisie est : {max_valeur}</h2>"

  
if __name__ == "__main__":
  app.run(debug=True)
