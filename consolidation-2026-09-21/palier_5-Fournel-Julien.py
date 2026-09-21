from palier_4_Fournel_Julien import postes  

print("--- Recherche d'un poste ---")
cherche = input("Quel poste chercher ? ")

trouve = False

for poste in postes:
    if cherche == postes:
        trouve = True
        print(cherche, "est dans le parc")
    else:
        trouve = False
        print(cherche, "n'est pas dans le parc")

print("-" * 40)