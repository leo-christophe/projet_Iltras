from colorama import *
from gestion_inventaire import *

def remove_0(inv):
    for key in inv:
        if inv[key] == 0:
            del inv[key]
            return 1

objets = recup_objet(nom="", all=True)

def affichage_inventaire():
    """
    Cette fonction permet d'afficher chaque objet de l'inventaire selon la rareté
    """
    if afficher_inventaire() != 0:

        listeObjets = objets
        inventaireJoueur = sorted(afficher_inventaire())

        idObjetsInventaireJoueur = []
        for i in range(len(inventaireJoueur)):
            for j in range(len(listeObjets)):
                if inventaireJoueur[i][1] == listeObjets[j][1]:
                    idObjetsInventaireJoueur += [listeObjets[j][0]]    
        print(idObjetsInventaireJoueur)

    else:
        print("Vous n'avez rien dans votre inventaire!")
        return 0

    listeObjets = objets

    rareteObjets = [listeObjets[idObjetsInventaireJoueur[i]][2] for i in range(len(inventaireJoueur))]
    print("☰☱☲☴☵☱☲☴☵☱☲☴ ◐ INVENTAIRE ◑ ☴☲☱☵☴☲☱☵☴☲☱☰")

    for i in range(len(inventaireJoueur)):
        nomObjet = inventaireJoueur[i][1]
        quantiteObjet = inventaireJoueur[i][2]

        if rareteObjets[i] == "rar":
            print(Fore.LIGHTRED_EX)
        elif rareteObjets[i] == "epi":
            print(Fore.MAGENTA)
        elif rareteObjets[i] == "leg":
            print(Fore.CYAN)
        print("",i+1,".",nomObjet,":",quantiteObjet)
        print(Style.RESET_ALL)
        
    print(Style.RESET_ALL)

