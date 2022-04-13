class Classes:
    """
    Cette classe gère les classes du jeu.
    """

    nom = None

    def __init__(self, classe, attaque, defense=0, chance=1, argent=0, vie=100):
        self.vie_joueur = vie
        self.attaque_joueur = attaque
        self.defense_joueur = defense
        self.chance_joueur = chance
        self.argent_joueur = argent
        self.nom_classe = classe

    def get_stats(self):
        return {"vie":self.vie_joueur,"attaque":self.attaque_joueur,"defense":self.defense_joueur,"chance":self.chance_joueur,"argent":self.argent_joueur}

    stats = property(get_stats,doc="Les stats peuvent être modifiées à partir de cette propriétée.")

classe_chevalier = Classes("Chevalier",attaque=6,defense=5,chance=5,argent=200)
classe_bouclier = Classes("Clypeus",attaque=3, defense=15, chance= 7, argent=150)
classe_lutin = Classes("Lutin",attaque=1,defense=3,chance=50,argent=350)
classe_president = Classes("JoeBiden",attaque=1,defense=2,chance=20,argent=300,vie=50)
classe_mario = Classes("Mario",attaque=10,defense=0,chance=0,argent=200)
classe_shrek = Classes("Shrek",attaque=6,defense=13,chance=0,argent=3)
classe_chanceux = Classes("Chanceux",attaque=2,defense=1,chance=75,argent=270)

