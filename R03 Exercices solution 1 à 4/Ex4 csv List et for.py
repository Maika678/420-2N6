import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script



# Importez le module csv
import csv


# Nous avons des offres de stages and le fichier "Ex4 Emplois Reseautique.csv"
# Faites un petit script qui ouvre le fichier csv en mode lecture et qui affiche uniquement les offres ou la demande de Diplôme a la valeur 'Dec' ou 'Non déterminé'
 

# Regardez le contenu du fichier "Ex4 Emplois Reseautique.csv"
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                   Poste;Compagnie;Ville;Expérience;Diplôme;Salaire
#          Certains champs ont la valeur "Non déterminé"



# Il vous faudra imprimer les informations des emplois demandant le Diplôme de 'Dec' ou ayant la valeur 'Non déterminé'
# 
#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas


ficher_a_lire = os.path.join("csvs","Ex4 Emplois Reseautique.csv" )


# INSTRUCTIONS DÉTAILLÉES
# Ouvrez en lecture le fichier "Ex4 Emplois Reseautique.csv", en utilisant l'encoding utf-8
with open(ficher_a_lire,"r",encoding='utf-8') as fichier_lu:
    # Lisez tout le contenu du fichier avec csv.reader() avec le delimiter=';'  
    lecteur = csv.reader(fichier_lu, delimiter=';') 
    # Sautez la première ligne avec next() puisqu'elle ne contient que les entêtes de colonnes
    next(lecteur)
    # Dans votre boucle qui passera à travers les lignes
    #      Le diplôme sera l'élément à l'indice 4 
    #      Vérifiez sa valeur et si elle est 'Dec' ou 'Non déterminé' imprimez l'offre d'emploi
    for ligne in lecteur :
        if ligne[4] in ['Dec', 'Non déterminer'] :
            print(ligne)

