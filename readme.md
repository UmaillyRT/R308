# TP1 La banque

## Les classes

### Client 
from compte import Compte

class Client:
    def __init__(self, n: str, p: str, c: Compte): #ajout des attributs client
        self.__nom = n
        self.__prenom = p
        self.__compte_courant = c

# assesseurs 
# Accesseurs pour obtenir nom et prénom
    def get_nom(self) -> str:
        return self.__nom

    def get_prenom(self) -> str:
        return self.__prenom

# Accesseurs pour récuperer et affichage du solde
    def get_solde(self) -> float:
        return self.__compte_courant.get_solde()

    def afficher_solde(self):
        print(f"Solde de {self.__prenom} {self.__nom} : {self.get_solde()}")



### Compte
class Compte:
    def __init__(self, numero: int): # ajout des attributs compte 
        self.__numero = numero # le numéro de compte est un parametre pour l'identifier
        self.__solde = 0.0 # le solde est mit à 0
        self.__decouvert = 0.0 # le découvert également

# Accesseurs 
    def get_decouvert(self) -> float:
        return self.__decouvert # retourne le montant du découvert autorisé

    def get_numero(self) -> int:
        return self.__numero # retourne le numéro de compte

    def get_solde(self) -> float:
        return self.__solde # retourne le montant du solde

# Mutateur pour découvert
    def set_decouvert(self, montant: float):
        self.__decouvert = montant # met à jour le découvert

# Affichage du solde
    def afficher_solde(self):
        print(f"Solde : {self.__solde}")

# Dépôt de somme sur le compte
    def depot(self, montant: float):
        self.__solde += montant # ajoute le montant au solde
        return f"Dépot effectué, Dépot de {montant}€"
    
# Retrait
    def retrait(self, montant: float) -> str:
        if montant <= self.__solde + self.__decouvert: 
            self.__solde -= montant # retire dans le solde si le retrait est positif
            return f"Retrait effectué, Retrait de {montant}€"

        else:
            return "Retrait refusé"


### ClientMultiComptes
class ClientMultiComptes:
    def __init__(self, nom: str, prenom: str, compte: Compte): #ajout des attributs client
        self.__nom = nom
        self.__prenom = prenom
        self.__tabcomptes = [compte] #permet au client d'avoir plusieurs compte (tableau de compte)
        self.__nbComptes = 1 

# Ajout d'un compte
    def ajouter_compte(self, c: Compte):
        self.__tabcomptes.append(c) # ajoute un compte à la lsite
        self.__nbComptes += 1 # incrémentation du nombre de compte

# Récupération du solde final
    def get_solde(self) -> float:
        return sum(compte.get_solde() for compte in self.__tabcomptes) # retourne le solde du compte clients
    

# Affichage des comptes et du solde
    def afficher_etat_client(self):
        print(f"Client : {self.__nom} {self.__prenom}") # affiche les infos du client
        for compte in self.__tabcomptes: 
            print(f"Compte {compte.get_numero()}: votre solde : {compte.get_solde()}") # affiche le numéro des comptes et leur soldes
        print(f"Solde Client : {self.get_solde()}")  # affiche la somme totale des compte



## Les programmes de test

### TestClient
from client import Client
from compte import Compte

if __name__ == "__main__":
# Création d'un client avec un compte
    compte = Compte(1)
    client = Client("Tare", "Guy", compte)

# Test des accesseurs pour afficher nom et prénom du client
    print(f"Nom: {client.get_nom()}")
    print(f"Prénom: {client.get_prenom()}")

# Test de l'affichage du solde
    client.afficher_solde()

### MaBanque
from compte import Compte
from client import Client
from client import ClientMultiComptes

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