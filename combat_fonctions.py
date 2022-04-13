

from gestion_inventaire import *
from random import randint, shuffle
from colorama import Style, Fore
import time

inv = afficher_inventaire()
stat_raw = elt_save()

ennemi_liste = recup_monstre("nom",all=True)



DB_FILE = "assets"



def apparition(zone):
    """
    Cette fonction permet de selectionner le monstre adéquat à la zone / progression du joueur tout en prenant compte de sa raretée

    Pré-conditions : L'indice des monstres de la zone adéquate est cherchée.

    Post-condition : Est retourné le monstre selectionné, plus précisemment son indice.
    """
    monstres = recup_monstre("n", all=True) #789
    zone_liste=[
        [int(monstres[e][0]) for e in monstres if (int(monstres[e][7])) == (zone)]+
        [int(monstres[e][0]) for e in monstres if (int(monstres[e][8])) == (zone)]+
        [int(monstres[e][0]) for e in monstres if (int(monstres[e][9])) == (zone)]+
        [int(monstres[e][0]) for e in monstres if (int(monstres[e][9])) == 999]
        ]
    shuffle(zone_liste) #zone est trié aléatoirement 
    for e in range(len(zone_liste)-1):
        if int(monstres[int(zone_liste[e])]["rar"]) > randint(0,100):
            choix = int(zone_liste[e])
            return choix



def specifique(indice, vie_ennemi):
    ennemi_combat.indice = indice
    ennemi_combat.vie = vie_ennemi
    main()

def main():
    if stat_raw[4] > 0:
        if ennemi_combat.vie > 0:
            if ennemi_combat.tour == 0:
                print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                arrivee = (ennemi_liste[ennemi_combat.indice][16])
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")    
            print("Que Faire ?")
            print("1. ATTAQUER")
            print("2. FUIR")
            print("3. SE CACHER")
            print("4. INVENTAIRE")
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
            input_done = 0
            while ((input_done != "1") and (input_done != "2") and (input_done != "3") and (input_done != "4")) :
                input_done = input("Faites un choix ! -> ")
                if input_done == "1":
                    attaque()
                elif input_done == "2":
                    fuir()
                elif input_done == "3":
                    cache()
                elif input_done == "4":
                    afficher_inventaire(classic=True)
        else:
            return fin_combat_reussite()

    else:
        return fin_combat_defaite()


def attaque():
    """
    Cette fonction calcule les points d'attaque que le joueur va infliger à l'ennemi au tour "ATTAQUER".
    """
    point_attaque = int(stat_raw[5])

    chance = int(stat_raw[7])
    att_final = round(point_attaque + chance/16.25,2)
    
    malchanceux = False
    couprate = 0 ##############MALCHANCE
    if chance < 0:
        malchance = randint(0,100)+chance
        if malchance <= 42:
            couprate = round(randint(1,int(stat_raw[5])),1)
            malchanceux = True

    if malchanceux == True:
        att_final -= couprate
        print(Fore.GREEN + "Vous avez glissé et vous avez raté votre coup! Vraiment malchanceux!")
        print(Style.RESET_ALL)
    else:
        print("Attaque effectuée avec succès!")
    ennemi_combat.soins_degats(round(-(att_final), 1))

    if ennemi_combat.vie > 0:
        print(att_final, "points de dégât ont été infligé à l'ennemi qui a maintenant ", ennemi_combat.vie, " points de vie.")
        monstre_attaque()
        return 0

    else:
        print(att_final, "points de dégât ont été infligé à l'ennemi qui a maintenant 0 points de vie.")
        fin_combat_reussite()
        return 1


