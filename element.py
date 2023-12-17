from abc import ABCMeta, abstractmethod

class Composition:
    def __init__(self, product=None, quantity=0):
        self.product = product
        self.quantity = quantity
    
    def __eq__(self, other):
        if isinstance(other, Composition):
            return self.product == other.product and self.quantity == other.quantity
        return False

class Product(metaclass=ABCMeta):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    @abstractmethod
    def get_prix_HT(self):
        pass

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.code == other.code
        return False
    
class ProduitElementaire(Product):
    def __init__(self, name, code, prixAchat):
        super().__init__(name, code)
        self.prixAchat = prixAchat

    def __str__(self):
        return f"ProduitElementaire: Nom - {self.name}, Code - {self.code}, Prix d'Achat - {self.prixAchat}"

    def get_prix_HT(self):
        return self.prixAchat

class ProduitCompose(Product):
    tauxTVA = 0.18

    def __init__(self, name, code, fraisFabrication):
        super().__init__(name, code)
        self.fraisFabrication = fraisFabrication
        self.listeConstituants = []

    def __str__(self):
        return f"ProduitCompose: Nom - {self.name}, Code - {self.code}, Frais de Fabrication - {self.fraisFabrication}"

    def get_prix_HT(self):
        total_price_ht = 0

        for composition in self.listeConstituants:
            total_price_ht += composition.product.get_prix_HT() * composition.quantity

        return total_price_ht + self.fraisFabrication

# les instances
elementaire1 = ProduitElementaire("Elem1", "E1", 10)
elementaire2 = ProduitElementaire("Elem2", "E2", 15)

compose1 = ProduitCompose("Compose1", "C1", 5)
compose1.listeConstituants.append(Composition(elementaire1, 2))
compose1.listeConstituants.append(Composition(elementaire2, 3))

total_price_ht_compose1 = compose1.get_prix_HT()
print(f"Total Price HT for Compose1: {total_price_ht_compose1}")
