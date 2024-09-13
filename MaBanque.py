from Compte import Compte
from Client import Client
from Client import ClientMultiComptes

if __name__ == "__main__":
    # Test de la classe Compte
    compte1 = Compte(1) # crée un compte
    print(f"Votre découvert autorisé c1: {compte1.get_decouvert()}") # affiche son découvert
    compte1.set_decouvert(100) # modifie le découvert à 100
    print(f"Vorte nouveau découvert autorisé c1: {compte1.get_decouvert()}") # affiche le nouveau découvert
    compte1.afficher_solde() # affiche le solde

    #  test de retrait et solde compte 2
    compte2 = Compte(2) # crée un 2ème compte
    compte2.depot(1000) # ajoute un dépot de 1000
    print(f"Votre solde : {compte2.get_solde()}") # affiche le solde
    print(compte2.retrait(600)) # retire 600 du solde
    compte2.afficher_solde() # reaffiche le solde
    print(compte2.retrait(700)) # fait un nouveau retrait de 700
    compte2.set_decouvert(500) # le découvert est mit à 500
    print(compte2.retrait(700)) # fait un retrait de 700
    compte2.afficher_solde() # affiche le solde final

    # Création d'un 2eme client 
    client2 = Client("Terrieur", "Alain", compte2) # le client à pour compte le c2
    client2.afficher_solde() # affiche le solde du compte 2

    # Client avec plusieurs comptes
    compte10 = Compte(10) # crée le compte 10
    compte10.depot(1000) # ajoute un dépot de 1000
    client_multi = ClientMultiComptes("Patrick", "létoile", compte10) # initialise le client à plusieurs comptes 
    client_multi.afficher_etat_client() # affiche le solde du client

    compte20 = Compte(20) # crée le compte 10
    compte20.depot(2500) # ajoute un dépot de 2500
    client_multi.ajouter_compte(compte20) # le compte 20 est ajouté au compte client 
    client_multi.afficher_etat_client() # affiche l'état des comptes du client

