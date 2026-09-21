print("--- Etat d'un poste ---")
espace_libre = int(input("Espace libre sur le disque, en GO ?"))
age = int(input("Age du poste, en annees ? "))

if espace_libre < 10:
    print("Etat: A NETTOYER, disque presque plein ")
elif age < 5:
    print("Etat: A REMPLACER, poste trop ancien ")
elif espace_libre < 50 and age < 3:
    print("A SURVEILLER ")
else:
    print("Etat: OK ")
print("-" * 40)
""" il affiche pas A REMPLACER car il prends en compte la premire condition pour la valeur 5 qui correspond au disque mais ne continue pas pour la deuxième contidion. Il faudrait appliquer une boucle selon moi."""