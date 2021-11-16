# -*- coding:utf-8 -*-
import os, json, re
os.system("clear")

from flask import Flask
app = Flask(__name__)

@app.route('/')  # route : localhost:5000/
def index():
   return "Bonjour"

@app.route('/references')
def references() :
   print("/references")
   references = []
   liste = os.listdir("BD_desserts")
   for fichier in liste :
      print(fichier)
      fd = open("BD_desserts/"+fichier)
      for ligne in fd.readlines() :
         resultat = re.search("muffin", ligne)
         if resultat : # resultat est une zone memoire qui a ete crees 
            references.append(resultat.group())
   return json.dumps(references)

@app.route('/recherche/<critere>')
def recherche_critere(critere) :
   print("/recherche/"+critere)
   lignes = []
   liste = os.listdir("BD_desserts")
   for fichier in liste :
      fd = open("BD_desserts/"+fichier)
      for ligne in fd.readlines() :
         res1 = re.search("muffin", ligne)
         res2 = re.search(""+critere, ligne)
         if res1 and res2 :
            lignes.append(ligne)
   return json.dumps(lignes)

@app.route('/hello/<param1>')  # ex. route : localhost:5000/hello/Pierre
def hello1(param1):
   return "Bonjour "+param1


@app.route('/hello/<param1>/<param2>')  # ex. route : localhost:5000/hello/Pierre/Paul
def hello2(param1, param2):
   return "Hello "+param1+" "+param2

app.run()
