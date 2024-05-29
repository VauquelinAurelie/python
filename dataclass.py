from dataclasses import dataclass
from typing import List
from datetime import date


@dataclass
class Contact:
    telephone: str
    email: str

    def __str__(self):
        return f"Téléphone: {self.telephone}, Email: {self.email}"


@dataclass
class Adresse:
    adresse: str
    code_postal: str
    ville: str

    def __str__(self):
        return f"Adresse: {self.adresse}, Code postal: {self.code_postal}, Ville: {self.ville}"


@dataclass
class Personne:
    nom: str
    prenom: str
    date_naissance: date
    contact: Contact
    adresse: Adresse

    def __str__(self):
        return (f"Nom: {self.nom}, Prénom: {self.prenom}, "
                f"Date de naissance: {self.date_naissance},\n"
                f"Contact: {self.contact},\n"
                f"Adresse: {self.adresse}")


@dataclass
class Repertoire:
    personnes: List[Personne]

    def __str__(self):
        return "\n\n".join(str(personne) for personne in self.personnes)


# Fonction pour créer des exemples de données
def creer_repertoire_exemple() -> Repertoire:
    personne1 = Personne(
        nom="Dupont",
        prenom="Jean",
        date_naissance=date(1985, 4, 12),
        contact=Contact(
            telephone="0123456789",
            email="jean.dupont@example.com"
        ),
        adresse=Adresse(
            adresse="123 Rue Principale",
            code_postal="75001",
            ville="Paris"
        )
    )

    personne2 = Personne(
        nom="Martin",
        prenom="Claire",
        date_naissance=date(1990, 7, 25),
        contact=Contact(
            telephone="0987654321",
            email="claire.martin@example.com"
        ),
        adresse=Adresse(
            adresse="456 Avenue de la République",
            code_postal="69001",
            ville="Lyon"
        )
    )

    return Repertoire(personnes=[personne1, personne2])


# Créer et afficher le répertoire
repertoire = creer_repertoire_exemple()
print(repertoire)
