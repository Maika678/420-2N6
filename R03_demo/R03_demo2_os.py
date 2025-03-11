import os

# Change le répertoire courant pour qu'il corresponde au répertoire où se trouve le fichier actuel.
os.chdir(os.path.dirname(__file__))


# Imprimez le répertoire courant avec la fonction getcwd() du module os
location = os.getcwd()


# Obtenez la liste des répertoires et fichiers dans le répertoire courant avec la fonction listdir()
# Imprimez tous fichiers et répertoires
fichiers = os.listdir()
for fichier in fichiers:
    print(fichier)

# Avec une boucle for, faites une liste de fichier python dans le répertoire courant
for fichier in os.listdir() :
    if ____ in ____ :
        pass