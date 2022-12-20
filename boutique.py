import csv
import codecs
from colorama import Fore,Style,Back
from gestion_inventaire import *

def boutique_recup(boutique):
    conn = creer_connexion(DB_FILE + ".db")

    cur = conn.cursor()
    cur.execute(
    f"""
    SELECT * FROM Objets
    WHERE boutique = {boutique}
    ORDER BY ind
    """
    )
    liste = cur.fetchall()
    conn.close()
    return liste  

liste_complete = [[elt[0] for elt in boutique_recup(i)] for i in range(0,5)]



stats = elt_save()

objets = recup_objet(nom=stats[0], all=True)
inventaire = afficher_inventaire()
inventaire_classic = afficher_inventaire(classic=True)

 

def boutique_main():
    achetable_0=[elt[0] for elt in recup_objet(nom=None, all=True) if elt[17] == 0]
    return achetable_0

def vente(boutique):
    afficher_inventaire(classic=True)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    choix_vente = -999
    while (choix_vente > len(list(inventaire)) or choix_vente <= 0):
        try:
            choix_vente = int(input("Que voulez vous vendre ? | Choisissez l'objet ou tapez -1 pour annuler. -> "))
            break
        except ValueError:
            print(Fore.RED + "Vous devez entrer un nombre!")
    if choix_vente == -1:
        boutique_debut(boutique)
    else:
        if inventaire != []:
            if inventaire[choix_vente-1] in inventaire_classic:
                nom_choix = inventaire[choix_vente-1]
                T=[S for S in objets] #Tableau de tout les noms d'objet de 0 à indice max
                objet_utilise="0"
                for e in range(len(T)):
                    if T[e][1] == nom_choix[1]:
                        T[e][1]= objet_utilise
                        i = e #L'indice i de l'objet
                        if objets[i]['vendable'] == "1":
                            quantitee = 10000
                            while ((quantitee > inventaire[nom_choix]) or (quantitee < 0)):
                                try:
                                    quantitee = int(input("Combien de cet objet voulez vous vendre ? -> "))
                                except ValueError:
                                    print("Vous devez entrer un nombre!")
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                            if quantitee > 0:
                                if nom_choix in inventaire:
                                    if (inventaire[nom_choix] - quantitee) >= 0:
                                        inventaire[nom_choix] -= quantitee
                                        print(quantitee, nom_choix, "ont été vendu.")
                                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                        update_joueur(argent=(quantitee * (int(objets[i]['valeur'])-(5/100)*int(objets[i]['valeur']))))
                                        stat_raw = elt_save()
                                        print("Vous avez maintenant ",stat_raw[8]," pièces.")
                                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                        if inventaire[nom_choix] == 0:
                                            del inventaire[nom_choix]
                                        vente(boutique)
                                    else:
                                        print("Vous ne pouvez pas vendre plus que ce que vous avez!")
                                        vente(boutique)
                                else:
                                    print("L'objet que vous voulez vendre n'est pas en votre possession...")
                                    boutique_debut(boutique)
                            else:
                                print("Vous ne pouvez pas vendre un nombre négatif d'objets, ou 0 objet!")
                                boutique_debut(boutique)
                        else:
                            print("Cet objet n'est pas vendable en boutique...")
                            vente(boutique)
        else:
            print("Vous n'avez aucun objet sur vous...")
            boutique_debut(boutique)

