# -*- coding:utf-8 -*-
# lancer par python3 fichier.py
import os, json, re
os.system("clear")

from flask import Flask
app = Flask(__name__)
app._static_folder = os.path.abspath("./")

@app.route('/')  # route : localhost:5000/ # route qui renvoie la page HTML 
def index():
   # return "Bonjour"
   print('/')
   if os.path.isfile("clientRecherche.html") : #True if specified path is an existing regular file, otherwise returns False.
       return app.send_static_file("clientRecherche.html")
       # html envoyé par server, tous les liens dans html vont recherché dans serveur app.route(/.../...), et envoyer résultat par serveur 
   return "clientRecherche.html non accessible"

@app.route('/image/<fichier>')  # route qui renvoie une image
def image(fichier):
   print('/image/'+fichier)
   if os.path.isfile("IMAGES/"+fichier) :
       return app.send_static_file("IMAGES/"+fichier)
   return fichier+"non accessible"

# @app.route('/references')
# def references() :
#    print("/references")
#    references = []
#    liste = os.listdir("BD_desserts")
#    for fichier in liste :
#       print(fichier)
#       fd = open("BD_desserts/"+fichier)
#       for ligne in fd.readlines() :
#          resultat = re.search("(chocolat)", ligne, re.IGNORECASE)
#          if resultat : # resultat est une zone memoire qui a ete crees 
#             references.append(resultat.group())
#    return json.dumps(references)

@app.route('/recherche/<criteres>')
def recherche_critere(criteres):
   print("/recherche/"+criteres)
   listecriteres = criteres.split(" ")
   liste = os.listdir("BD_desserts")
   for critere in listecriteres :
      lignes = []
      for fichier in liste :
         fd = open("BD_desserts/"+fichier)
         for ligne in fd.readlines() :
            res = re.search(""+critere, ligne, re.IGNORECASE)   
            # re.search() function will search the regex and return the first occurrence.
            # returns a match object when the pattern is found and “null” if the pattern is not found
            if res :
               lignes.append([fichier, ligne])  # Le nom de la page est envoyée avant la ligne dans une sous-liste
   return json.dumps(lignes)

# @app.route('/hello/<param1>')  # ex. route : localhost:5000/hello/Pierre
# def hello1(param1):
#    return "Bonjour "+param1


# @app.route('/hello/<param1>/<param2>')  # ex. route : localhost:5000/hello/Pierre/Paul
# def hello2(param1, param2):
#    return "Hello "+param1+" "+param2

app.run()
