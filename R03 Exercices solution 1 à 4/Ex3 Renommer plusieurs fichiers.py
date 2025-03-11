# importez os
import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.


# # allez dans le dossier Ex3 Videos
os.chdir('Ex3 Videos')
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()

for fichier in os.listdir():
    # # utilisez os.path.splitext pour obtenir le filename et l'extension
    nom_fichier, extension = os.path.splitext(fichier)
    # # utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
    sujet, cours, num = nom_fichier.split("_")
    # # utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
    sujet = sujet.strip()
    cours = cours.strip()
    num = num.strip()
    # # en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
    num = num[1:] # pour retiré le carré
    num = num.zfill(2)
    # # recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
    nouveau_nom = f"{num} {sujet} {cours}{extension}"
    # os.rename(fichier, nouveau_nom)


