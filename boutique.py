from colorama import Fore,Style
from gestion_inventaire import *
from time import sleep

class Boutique():
    liste_complete = [[elt[0] for elt in boutique_recup(i)] for i in range(0,5)]
    stats = elt_save()
    objets = recup_objet(nom=stats[0], all=True)
    inventaire = afficher_inventaire()
    inventaire_classic = afficher_inventaire(classic=True)

def vente(boutique):
    """
    Cette fonction permet de vendre dans n'improte quelle boutique
    """
    if afficher_inventaire(classic=True) == 0:
        print(Fore.RED + "Vous n'avez rien à vendre! " + Style.RESET_ALL)
        return boutique_debut(boutique)

    print("\t << Vous voulez vendre? Compris. Qu'avez-vous donc? >> \n")
    afficher_inventaire(classic=True)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    # Le choix de la vente
    choix_vente = -999
    # Tant qu'un choix n'a pas été fait
    tailleInventaire = len(list(Boutique.inventaire))
    while (choix_vente > tailleInventaire) or (choix_vente < -1 or choix_vente == 0):
        try:
            choix_vente = int(input("Que voulez vous vendre ? \t Choisissez l'objet ou tapez -1 pour annuler. \n-> "))
            
        except ValueError:
            print(Fore.RED + "Entrez un nombre strictement supérieur à 0 ou -1 pour annuler!")
            print(Style.RESET_ALL)

    #! SI LE JOUEUR DECIDE FINALEMENT DE NE RIEN VENDRE
    if choix_vente == -1:
        return boutique_debut(boutique)
    # S'il y a un choix de vente

    if Boutique.inventaire == []:
        print("Vous n'avez aucune objet sur vous!!")
        return vente(boutique)
    else:
        # Si l'inventaire n'est pas vide

        indiceObjetInventaireAVendre = choix_vente - 1
        if Boutique.inventaire[indiceObjetInventaireAVendre] in Boutique.inventaire_classic:
            nom_choix = Boutique.inventaire[indiceObjetInventaireAVendre]

            nomObjets = [S for S in Boutique.objets] #Tableau de tout les noms d'objet de 0 à indice max
            nomObjetAVendre = "0"

            # On retrouve le nom de l'objet à partir de l'indice
            for indiceObjet in range(len(nomObjets)):
                if nomObjets[indiceObjet][1] == nom_choix[1]:
                    nomObjetAVendre = nomObjets[indiceObjet][1]
                    # On sauvegarde le nom de l'objet à vendre
                    indiceObjetSave = indiceObjet
                    # On sauvegarde l'indice de l'objet à vendre dans le tableau d'objets

            if nomObjetAVendre == "0":
                return Exception()

            #! SI L'OBJET N'EST PAS VENDABLE
            if Boutique.objets[indiceObjetSave][18] != 1:
                print("Cet objet n'est pas vendable en boutique...")
                return vente(boutique)

            quantite = 10000
            #! Tant que la quantité que le joueur veut vendre dépasse le nombre d'objet ou que la quantité est négative
            while quantite > Boutique.inventaire[indiceObjetInventaireAVendre][2] or quantite < 0:
                try:
                    quantite = int(input("Combien de cet objet voulez vous vendre ? -> "))
                except ValueError:
                    print("Vous devez entrer un nombre!")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

            # Si la quantité que le joueur veut vendre "existe"
            if (Boutique.inventaire[indiceObjetInventaireAVendre][2] - quantite) >= 0:
                update_inventaire(nomObjetAVendre, -quantite)
                print(quantite, nom_choix, "ont été vendu.")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                update_joueur(argent=(quantite * (int(Boutique.objets[indiceObjetSave][7])-(5/100)*int(Boutique.objets[indiceObjetSave][7]))))
                print("Vous avez maintenant ",Boutique.stats[8]," pièces.")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

                if Boutique.inventaire[indiceObjetInventaireAVendre][2] == 0:
                    delete_elt(nomObjetAVendre)
            
            # Si le joueur essaye de vendre plus que ce qu'il a
            else:
                print("Vous ne pouvez pas vendre plus que ce que vous avez!")
    #! On rappelle la fonction vente
    return vente(boutique)

