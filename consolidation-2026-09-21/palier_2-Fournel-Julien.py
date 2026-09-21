print("--- Commande de postes ---")

nb_postes = int(input("Combien de postes à commander ? "))
prix_unitaire = float(input("Prix d'un poste hors taxes ?"))
total_ttc = prix_unitaire * 1.20
print("Nombre de postes : ", nb_postes, 2)
print("Prix unitaire = ", prix_unitaire, "euros")
print("Total TTC d'un poste = ", total_ttc, "euros")
somme_prix_unitaire_total = nb_postes * prix_unitaire
somme_total_ttc_total = nb_postes * total_ttc
print("Prix unitaire total ", somme_prix_unitaire_total, "euros")
print("Total TTC de tous les postes", somme_total_ttc_total, "euros")
print("-" * 40)