import sys, os, json
os.system("curl localhost:5000/recherche/"+sys.argv[1]+" > resultat")