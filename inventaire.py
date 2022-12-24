import csv, codecs
from colorama import *
from gestion_inventaire import *

def remove_0(inv):
    for key in inv:
        if inv[key] == 0:
            del inv[key]
            return 1

objets = recup_objet(nom="", all=True)

from colorama import Fore,Style
def affichage_inventaire(inv):
    E = []
    I = [(i['ind'],i['nom']) for i in objets if i['nom'] in inv]
    print("☰☱☲☴☵☱☲☴☵☱☲☴ ◐ INVENTAIRE ◑ ☴☲☱☵☴☲☱☵☴☲☱☰")
    for key,value in inv.items():
        E.append(value)
    sorted(E)
    for i in range(len(list(inv))):
        if I[i][1] in inv:
            if objets[int(I[i][0])]['rar'] == "com":
                print("",i+1,".",list(inv)[i],":",E[i])
            elif objets[int(I[i][0])]['rar'] == "rar":
                print(Fore.LIGHTRED_EX + "",i+1,".",list(inv)[i],":",E[i])
            elif objets[int(I[i][0])]['rar'] == "epi":
                print(Fore.MAGENTA + "",i+1,".",list(inv)[i],":",E[i])
            elif objets[int(I[i][0])]['rar'] == "leg":
                print(Fore.CYAN + "",i+1,".",list(inv)[i],":",E[i])
        print(Style.RESET_ALL)

