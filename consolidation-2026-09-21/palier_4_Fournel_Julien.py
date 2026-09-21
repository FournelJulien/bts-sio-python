print("--- Parc actuel---")

postes = ["GSB-PARIS-01", "GSB-LYON-02", "GSB-NANTES-03", "GSB-LILLE-04", "GSB-PARIS-05"]

compteur = 0 
for i in range(len(postes)):
    compteur = i+1
    print(compteur, ": ", postes[i])

print(compteur, "postes dans le parc ")