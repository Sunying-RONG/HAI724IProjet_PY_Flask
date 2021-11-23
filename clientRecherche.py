# lancer par python3 ./clientRecherche.py vanille
import sys, json, requests
print("OK")
reponse = requests.get("http://localhost:5000/recherche/"+sys.argv[1])
lignes = reponse.json()
for ligne in lignes : 
    print(ligne)
    print("---------------")