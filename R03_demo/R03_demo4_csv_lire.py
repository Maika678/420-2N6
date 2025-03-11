import os
import csv
os.chdir(os.path.dirname(__file__)) # placement du terminal dans le répertoire où se trouve ce script.


 #On veut compter le nombre d'étudiants dans le programme d'informatique
with open("etudiants.csv","r") as fichier:
     lecteur_csv = csv.reader(fichier)   #créer un objet de la classe "reader"
     next(lecteur_csv)   # passe à la prochaine ligne ( pas nécessaire ici mais on veux souvent sauté la première ligne d'un csv )
     compteur = 0 
     for ligne in lecteur_csv : # pour chaque ligne dans notre "lecteur" (donc dans notre fichier)
         pass    # On compte le nombre d'étudiants en informatique ici

     print(f"Il y a {compteur} étudiants dans le programme d'informatique")
    


























""" 
with open('etudiants.csv',"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    # saute la première ligne #
    list_dict = []
    header = next(csv_reader)
    for line in csv_reader :
        petit_dict = {"nom":line[0],"id":line[1],"programme":line[2]}
        list_dict.append(petit_dict)

print(list_dict) """

