from Client import Client
from Compte import Compte

if __name__ == "__main__":
    # Création d'un client avec un compte
    compte = Compte(1)
    client = Client("Tare", "Guy", compte)

    # Test des accesseurs pour afficher nom et prénom du client
    print(f"Nom: {client.get_nom()}")
    print(f"Prénom: {client.get_prenom()}")

    # Test de l'affichage du solde
    client.afficher_solde()