def affichage_stats():
    statsJoueur = afficher_joueur()[get_use()-1]

    # LA VIE
    if 0 < statsJoueur[4] < 10:
        barVie="🖤                                   "
    elif 10 <= statsJoueur[4] < 20:
        barVie="💓                                   "
    elif 20 <= statsJoueur[4] < 30:
        barVie="❤️ ❤️                                "
    elif 30 <= statsJoueur[4] < 40:
        barVie="❤️ ❤️ ❤️                             "
    elif 40 <= statsJoueur[4] < 50:
        barVie="🧡 🧡 🧡 🧡                          "
    elif 50 <= statsJoueur[4] < 60:
        barVie="🧡 🧡 🧡 🧡 🧡                      "
    elif 60 <= statsJoueur[4] < 70:
        barVie="💛 💛 💛 💛 💛 💛                   "
    elif 70 <= statsJoueur[4] < 80:
        barVie="💛 💛 💛 💛 💛 💛 💛               "
    elif 80 <= statsJoueur[4] < 90:
        barVie="💚 💚 💚 💚 💚 💚 💚 💚            "
    elif 90 <= statsJoueur[4] < 100:
        barVie="💚 💚 💚 💚 💚 💚 💚 💚 💚        "
    else:
        barVie="💚 💚 💚 💚 💚 💚 💚 💚 💚 💚     "

    # LA DEFENSE
    if 0 <= statsJoueur[6] < 10:
        barDefense="🛡️                                    "
    elif 10 >= statsJoueur[6] > 20:
        barDefense="🛡️                                    "
    elif 20 >= statsJoueur[6] > 30:
        barDefense="🛡️ 🛡️                                 "
    elif 30 >= statsJoueur[6] > 40:
        barDefense="🛡️ 🛡️ 🛡️                              "
    elif 40 >= statsJoueur[6] > 50:
        barDefense="🛡️ 🛡️ 🛡️ 🛡️                           "
    else:
        barDefense="🛡️ 🛡️ 🛡️ 🛡️ 🛡️                        "

    # L'ATTAQUE
    if 0 <= statsJoueur[5] < 10:
        barAttaque="⚔️                                    "
    elif 10 <= statsJoueur[5] < 20:
        barAttaque="⚔️                                    "
    elif 20 <= statsJoueur[5] < 30:
        barAttaque="⚔️ ⚔️                                 "
    elif 30 <= statsJoueur[5] < 40:
        barAttaque="⚔️ ⚔️ ⚔️                             "
    elif 40 <= statsJoueur[5] < 50:
        barAttaque="⚔️ ⚔️ ⚔️ ⚔️                          "
    else:
        barAttaque="⚔️ ⚔️ ⚔️ ⚔️ ⚔️                       "

    # LA CHANCE
    if 0 <= statsJoueur[7] < 10:
        barChance="🍀                                     "
    elif 10 <= statsJoueur[7] < 40:
        barChance="🍀 🍀                                  "
    elif 40 <= statsJoueur[7] < 70:
        barChance="🍀 🍀 🍀                               "
    elif 70 <= statsJoueur[7] < 75:
        barChance="🍀 🍀 🍀 🍀                           "
    elif statsJoueur[7] >= 75:  
        barChance="🍀 🍀 🍀 🍀 🍀                        "

    print("-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
    print("Vos statistiques :")
    print("Attaque: ",barAttaque,f"({statsJoueur[5]})\t | Défense :", barDefense,f"({statsJoueur[6]})")
    print("Vie :", barVie,f"({statsJoueur[4]})\t | Chance: ",barChance,f"({statsJoueur[7]})")
    
    affichage_inventaire()
    
    print("-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")

def check_objet_vie(vieObjet):

    
    update_joueur(vie=vieObjet)

    if afficher_joueur()[get_use()-1][4] > 100:                               #VIE
        update_joueur(vie = afficher_joueur[get_use()-1][4]) - (afficher_joueur[get_use()-1][4] - 100)
        print("Vous êtes au TOP de votre forme!")

    print(Fore.RED)
    print("Vous avez regagné ",vieObjet," nouveaux points de vie.")
    print(Style.RESET_ALL)


def check_objet_chance(specification,stat,inv,chance):
    print("Vous avez obtenu ",chance," nouveaux points de chance.")
    chance_joueur = int(stat['chance'])
    chance_joueur += chance    
    if specification == "notweaponry":                                 #CHANCE
        if chance_joueur > 75:
            chance_joueur = 75
            print("Le plafond de 75 points de chance (sans armes ou armures) a été atteint...!")
    stat['chance'] = chance_joueur

def inventory_equip(specification,stat,inv,arme,armure):    
    affichage_inventaire(inv)
    print("'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
    if inv != {}:
        print("Que voulez vous utiliser ?")
        choix_inventaire=-2
        while (choix_inventaire < -1) and (choix_inventaire) != 0: 
            try:
                choix_inventaire = int(input("Choisissez un objet de votre inventaire ou tapez -1 pour revenir en arrière... -> "))
            except ValueError:
                print(Fore.RED + "Vous devez entrer un nombre valide!")
                print(Style.RESET_ALL)
        try:
            if choix_inventaire == -1:
                inventory_main(specification,stat,inv,arme,armure)
                return 0
            elif choix_inventaire == 0:
                print(Fore.RED + "Il n'y a pas de numéro 0 dans votre inventaire...")
                print(Style.RESET_ALL)
                inventory_equip(specification,stat,inv,arme,armure)
                return 0
            print("'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
            T=[S["nom"] for S in objets] #Tableau de tout les noms d'objet de 0 à indice max
            nom_choix = list(inv)[choix_inventaire-1]
            objet_utilise="0"
            for e in range(len(T)):
                if T[e] == nom_choix:
                    objets[e]["nom"] = objet_utilise
                    i = e
            vie_objet = int(objets[i]['vie']) #Si cet objet peut soigner...
            chance = int(objets[i]['chance']) #Si cet objet peut augmenter la chance
            attaque_supp = int(objets[i]['att'])
            defenseplus = int(objets[i]['def'])
            if inv[nom_choix] > 0:
                if nom_choix in inv:
                    if (vie_objet != 0) and (chance != 0) and (attaque_supp == 0) and (defenseplus == 0):
                        check_objet_chance("notweaponry",stat,inv,chance)
                        check_objet_vie(specification,stat,inv,vie_objet)
                    elif chance != 0 and (attaque_supp == 0) and (defenseplus == 0):
                        check_objet_chance("notweaponry",stat,inv,chance)
                    elif vie_objet != 0 and (attaque_supp == 0) and (defenseplus == 0):
                        check_objet_vie(specification,stat,inv,vie_objet)
                    ######################################################################
                    elif ((attaque_supp != 0) and (objets[i]["typ"] == "arme")):
                        if arme == []:
                            print("Vous avez équipé ",nom_choix," ce qui vous apporte un bonus d'attaque de ", attaque_supp, " points.")
                            attaque_joueur = int(stat['attaque'])                       #ATTAQUE
                            attaque_joueur += attaque_supp
                            arme = [i,nom_choix]
                            stat['attaque'] = attaque_joueur
                            if (defenseplus != 0):
                                print("Cette même arme vous apporte aussi un bonus de ", defenseplus," points de défense...")
                                defense_joueur = int(stat['defense'])                       #DEFENSE
                                defense_joueur += defenseplus
                                if defense_joueur > 50:
                                    defense_joueur = 50
                                    print("Vous ne pouvez plus rien porter sur vous, vous vous sentez très lourd (vous avez atteint le plafond de 50 points de défense)")
                                stat['defense'] = defense_joueur
                            elif (vie_objet != 0) and (chance != 0):
                                check_objet_chance(specification,stat,inv,chance)
                                check_objet_vie(specification,stat,inv,vie_objet)
                            elif chance != 0:
                                check_objet_chance(specification,stat,inv,chance)
                            elif vie_objet != 0:
                                check_objet_vie(specification,stat,inv,vie_objet)
                        else:
                            print("Vous avez déjà une arme d'équipée.")
                            inventory_main(specification,stat,inv,arme,armure)
                    ######################################################################
                    elif ((defenseplus != 0) and (objets[i]["typ"] == "armure")):
                        if armure == []:
                            print("Vous avez équipé ",nom_choix," ce qui vous apporte un bonus de défense de ", defenseplus," points.")
                            defense_joueur = int(stat['defense'])                       #DEFENSE
                            defense_joueur += defenseplus
                            if defense_joueur > 50:
                                defense_joueur = 50
                                print("Vous ne pouvez plus rien porter sur vous, vous vous sentez très lourd (vous avez atteint le plafond de 50 points de défense)")
                            armure = [i,nom_choix]
                            stat['defense'] = defense_joueur
                            if (attaque_supp != 0):
                                print("Cette armure vous procure aussi un bonus de ", attaque_supp, "points d'attaque.")
                                attaque_joueur = int(stat['attaque'])                       #ATTAQUE
                                attaque_joueur += attaque_supp
                                stat['attaque'] = attaque_joueur
                            elif (vie_objet != 0) and (chance != 0):
                                check_objet_chance(specification,stat,inv,chance)
                                check_objet_vie(specification,stat,inv,vie_objet)
                            elif chance != 0:
                                check_objet_chance(specification,stat,inv,chance)
                            elif vie_objet != 0:
                                check_objet_vie(specification,stat,inv,vie_objet)
                        else:
                            print("Vous portez déjà quelque chose...")
                            inventory_main(specification,stat,inv,arme,armure)
                    #######################################################################
                    print(Fore.RED + nom_choix," a été utilisé.")
                    print(Style.RESET_ALL)
                    if inv[nom_choix] == 1:
                        del inv[nom_choix]
                    elif inv[nom_choix] > 1:
                        inv[nom_choix] -= 1                                        #UTILISATION ET REMOVAL
                    inventory_main(specification,stat,inv,arme,armure)
                else:
                    print("Cet objet n'est pas disponible...")
            else:
                print("Vous n'avez pas cet objet..")
        except IndexError or KeyError:
            print(Fore.RED + "Veuillez entrer le numéro d'un objet présent dans l'inventaire...")
            print(Style.RESET_ALL)
            inventory_equip("0",stat,inv,arme,armure)
            return 0
    elif inv == {}:
        print("Votre inventaire est vide... Vous ne pouvez rien faire.")

def objet_chanceux(stat,ind):
    if int(objets[ind]['chance']) != 0:
        pv_plr = int(stat['chance'])
        pv_plr -= int(objets[ind]['chance'])
        stat['chance'] = pv_plr
        print("Au passage, vous perdez ",int(objets[ind]['chance'])," points de chance rabaissant ces derniers à ", stat['chance'],".")


def enlever(specification,stat,inv,arme,armure):
    try:
        if (arme != []) or (armure != []):
            print(Fore.YELLOW + "Tapez -1 pour revenir en arrière")
            print(Style.RESET_ALL)
            if arme != []:
                print(Fore.RED + "1) Votre arme : ",arme[1])
                print(Style.RESET_ALL)
            else:
                print("Vous ne portez aucune arme.")
            if armure != []:
                print(Fore.RED + "2) Votre portez : ", armure[1])
                print(Style.RESET_ALL)
            else:
                print("Vous ne portez aucune armure.")
            choix_enlev = "0"
            while ((choix_enlev != "-1") and (choix_enlev != "1") and (choix_enlev != "2")):
                choix_enlev = input("Que décidez vous d'enlever ? -> ")
            if choix_enlev == "-1":
                print("Vous changez d'avis et gardez vos équipements sur vous.")
                inventory_main(specification,stat,inv,arme,armure)
            elif choix_enlev == "1":
                if arme != []:
                    arme_indice = arme[0]
                    attaque_du_joueur = int(stat['attaque'])
                    attaque_du_joueur -= int(objets[arme_indice]['att'])
                    stat['attaque'] = attaque_du_joueur
                    if int(objets[arme_indice]['def']) != 0:
                        defense_du_joueur = int(stat['defense'])
                        defense_du_joueur -= int(objets[arme_indice]['def'])
                        stat['defense'] = defense_du_joueur
                        print("En remettant votre arme dans votre sac à dos, vous perdez ", objets[arme_indice]['att'], " points d'attaque rabaissant ces derniers à ", stat['attaque'],"et vous perdez", objets[arme_indice]['def'],
                        "rabaissant ces derniers à ", stat['defense'],".")
                    else:
                        print("En remettant votre arme dans votre sac à dos, vous perdez ", objets[arme_indice]['att'], " points d'attaque rabaissant ces derniers à ", stat['attaque'],".")
                    objet_chanceux(stat,arme_indice)
                    if inv[arme[1]] > 0:
                        inv[arme[1]] += 1
                    elif inv[arme[1]] == 0:
                        inv[arme[1]] = 1
                    arme = []
                    inventory_main(specification,stat,inv,arme,armure)
                else:
                    print("Vous n'avez pas d'arme équipée...")
                    enlever(specification,stat,inv,arme,armure)
            elif choix_enlev == "2":
                if armure != []:
                    armure_indice = armure[0]
                    defense_du_joueur = int(stat['defense'])
                    defense_du_joueur -= int(objets[armure_indice]['def'])
                    stat['defense'] = defense_du_joueur
                    if int(objets[armure_indice]['att']) != 0:
                        attaque_du_joueur = int(stat['attaque'])
                        attaque_du_joueur -= int(objets[armure_indice]['att'])
                        stat['attaque'] = attaque_du_joueur
                        print("En remettant ce que vous portiez dans votre sac à dos, vous perdez ", objets[armure_indice]['def'], " points d'attaque rabaissant ces derniers à ", stat['defense'],"et vous perdez", objets[armure_indice]['att'],
                        "rabaissant ces derniers à ", stat['attaque'],".")
                    else:
                        print("En remettant ce que vous portiez dans votre sac à dos, vous perdez ", objets[armure_indice]['def']," points de défense rabaissant ces derniers à ", stat['defense'],".")
                    objet_chanceux(stat,armure_indice)
                    if armure[1] in inv:
                        inv[armure[1]] += 1
                    else:
                        inv[armure[1]] = 1
                    armure = []
                    inventory_main(specification,stat,inv,arme,armure)
                else:
                    print("Vous n'avez pas d'armure équipée...")
                    enlever(specification,stat,inv,arme,armure)
        else:
            print(Fore.RED + "Vous n'avez rien d'équipé!!!")
            print(Style.RESET_ALL)
            inventory_main(specification,stat,inv,arme,armure)
    except KeyError or ValueError:
        print(Fore.RED + "Une erreur est survenue... Choisissez un nombre entre 1 et 2 ou tapez -1 pour revenir en arrière.")
        print(Style.RESET_ALL)
        inventory_main(specification,stat,inv,arme,armure)


def jeter():
    """
    Cette fonction permet de jeter des objets.
    """
    inventaireJoueur = afficher_inventaire()
    
    if inventaireJoueur == 0:
        print("Il n'y a plus rien à jeter! \n'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
        return 0
    
    ajeter = -1
    while (ajeter < 0 or ajeter >= len(inventaireJoueur)):
        try:
            ajeter = int(input("Que voulez vous jeter? Selectionnez l'objet à supprimer, ou tapez 0 pour revenir en arrière. -> "))
        except ValueError:
            print(Fore.RED + "Entrez un nombre correct." + Style.RESET_ALL)

        if ajeter != 0:
            quantiteInitial = inventaireJoueur[ajeter-1][2]
                
            nbr=-1
            #tant que le nombre choisi n'est pas valide (pas dans l'inventaire)
            while (nbr < 0 or nbr > quantiteInitial):
                try:
                    nbr = int(input("Combien voulez-vous en jeter? -> "))
                except ValueError:
                    print(Fore.RED + "Entrez un nombre correct." + Style.RESET_ALL)

            #on enlève ce que le joueur veut jeter
            update_inventaire(nom=inventaireJoueur[ajeter-1][1], quantite=-nbr)

            print("Vous avez supprimé ",quantiteInitial , inventaireJoueur[ajeter-1][1],".")
            #on redemande
            return jeter()
        
        # revenir en arrière
        return inventory_main()

def inventory_main():
    """
    Cette fonction gère l'inventaire tout entier.
    """
    affichage_stats()
    print("ACTIONS :")
    print("\t 1. ÉQUIPER / UTILISER")
    print("\t 2. ENLEVER (ARME/ARMURE)")
    print("\t 3. JETER")
    print("\t 4. ANNULER")
    print("-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
    choice = "0"
    while ((choice != "1") and (choice != "2") and (choice !="3") and (choice != "4")):
        choice = input("Que voulez-vous faire? -> ")
    if choice == "1":
        return inventory_equip()
    elif choice == "2":
        return enlever()
    elif choice == "3":
        print("jeter")
        return jeter()

    elif choice == "4":
        return "ANNULER"