def boutique_acheter(boutique):
    """
    Cette fonction permet de gérer l'achat de produit dans les boutiques.
    """
    boutique_indice = Boutique.liste_complete[boutique]
    id = get_use()-1
    argentJoueur = afficher_joueur()[id][8]
    
    print("Cela tombe bien je viens de recevoir de nouveaux articles qui vont surement vous plaire !")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Voici ce que vous pouvez acheter :     | Vous avez", argentJoueur, "pièces.")

    for i in range(len(boutique_recup(boutique))):
        print(i+1," - ",boutique_recup(boutique)[i][1], " : ", boutique_recup(boutique)[i][7]," pièces l'unité.")  #objet[7] correspond à la valeur de l'objet
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    choix_acheter = -500
    # Tant que le choix de l'achat n'est pas valide
    while choix_acheter < -1 or choix_acheter == 0 or choix_acheter > len(boutique_recup(boutique)):
        try :
            choix_acheter = int(input("Que voulez vous acheter? (Entrez le numéro correspondant ou tapez -1 pour revenir en arrière) ->"))
        except ValueError or (choix_acheter > len(boutique_recup(boutique)) or choix_acheter < -1):
            print(Fore.RED + "Veuillez entrer le nombre d'un des produits présent dans la boutique.")
            print(Style.RESET_ALL)
    if choix_acheter == -1:
        boutique_debut(boutique)
        return -1    
    indice = int(boutique_indice[choix_acheter-1])
    print("\n ||| Choix :", Boutique.objets[indice][1]  + "\t Prix à l'unité:",(Boutique.objets[indice][7])," pièces |||")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    valeur_indice = (Boutique.objets[indice][7])
    choix_nom = (Boutique.objets[indice][1])

    achetes = -5
    #! CONFIRMATION ACHAT
    # CELA VERIFIE SI LE JOUEUR VEUT BIEN ACHETER LE PRODUIT
    while ((achetes != 1) or (achetes != 2)):
        try:
            achetes=int(input("Voulez vous vraiment acheter ceci ? \n1: OUI \n2: NON\n-> "))
            if ((achetes == 1) or (achetes == 2)):
                break
        except ValueError:
            print(Fore.RED + "Tapez 1 ou 2 uniquement!")
            print(Style.RESET_ALL)

    # SI LE JOUEUR VEUT BIEN ACHETER LE PRODUIT
    if achetes == 1:
        #! CHOIX QUANTITE
        # ON DEMANDE LA QUANTITE A ACHETER
        choix_fait_quantite = -1
        #? La variable vérifiant que le choix a été fait

        while choix_fait_quantite == -1:
            quantiteAchetee = -5
            #? La quantité achetée

            while quantiteAchetee < 0:
                try:
                    quantiteAchetee = int(input("Combien de cet objet voulez vous acheter ? -> "))
                except ValueError:
                    print(Fore.RED + "Tapez un nombre au dessus ou égal à 0!")
                    print(Style.RESET_ALL)

            # SI LA QUANTITE ACHETEE DEMANDE EST DE 0, ON NE FAIT RIEN.
            if quantiteAchetee == 0:
                choix_fait_quantite = 1

            # SI LA QUANTITE EST SUPERIEURE A 0, ON VERIFIE QUE LE JOUEUR A L'ARGENT, S'IL L'A ON LUI DONNE
            elif argentJoueur >= (int(valeur_indice)*quantiteAchetee):
                # On enlève l'argent au joueur
                update_joueur(argent= -(int(valeur_indice)*quantiteAchetee))

                # On ajoute l'objet dans l'inventaire du joueur
                if Boutique.inventaire == 0:
                    ajouter_inventaire(choix_nom, quantiteAchetee)
                elif choix_nom in Boutique.inventaire:
                    update_inventaire(choix_nom, quantiteAchetee)
                else:
                    ajouter_inventaire(choix_nom, quantiteAchetee)

                #? On redéfinit argentJoueur après avoir enlever l'argent
                argentJoueur = afficher_joueur()[id][8]
                # Affichages
                print("Votre inventaire :", Boutique.inventaire)
                print("Votre monnaie restante:", argentJoueur)
                    
                choix_fait_quantite = 1
            else:
                print("Vous n'avez pas assez de monnaie pour acheter ",quantiteAchetee, choix_nom)
                choix_fait_quantite = -1

    #! SI LE JOUEUR NE VEUT PAS ACHETER LE PRODUIT
    elif achetes == 2:
        print("Alors que faites vous ici?! Vous achetez quelque chose ou vous vous en allez, vous faites fuir les clients.")
        sleep(1.2)
    return boutique_debut(boutique)
        

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
        inventory_main()
        boutique_debut(boutique)
    return -1
boutique_debut(0)

