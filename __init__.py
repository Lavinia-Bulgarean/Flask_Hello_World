from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__) 
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>" #cOmm2

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2
  if result % 2 == 0:
        message = "La somme est paire."
    else:
        message = "La somme est impaire."
    return "<h2>La somme de vos valeurs est : </h2>" + str(result)

  
if __name__ == "__main__":
  app.run(debug=True)
