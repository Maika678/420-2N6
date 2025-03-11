auto = {"marque":"ford",
        "modele": "mustange",
        "annee" : 1964}

# Obtenir l'année de fabrication avec le .get()
print(auto["annee"])
# Obtenir l'année de fabrication SANS le .get()
print(auto.get("annee"))


# Le comportement de auto["annee"] et auto.get["annee"] différent lorsque la clef n'existe pas 
# Essayons avec la couleur de la voiture
auto["couleur"] = "rouge"
print(auto["couleur"])

# Modifier l'année de fabrication pour que ce soit 1974
auto["annee"] = 1974
print(auto["annee"])

# Ajouter une valeur pour le kilomètrage
auto["kilo"] = 200
print(auto["kilo"])
#ou auto.update({"marque" : "Ford", "modele" : "autre"})