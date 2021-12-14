# HAI724IProjet_PY_Flask

# Pour lancer
1. Télécharger le projet, par exemple :  
git clone https://github.com/Sunying-RONG/HAI724IProjet_PY_Flask.git
2. Dans terminal entrer dans le dossier HAI724IProjet_PY_Flask qui est téléchargé, lancer serveur par :  
python3 serveurFlask_basique.py  
3. Dans navigateur : localhost:5000
# Fonctions implémentées
1. Rechercher par un mot clé :  
Pour chaque fichier,  retourner le nom de fichier avec lien de wikipédia et une ligne qui comprend ce mot clé si existe.  
E.g. Recherche : vanille

2. Rechercher par plusieurs mots clés, séparés par espace :  
Retourner nom de fichier avec lien de wikipédia et une ligne qui comprend tous les mots clés dans n'importe quel ordre.  
Puis, pour les autres fichiers qui ne comprennent pas tous les mots clés, retourner nom de fichier avec lien de wikipédia et une ligne qui comprend au moins un mot clé parmi tous les mots clés.  
E.g. Recherche : vanille chocolat

3. Rechercher par plusieurs mots clés compris les mots clés chacuns avec "", qui doit forcément exister :  
Retourner nom de fichier avec lien de wikipédia et une ligne qui comprend tous les mots clés dans n'importe quel ordre.  
Puis, pour les autres fichiers qui ne comprennent pas tous les mots clés, retourner nom de fichier avec lien de wikipédia et une ligne qui comprend tous les mots clés obligatoires dans n'importe quel ordre.  
E.g. Recherche : vanille chocolat "fraise" "citron"

4. Enlever les espaces au début et à la fin, garder un espace entre les mots
E.g. Recherche :       vanille    "chocolat"     

5. Tous les mots clés qui s'affichent dans résultat sont en couleur rouge.

6. Mettre une image de fond. 

