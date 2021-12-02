champs="Cupcake %C3%89clair_(p%C3%A2tisserie) Tarte_au_chocolat Souffl%C3%A9"
champsNom="Cupcake Éclair_(pâtisserie) Tarte_au_chocolat Soufflé"
champsArray=($champs)
champsNomArray=($champsNom)
for i in ${!champsArray[@]}
do
    echo $i
    echo importation de ${champsArray[$i]}
    echo importation de ${champsNomArray[$i]}
    curl "https://fr.wikipedia.org/w/index.php?title=${champsArray[$i]}&action=raw" > BD_desserts/${champsNomArray[$i]}
done

# for i, champ in $champs
# do 
#     echo importation de $champ
#     curl "https://fr.wikipedia.org/w/index.php?title=${champ}&action=raw" > BD_desserts/$champ
# done
# copier url ici, utiliser le nom avec % dans champs
# https://fr.wikipedia.org/w/index.php?title=%C3%89clair_(p%C3%A2tisserie)

