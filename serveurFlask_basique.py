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
   if os.path.isfile("image/"+fichier) :
      return app.send_static_file("image/"+fichier)
   return fichier+"non accessible"

@app.route('/style/<fichier>')
def style(fichier):
   print('/style/'+fichier)
   if os.path.isfile(fichier) :
      return app.send_static_file(fichier)
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

# @app.route('/recherche/<criteres>')
# def recherche_critere(criteres):
#    print("/recherche/"+criteres)
#    listecriteres = criteres.split(" ")
#    liste = os.listdir("BD_desserts")
#    for critere in listecriteres :
#       lignes = []
#       for fichier in liste :
#          fd = open("BD_desserts/"+fichier)
#          for ligne in fd.readlines() :
#             res = re.search(""+critere, ligne, re.IGNORECASE)   
#             # re.search() function will search the regex and return the first occurrence.
#             # returns a match object when the pattern is found and “null” if the pattern is not found
#             if res :
#                lignes.append([fichier, ligne])  # Le nom de la page est envoyée avant la ligne dans une sous-liste
#    return json.dumps(lignes)

@app.route('/recherche/<criteres>')
def recherche_critere(criteres):
   print("/recherche/"+criteres)
   listecriteres = criteres.split(" ")
   print("listecriteres: ", listecriteres)
   regexTousCriteres = ""
   regexOuCriteres = ""
   regexMustCristeres = ""

   for critere in listecriteres :
      if (critere[0:1]=='"' and critere[-1:]=='"') :
         critere = critere[1:-1]
         print(critere)
         regexMustCristeres = regexMustCristeres+"(?=.*"+critere+")"
      regexTousCriteres = regexTousCriteres+"(?=.*"+critere+")"
      regexOuCriteres = regexOuCriteres + critere + "|" 

   regexTousCriteres = regexTousCriteres+".*" # eg (?=.*jack)(?=.*james).* - match jack and james in any order: jack and james. james and jack.
   regexOuCriteres = regexOuCriteres[:-1] # eg "aa|cc" match "bb cc dd"
   regexMustCristeres = regexMustCristeres+".*" # in any order
   print(regexTousCriteres)
   print(regexOuCriteres)
   print(regexMustCristeres)

   liste = os.listdir("BD_desserts")
   fichierTrouve = []
   # afficher une ligne de fichier qui comprend tous les critères
   lignes = []
   for fichier in liste :
      fd = open("BD_desserts/"+fichier)
      for ligne in fd.readlines() :
         resTous = re.search(regexTousCriteres, ligne, re.IGNORECASE)
         # print(resTous)
         if resTous :
            print("!",fichier)
            lignes.append([fichier, ligne])
            fichierTrouve.append(fichier)
            break
   # pour les autre fichiers
   for fichier in liste :
      if fichier not in fichierTrouve :
         fd = open("BD_desserts/"+fichier)
         # s'il y a des criètres obligatoires, qui avec "", afficher une ligne qui comprend ces critères obligatoires.
         if len(regexMustCristeres) > 2 : # s'il n'y a pas de mot clé obligatoire, regexMustCristeres est .*
            for ligne in fd.readlines() :
               resMust = re.search(regexMustCristeres, ligne, re.IGNORECASE)
               if resMust :
                  print("!",fichier)
                  lignes.append([fichier, ligne])
                  break
         # s'il y a pas des critères obligatoires, afficher une ligne qui comprend au moins une critère, n'import laquel.
         else :
            for ligne in fd.readlines() :
               res = re.search(regexOuCriteres, ligne, re.IGNORECASE)
               # print(res)
               if res :
                  print("!",fichier)
                  lignes.append([fichier, ligne])
                  break
   return json.dumps(lignes)

# @app.route('/hello/<param1>')  # ex. route : localhost:5000/hello/Pierre
# def hello1(param1):
#    return "Bonjour "+param1


# @app.route('/hello/<param1>/<param2>')  # ex. route : localhost:5000/hello/Pierre/Paul
# def hello2(param1, param2):
#    return "Hello "+param1+" "+param2

app.run()
