champs="Cupcake %C3%89clair_(p%C3%A2tisserie) Tarte_au_chocolat Souffl%C3%A9"
for champ in $champs
do 
    echo importation de $champ
    curl "https://fr.wikipedia.org/w/index.php?title=${champ}&action=raw" > BD_desserts/$champ
done