
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


