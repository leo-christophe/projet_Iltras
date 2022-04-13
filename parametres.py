"""
def pars():

    temps_attente = "automatique"
    temps_attente = Parametres.temps_attente
    while temps_attente != "automatique" and temps_attente != "manuel":
        temps_attente = Parametres.temps_attente
    

    difficultee = 2
    difficultee = Parametres.difficultee
    while difficultee != 1 and difficultee != 2 and difficultee != 3:
        difficultee = Parametres.difficultee
        
class Parametres:
    \"""
    \Cette classe permet de personnaliser les paramètres du jeu.
    \"""
    temps_attente = input("-> Pour le défilement de l'histoire, voulez-vous que ce soit automatique ou manuel ? \n \
        Si c'est automatique, il va y avoir un temps d'attente de 0.5s à 4s entre chaque ''partie d'histoire'' \n \
        Mais si c'est manuel, vous devrez appuyer sur votre barre d'espace pour passer au prochain ''dialogue''.")

    difficultee = int(input("-> Selectionnez une difficultée entre 1 et 3"))

"""