def boutique_acheter(boutique):
        boutique_indice = liste_complete[boutique]
        
        print("Cela tombe bien je viens de recevoir de nouveaux articles qui vont surement vous plaire !")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        id = get_use()
        print("Voici ce que vous pouvez acheter :     | Vous avez",afficher_joueur()[id-1][8],"pièces.")

        for i in range(len(boutique_recup(boutique))):
            print(i+1," - ",boutique_recup(boutique)[i][1], " : ", boutique_recup(boutique)[i][7]," pièces l'unité.")  #objet[7] correspond à la valeur de l'objet
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

        
        choix_acheter = -500
        while choix_acheter < -1 or choix_acheter == 0 or choix_acheter > len(boutique_recup(boutique)):
            try :
                choix_acheter = int(input("Que voulez vous acheter? (Entrez le numéro correspondant ou tapez -1 pour revenir en arrière) ->"))
            except ValueError or (choix_acheter > len(boutique_recup(boutique)) or choix_acheter < -1):
                print(Fore.RED + "Veuillez entrer le nombre d'un des produits présent dans la boutique.")
                print(Style.RESET_ALL)
        if choix_acheter == -1:
            boutique_debut(boutique)
            return -1    
        print(boutique_indice)
        indice = int(boutique_indice[choix_acheter-1])
        print("Choix :", objets[indice][1])
        valeur_indice = (objets[indice][7])
        print("Prix à l'unité:",(objets[indice][7])," pièces ")
        choix_nom = (objets[indice][1])
        achetes = -5
        while ((achetes != 1) or (achetes != 2)):
            try:
                achetes=int(input("Voulez vous vraiment acheter ceci ? \n1: OUI \n2: NON\n-> "))
                if ((achetes == 1) or (achetes == 2)):
                    break
            except ValueError:
                print(Fore.RED + "Tapez 1 ou 2 uniquement!")
                print(Style.RESET_ALL)
        if achetes == 1:
            choix_fait_quantitee = -1
            while choix_fait_quantitee == -1:
                quantitee_ac = -5
                while quantitee_ac < 0:
                    try:
                        quantitee_ac = int(input("Combien de cet objet voulez vous acheter ? -> "))
                    except ValueError:
                        print(Fore.RED + "Tapez un nombre au dessus ou égal à 0!")
                        print(Style.RESET_ALL)
                

                if quantitee_ac == 0:
                    choix_fait_quantitee = 1

                elif afficher_joueur()[get_use()-1][8] >= (int(valeur_indice)*quantitee_ac):
                    update_joueur(argent= -(int(valeur_indice)*quantitee_ac))
                    if choix_nom in inventaire:
                        ajouter_inventaire(choix_nom, 1)
                        choix_fait_quantitee = 1
                    else:
                        if quantitee_ac >0:
                            update_inventaire(choix_nom, quantitee_ac)
                        print("Votre inventaire :", inventaire)
                        print("Votre monnaie restante:", afficher_joueur()[get_use()-1][8])
                        choix_fait_quantitee = 1
                else:
                    print("Vous n'avez pas assez de monnaie pour acheter ",quantitee_ac, choix_nom)
                    choix_fait_quantitee = -1
            boutique_debut(boutique)
        elif achetes == 2:
            print("Alors que faites vous ici?! Vous achetez quelque chose ou vous vous en allez, vous faites fuir les clients.")
            boutique_debut(boutique) 
            choix_fait=1

from inventaire import inventory_main
def boutique_debut(boutique):

    if boutique == 0:
        greetings = "Bonjour, je vous souhaite la bienvenue dans ma modeste auberge, John à votre service! "
        goodbye = "Un vent de changement souffle, je le sens arriver."
    elif boutique == 1:
        greetings = "Bien le bonjour aventurier! Et bienvenue à la plus grande boutique de la capitale! Prenez le temps de décider ce que vous voulez faire et revenez à moi!"
        goodbye = "Bonne chance, dehors, les temps sont durs!"
    elif boutique ==2:
        greetings = "Hééé! Oohhh! YYYAARGHHH Jeune mousse, que m'veux tu? "
        goodbye = "Bonne chance sur les mers déchaînés YAAARGHHHH!"
    elif boutique  == 3:
        greetings = "Bonsoir, je serai votre vendeur pour aujourd'hui, vous pouvez m'appeler Rambo."
        goodbye = "Faites attention, la jungle peut s'avérer très dangereuse!"
    elif boutique == 4:
        greetings = "HEYYY, T'AS PAS UN PEU TROP CHAUD? T'AIMERAIS QUOI?"
        goodbye = "A BIENTÔT, SI TU NE FINIS PAS GRILLÉ D'ICI LA AHAHAHAHAHAHAHAH"

    
    
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(greetings)

    # CHOIX DE L'ACTION
    # On demande ce que le joueur veut faire en entrant dans la boutique.
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Comment pourrais-je vous aider ?")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("1. ACHETER")
    print("2. VENDRE")
    print("3. PARTIR")
    print("4. INVENTAIRE ")
    choix_march = 0
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    while ((choix_march) !=1) and ((choix_march)!=2) and ((choix_march) != 3) and ((choix_march != 4)):
        try:
            choix_march=int(input("Bon j'ai une livraison qui m'attend. Que puis-je faire pour vous ? 1- Acheter 2- Vendre 3- Partir 4- Inventaire ->"))
        except ValueError:
            print(Fore.RED + "Tapez 1,2,3 ou 4!!!")
            print(Style.RESET_ALL)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    # CHOIX : ACHETER
    if choix_march == 1:
        boutique_acheter(boutique)
    # CHOIX : VENDRE
    elif choix_march == 2:
        vente(boutique)
    # CHOIX : PARTIR
    elif choix_march == 3:
        print(goodbye)
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        return -1
    # CHOIX : REGARDER INVENTAIRE
    elif choix_march == 4:  
        inventory_main(0,inventaire)
        boutique_debut(boutique,inventaire)
    return -1
boutique_debut(0)