def affichage_stats(specification,stat,inv,arme,armure):
    print("-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
    print("Vos statistiques :")
    bar="❤︎ ❤︎ ❤︎ ❤︎ ❤︎ ❤︎ ❤︎ ❤︎ ❤︎ ❤︎"
    if int(stat['vie']) >= 0 and int(stat['vie'])<10:
        bar="🖤                                   "
    if int(stat['vie']) >= 10 and int(stat['vie'])<20:
        bar="💓                                   "
    elif int(stat['vie']) >= 20 and int(stat['vie'])<30:
        bar="❤️ ❤️                                "
    elif int(stat['vie']) >= 30 and int(stat['vie'])<40:
        bar="❤️ ❤️ ❤️                             "
    elif int(stat['vie']) >= 40 and int(stat['vie'])<50:
        bar="🧡 🧡 🧡 🧡                          "
    elif int(stat['vie']) >= 50 and int(stat['vie'])<60:
        bar="🧡 🧡 🧡 🧡 🧡                      "
    elif int(stat['vie']) >= 60 and int(stat['vie'])<70:
        bar="💛 💛 💛 💛 💛 💛                   "
    elif int(stat['vie']) >= 70 and int(stat['vie'])<80:
        bar="💛 💛 💛 💛 💛 💛 💛               "
    elif int(stat['vie']) >= 80 and int(stat['vie'])<90:
        bar="💚 💚 💚 💚 💚 💚 💚 💚            "
    elif int(stat['vie']) >= 90 and int(stat['vie'])<100:
        bar="💚 💚 💚 💚 💚 💚 💚 💚 💚        "
    elif int(stat['vie']) == 100:
        bar="💚 💚 💚 💚 💚 💚 💚 💚 💚 💚     "
    bar1 = "defense"
    if int(stat['defense']) >= 0 and int(stat['defense'])<10:
        bar1="🛡️                                    "
    if int(stat['defense']) >= 10 and int(stat['defense'])<20:
        bar1="🛡️                                    "
    elif int(stat['defense']) >= 20 and int(stat['defense'])<30:
        bar1="🛡️ 🛡️                                 "
    elif int(stat['defense']) >= 30 and int(stat['defense'])<40:
        bar1="🛡️ 🛡️ 🛡️                              "
    elif int(stat['defense']) >= 40 and int(stat['defense'])<50:
        bar1="🛡️ 🛡️ 🛡️ 🛡️                           "
    elif int(stat['defense']) == 50:
        bar1="🛡️ 🛡️ 🛡️ 🛡️ 🛡️                        "
    bar2 = ("attaque")
    if int(stat['attaque']) >= 0 and int(stat['attaque'])<10:
        bar2="⚔️                                    "
    if int(stat['attaque']) >= 10 and int(stat['attaque'])<20:
        bar2="⚔️                                    "
    elif int(stat['attaque']) >= 20 and int(stat['attaque'])<30:
        bar2="⚔️ ⚔️                                 "
    elif int(stat['attaque']) >= 30 and int(stat['attaque'])<40:
        bar2="⚔️ ⚔️ ⚔️                             "
    elif int(stat['attaque']) >= 40 and int(stat['attaque'])<50:
        bar2="⚔️ ⚔️ ⚔️ ⚔️                          "
    elif int(stat['attaque']) >= 50:
        bar2="⚔️ ⚔️ ⚔️ ⚔️ ⚔️                       "
    print("Attaque: ",bar2,"| Défense :", bar1)
    bar3 = ("chance")
    if int(stat['chance']) >= 0 and int(stat['chance'])<10:
        bar3="🍀                                     "
    elif int(stat['chance']) >= 10 and int(stat['chance'])<40:
        bar3="🍀 🍀                                  "
    elif int(stat['chance']) >= 40 and int(stat['chance'])<70:
        bar3="🍀 🍀 🍀                               "
    elif int(stat['chance']) >= 70 and int(stat['chance'])<75:
        bar3="🍀 🍀 🍀 🍀                           "
    elif int(stat['chance']) == 75:  
        bar3="🍀 🍀 🍀 🍀 🍀                        "
    print("Vie :", bar,"| Chance: ",bar3)
    affichage_inventaire(inv)
    print("-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")

def check_objet_vie(specification,stat,inv,vie_objet):
    print(Fore.RED)
    print("Vous avez regagné ",vie_objet," nouveaux points de vie.")
    print(Style.RESET_ALL)
    vie_joueur = int(stat['vie'])
    vie_joueur += vie_objet
    if vie_joueur>100:                               #VIE
        vie_joueur=100
        print("Vous êtes au TOP de votre forme!")
    stat['vie'] = vie_joueur

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

from colorama import Fore,Style
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


def jeter(specification,stat,inv,arme,armure):
    if inv != {}:
        P=[]
        for value in inv.items():
            P.append(value)
        affichage_inventaire(inv)
        print("'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
        try:
            ajeter = -1
            while (ajeter < 0):
                try:
                    ajeter = int(input("Que voulez vous jeter? Selectionnez l'objet à supprimer, ou tapez 0 pour revenir en arrière. -> "))
                except ValueError or (ajeter > len(list(inv))+1):
                    print(Fore.RED + "Entrez un nombre correct.")
                    print(Style.RESET_ALL)
            if list(inv)[ajeter-1] in inv:
                if ajeter != 0:
                    nom_choix_j = list(inv)[ajeter-1]
                    initial = inv[nom_choix_j]
                    if nom_choix_j in inv:
                        if inv[nom_choix_j] > 0:
                            nbr=-1
                            while (nbr < 0):
                                try:
                                    nbr = int(input("Combien voulez-vous en jeter? -> "))
                                except ValueError:
                                    print(Fore.RED + "Entrez un nombre correct.")
                                    print(Style.RESET_ALL)
                                    jeter(specification,stat,inv,arme,armure)
                            nbr_0 = initial - inv[nom_choix_j]
                            inv[nom_choix_j] -= nbr
                            if inv[nom_choix_j] <= 0:
                                del inv[nom_choix_j]
                                print("Vous avez supprimé ",initial , nom_choix_j,".")
                            else:
                                print("Vous avez supprimé ",nbr , nom_choix_j,".")
                            jeter(specification,stat,inv,arme,armure)
                        else:
                            print("Vous n'avez pas cet objet.")
                            inventory_main(specification,stat,inv,arme,armure)
                    else:
                    
                        print("Vous n'avez pas cet objet.")
                        inventory_main(specification,stat,inv,arme,armure)
                else:
                    inventory_main(specification,stat,inv,arme,armure)
        except IndexError:
            print(Fore.RED + "Entrez un nombre correct, d'un objet présent dans l'inventaire.")
            print(Style.RESET_ALL)
            jeter(specification,stat,inv,arme,armure)
            
            
    else:
        print("Votre inventaire est vide, vous ne pouvez rien jeter...")
        inventory_main(specification,stat,inv,arme,armure)

def inventory_main(specification,stat,inv):
    affichage_stats(specification,stat,inv)
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
        inventory_equip(specification,stat,inv)
    elif choice == "2":
        enlever(specification,stat,inv)
    elif choice == "3":
        jeter()
    elif choice == "4":
        return "ANNULER"