def monstre_attaque():
    """
    Cette fonction inflige les dégats aux joueurs par l'ennemi
    """
    ennemi = ennemi_combat.indice
    vie_joueur = stat_raw[4]
    ennemi_nom = ennemi_liste[ennemi][1]

    defense_joueur = int(stat_raw[6])
    chance_joueur = int(stat_raw[7])
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print(ennemi_nom, "vous attaque ...!")
    #effet_du_monstre
    time.sleep(1.15)
    attaque_ennemi_supp = 1
    #calcul_vie_joueur_restante
    attaque_ennemi = int(ennemi_liste[ennemi][2])

    point_attaque_ennemi = (
        (attaque_ennemi + attaque_ennemi_supp)
        -(chance_joueur/15 + defense_joueur / 7)
        )

    if point_attaque_ennemi < 0:
        point_attaque_ennemi = 0
    vie_joueur = round(vie_joueur - point_attaque_ennemi,1)
    update_joueur(nom=Classes.nom, zone=stat_raw[3], vie=round(-(point_attaque_ennemi), 1))

    print("Vous perdez", round(point_attaque_ennemi,1), "points de vie et vous avez maintenant ",vie_joueur," points de vie.")

    stat_raw = elt_save()
    if stat_raw[4] <= 0:
        fin_combat_defaite()
    else:
        time.sleep(2.5)
        effets()


def effets():
    """
    Cette fonction définit les effets 
    """
    
    if ennemi_liste[ennemi_combat.indice][5] != 0:
        if ennemi_liste[ennemi_combat.indice][5] == "saignement":
            if int(ennemi_liste[ennemi_combat.indice][6]) > randint(0,100):
                stat_raw[4] -= round(int(ennemi_liste[ennemi_combat.indice][2]) /3  ,1)
                if stat_raw[4]< 0:
                    stat_raw[4] = 0 
                print("Vous avez maintenant ", stat_raw[4] ,"dû au saignement que votre ennemi a causé.")
        elif ennemi_liste[ennemi_combat.indice][5] == "poison":
            if int(ennemi_liste[ennemi_combat.indice][6]) > randint(0,100):
                poison = round(int(ennemi_liste[ennemi_combat.indice][2]) /2  ,1)
                stat_raw[4] -= poison
                if stat_raw[4]< 0:
                    stat_raw[4] = 0
                print("Vous avez été empoisonné!")
                print("Vous perdez ", poison, " points de vie.")
        elif ennemi_liste[ennemi_combat.indice][5] == "ecrasement":
            if int(ennemi_liste[ennemi_combat.indice][6]) > randint(0,100):
                print("L'ennemi vous a écrasé...")
                stat_raw[4] -= round(int(ennemi_liste[ennemi_combat.indice][2]) /2.5  ,1)
                if stat_raw[4]< 0:  
                    stat_raw[4] = 0
                print("Vous avez maintenant ", round(stat_raw[4],1), "points de vie.")
        elif ennemi_liste[ennemi_combat.indice][5] == "vie_drainage":
            if int(ennemi_liste[ennemi_combat.indice][6]) > randint(0,100):
                vie_drainee = round(int(ennemi_liste[ennemi_combat.indice][2]) /2  ,1)
                stat_raw[4] -= vie_drainee
                if stat_raw[4]< 0:
                    stat_raw[4] = 0
                print(ennemi_liste[ennemi_combat.indice][1], " a utilisé sa capacité drainage...")
                print("Votre ennemi vous a volé ",vie_drainee)
                vie_ennemi += vie_drainee
                print("Votre ennemi a récupéré ", vie_drainee, "points de vie.")
        elif ennemi_liste[ennemi_combat.indice][5] == "magie":
            if int(ennemi_liste[ennemi_combat.indice][6]) > randint(0,100):
                magie = round(int(ennemi_liste[ennemi_combat.indice][2]) /2  ,1)
                stat_raw[4] -= magie
                if stat_raw[4]< 0:
                    stat_raw[4] = 0
                print("Vous vous sentez bizzare, comme si vos forces vous quittent petit à petit... Votre ennemi a utilisé de la magie...")
                print("En conséquent, vous perdez ", magie, "points de vie et vous avez maintenant ", stat_raw[4], " points de vie.")
        elif ennemi_liste[ennemi_combat.indice][5] == "fatigue":
            if int(ennemi_liste[ennemi_combat.indice][6]) > randint(0,100):
                fatigue = round(int(ennemi_liste[ennemi_combat.indice][2]) /5  ,1)
                stat_raw[4] -= fatigue
                if stat_raw[4]< 0:
                    stat_raw[4] = 0
                print("La fatigue vous fait perdre ", fatigue, " points de vie!")
        elif ennemi_liste[ennemi_combat.indice][5] == "brulure":
            if int(ennemi_liste[ennemi_combat.indice][6]) > randint(0,100):
                brulure = round(int(ennemi_liste[ennemi_combat.indice][2]) /2  ,1)
                stat_raw[4] -= brulure
                if stat_raw[4]< 0:
                    stat_raw[4] = 0
                print("Vous remarquez une marque de brûlure sur votre corp...")
                print("Vous perdez ", brulure, " points de vie.")
    ennemi_combat.tours += 1
    main()

