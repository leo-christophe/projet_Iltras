from setup import main_setup
from gestion_inventaire import ajout_joueur, sauvegardes, get_use, use, afficher_joueur
import time
from histoire_principale import *
from colorama import Fore,Style
from auto import wait_spacebar

from classes import *

def initialisation_jeu():
    """
    Cette fonction permet d'initialiser le jeu. elle retourne 1
    """
    main_setup()
    print("\n > Bienvenue sur Iltras, ce jeu narratif d'un univers de fantasy a été développé initialement lors d'un projet de première par Léo et Evann! \n \n")
    return 1

def debut():
    """Ce programme sert à choisir sa classe de personnage.
    préconditions: le joueur doit choisir une classe avec un numéro allant de 1 à 3.
    postconditions: le programme renvoit un numéro associer à une classe (1,2 ou 3)
    """
    choix_joueur="0"
    while (
        not(int(choix_joueur) in range(0, 8))
    ):
        choix_joueur = input("Il est temps de choisir une classe : \n1-Chevalier \n2-Clypeus \n3-Lutin \n4-Joe Biden \n5-Mario \n6-Shrek \n7-Grand chanceux \n->")
        print("------------------------------------------------")
    return choix_joueur


def choix_nom():
    '''
    Ce programme permet au joueur de choisir son nom d'aventurier/aventurière.
    '''
    choix_nom_joueur = "0xD8xx9x2I92901010001100111101101010100011110011010VOUSAVEZTROUVELESECRETEASTEREGGAHAHNONENFAITECESJUSTEQUEJAIBESOINDEREMPLIRUNGRANDNOMBREDECARACTERESVRAIMENTILYARIENAVOIRAHAHBYE11011011"
    while len(choix_nom_joueur) > 20:
        choix_nom_joueur=input("Quel est ton nom, aventurier/ aventurière ?\
        \n -> ")
        Classes.nom = choix_nom_joueur
        if len(choix_nom_joueur) <= 20:
            time.sleep(0.5)
            print(choix_nom_joueur,"? Quel beau nom. Enchanté!")
            time.sleep(0.7)
            return choix_nom_joueur

        else:
            print(Fore.RED + "⚠️  Il faut que votre nom soit de 20 lettres maximum.")
            print(Style.RESET_ALL)

def classe_choix():
    """
    Ce programme sert à choisir la classe, qui sera définitif. Elle définie les statistiques. 
    """
    print("------------------------------------------------")
    print("Bonjour à toi aventurier, bienvenue dans le monde d'Iltras !")
    print("------------------------------------------------")
    nom=choix_nom()
    print("Maintenant,",nom,", tu dois choisir une classe.")
    print("------------------------------------------------")
    c_c = debut()
    stat = classe_chevalier.get_stats()
    if c_c == "1":
        print("Par la bénédiction de la sainte frite, te voila Chevalier !!!")
        stat = classe_chevalier.get_stats()
    elif c_c == "2":
        print("Mais que voila est-ce un mur,non ça m'a l'air plus dur, voici donc le fameux Clypeus !!")
        stat = classe_bouclier.get_stats()
    elif c_c == "3":
        print("Saperlipopette ! Par la magie des bottes de Merlin ! Enchanté! This is THE Lutin !!")
        stat = classe_lutin.get_stats()
    elif c_c == "4":
        print("Vous voilà maintenant comme le président de l'Amérique (en 2021), enfin, vous n'êtes pas président...!")
        stat = classe_president.get_stats()
    elif c_c == "5":
        print("Yahoo! Mario fait son entrée spétaculaire!")
        stat= classe_mario.get_stats()
    elif c_c == "6":
        print("Shrek? Vraiment? Voilà Shrek!")
        stat= classe_shrek.get_stats()
    elif c_c == "7":
        print("Si tu as de la chance, passe, et si le destin t'est favorable, marche.")
        stat= classe_chanceux.get_stats()
    ajout_joueur(nom, zone=404, vie=stat['vie'], attaque=stat['attaque'], defense=stat['defense'], chance=stat['chance'], argent=stat['argent'], arme="x", armure="x")
    print("------------------------------------------------")
    wait_spacebar()
    histoire_principale_d()

def recup_save():
    liste_choix=afficher_joueur()
    element = liste_choix[choix]

    zone = element[3]
    if zone == 404 or zone == 0:
        return classe_choix()
    elif zone == 1:
        return histoire_principale_d()
    elif zone == 2 or zone == 3:
        return capitale()
    elif zone == 4:
        return grande_foret()
    elif zone == 5:
        return port()
    elif zone == 6:
        return mer()
    elif zone == 7:
        return desert()
    elif zone == 8:
        return jungle()
    elif zone == 9:
        return grotte()
    elif zone == 10:
        return portail_demo()
    elif zone == 11:
        return zone_volca()
    elif zone == 12:
        return boss()


if __name__ == "__main__": 
    initialisation_jeu()
    liste_choix = afficher_joueur()
    choix = sauvegardes()

    ids = [elt[2] for elt in afficher_joueur()]
    use(choix)

    if choix == (len(ids)) or afficher_joueur() == []:
        classe_choix()

    else:
        recup_save()



