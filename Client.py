from Compte import Compte

class Client:
    def __init__(self, n: str, p: str, c: Compte): #ajout des attributs client
        self.__nom = n
        self.__prenom = p
        self.__compte_courant = c

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