def fuir():       
    """
    Cette fonction sert à fuir, c'est-à-dire échapper le combat. Cela dépend du monstre choisit et de la chance du joueur. Le problème, c'est qu'en fuyant, on perd un peu d'argent.
    """
    liste_monstres = recup_monstre()
    joueur = elt_save()
    ennemi = ennemi_combat.indice
    if (liste_monstres[ennemi][13] == "possible") and int(joueur[7]) > 0:
        print(Fore.RED + "Vous avez fuit avec succès!")
        print(Style.RESET_ALL)
        piece_perdu = round(int((liste_monstres[ennemi][15]))/2)
        print("Mais malheureusement, vous perdez",piece_perdu,"pièces...")
        update_joueur(argent=-(piece_perdu))
        print("Vous avez maintenant", joueur[8], "pièces.")
        return 1
    else:
        print("Vous avez essayé de fuir, mais votre ennemi vous a rattrapé, la fuite n'est pas possible!")
        ennemi_combat.tours += 1
        return main()

def cache(): 
    """
    Cette fonction sert à se cacher, c'est-à-dire échapper le combat. Cela dépend du monstre choisit et de la chance du joueur. Contrairement à la fuite, on ne perd pas d'argent en se cachant. 
    """
    ennemi = ennemi_combat.indice
    liste_monstres = recup_monstre()
    joueur = elt_save()
    if (liste_monstres[ennemi][14] == "possible") and int(joueur[7]) > 0:
        print(Fore.RED + "Vous vous êtes caché, votre ennemi vous a pas vu et vous avez pu garder ce que vous possédez, ouf!!")
        print(Style.RESET_ALL)
        return 1
    else:
        ennemi_combat.tours += 1
        return main()

