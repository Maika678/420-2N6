import csv


# # créé et écrit dans un fichier
with open("demo5-b.txt","w",encoding="utf-8") as fichier2:
    csv_writer = csv.writer(fichier2, delimiter="|", lineterminator="\n")
    csv_writer.writerow(["nom", "id", "groupe"])
    csv_writer.writerow(["anna","34","groupe2"])