def fin_combat_reussite():
    """
    Cette fonction initie la fin du combat, lorsque l'ennemi est mort. Dans ce cas la, la fonction va donner l'argent qui est dû (la récompense), puis, elle va appeler la fonction qui elle va donner des potentiels objets
    en récompense.
    Pré-Condition : ennemi est un nombre entier entre 0 et l'indice du dernier ennemi du csv "monstres_csv". stat est le dictionnaire rassemblant tout les stats du joueur et inv est le dictionnaire qui gère l'inventaire
    du joueur. 
    Post-Condition : stat est renvoyé. 
    """
    ennemi = ennemi_combat.indice
    liste_monstres = recup_monstre(nom="X",all=True)
    element = elt_save()

    print(Fore.YELLOW + "x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print(Style.RESET_ALL)
    print("Combat terminé, l'ennemi est vaincu.")
    print(Fore.YELLOW + "x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print(Style.RESET_ALL)
    argent_gagne = liste_monstres[ennemi][15]
    update_joueur(Classes.nom, argent=argent_gagne)

    print("Vous obtenez", argent_gagne, "pièces et vous avez maintenant ",element[8]," pièces.")
    if liste_monstres[ennemi][10] == "bandit":
        bonus_bandit = randint(1,int(liste_monstres[ennemi][2])+5)
        print("Puisque votre ennemi était un bandit, vous obtenez ", bonus_bandit, "pièces en plus. Félicitation!" )
        update_joueur(Classes.nom, argent=bonus_bandit)
    return loot_recompense()

def fin_combat_defaite():
    """
    Cette fonction initie la fin du combat, lorsque le joueur est mort. Dans ce cas la, la fonction va donner l'argent qui est dû (la récompense), puis, elle va appeler la fonction qui elle va donner des potentiels objets
    en récompense.
    Pré-Condition : ennemi est un nombre entier entre 0 et l'indice du dernier ennemi du csv "monstres_csv". stat est le dictionnaire rassemblant tout les stats du joueur et inv est le dictionnaire qui gère l'inventaire
    du joueur. 
    Post-Condition : stat est renvoyé. 
    """
    ennemi = ennemi_combat.indice
    monstres_liste = recup_monstre
    print(Fore.YELLOW + "☠-x-☠-x-☠-x-☠-x-☠-x-☠-x-☠-x-☠")
    print(Style.RESET_ALL)
    print("Combat terminé, vous êtes vaincu.")
    print(Fore.YELLOW + "x-☠-x-☠-x-☠-x-☠-x-☠-x-☠-x-☠-x")
    print(Style.RESET_ALL)
    argent_perdu = randint(0,int(monstres_liste[ennemi][2])*2)
    update_joueur(argent= -(argent_perdu) )
    time.sleep(1.5)
    print("Vous vous réveillez sur un lit d'hôpital...")
    time.sleep(2)
    joueur = elt_save()


    print(f"Vous perdez {argent_perdu} pièces pour les soins...")
    if joueur[8] < 0:
        print("Et puis vous êtes en dette! Zut!")
    else:
        print("Vous avez déjà survécu, ça pourrait être pire!")
    update_joueur(vie=-50)

    print(Fore.GREEN + "Vous reprenez vos forces, la vie continue...!" + Style.RESET_ALL)
    return 0

    
def loot_recompense():
    """
    Cette fonction récompense le joueur ayant réussi le combat d'objets.
    Pré-Condition : ennemi est un nombre entier entre 0 et l'indice du dernier ennemi du csv "monstres_csv". stat est le dictionnaire rassemblant tout les stats du joueur et inv est le dictionnaire qui gère l'inventaire
    du joueur. 
    """
    ennemi = ennemi_combat.indice
    liste_monstre = recup_monstre()
    liste_objets = recup_objet()
    e = 1
    rarete = liste_monstre[4]
    for i in range(2):
        if ((rarete) <= (randint(0,100))):
            e+=1
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT ind
        FROM Objets
        WHERE typ1 = "{liste_monstre[ennemi][11]}" OR typ1 = "{liste_monstre[ennemi][12]}" OR typ2 = "{liste_monstre[ennemi][11]}" OR typ2 = "{liste_monstre[ennemi][12]}"
        """
    )
    T = cur.fetchall()
    conn.close()
    list(set(T))
    if T != []:
        if len(T) <= 5:
            loot = len(T)
        elif len(T) > 5:
            loot=6
        print(Fore.YELLOW + "x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print(Style.RESET_ALL)
        print("Vous recevez...")
        for i in range(loot):
            time.sleep(1)
            arajouter = str(liste_objets[T[i]][1])

            if int(liste_objets[T[i]][14]) >= randint(0,100):
                ajouter_inventaire(arajouter, 1)
                print(Fore.RED + "-", arajouter)
                print(Style.RESET_ALL)
        print(Fore.YELLOW + "x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print(Style.RESET_ALL)
        afficher_inventaire(classic=True)
    else:
        print("Vous ne pouvez rien récupérer de votre ennemi...")

class Ennemi_Actuel:
    def __init__(self):

        #self.indice = int(apparition(stat_raw[3]))
        self.indice = 0
        self.vie = ennemi_liste[self.indice][3]
        self.attaque = ennemi_liste[self.indice][2]
        self.tour = 0
    
    def soins_degats(self, vie):
        self.vie += vie
        return self.vie

ennemi_combat = Ennemi_Actuel()

if __name__ == "__main__":
    print(stat_raw)