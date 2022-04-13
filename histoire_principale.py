
from random import randint
from colorama import Style,Fore
import csv
import codecs
from boutique import boutique_debut
from evenements import chest
from combat_fonctions import main, specifique
from gestion_inventaire import *
from inventaire import affichage_inventaire, inventory_main
import time
from classes import *
from auto import wait_spacebar


def scen():
    T_hist_1=[]
    with codecs.open('scenario.csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=',')
        for row in r:
            T_hist_1.append(dict(row))
        return T_hist_1
def obj():
    T_obj_1=[]
    with codecs.open('liste_objets.csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=',')
        for row in r:
            T_obj_1.append(dict(row))
        return T_obj_1
        

def boss(inv,stat,arme,armure):
    print("af")
    fin(inv,stat,arme,armure)

def mauvaise_fin(stat,inventaire,arme,armure):
    print(Fore.CYAN + Style.BRIGHT + "|||||||||||||||||||||||||||||||-/ GAME OVER \-|||||||||||||||||||||||||||||||")
    return -1


def fin(inv,stat,arme,armure):
    print("Aussi, par soucis de budget, et de temps, vous décidez de retourner dans votre village pour plus longtemps que prévu. Vous vous achetez une petite maison au bord d'une rivière et devenez alcoolique.")
    print("Votre inventaire :")
    for key,value in inv.items():
        print("-",key,":",value)
    print(f"Vos statistiques : {stat}")
    print("Merci d'avoir joué à la démo d'Iltras. Nous n'avions pas eu le temps de développer l'histoire comme nous le voulions, donc peut-être qu'il y aura une suite plus tard, peut être pas...")
    print("Léo et Evann")
    

def zone_volca(inv,stat,arme,armure):
    print("af")
    boss(inv,stat,arme,armure)

def portail_demo(inv,stat,arme,armure):
    print("af")
    zone_volca(inv,stat,arme,armure)

def grotte(inv,stat,arme,armure):
    print("af")
    portail_demo(inv,stat,arme,armure)

def jungle(inv,stat,arme,armure):
    print("af")
    grotte(inv,stat,arme,armure)

def tp_potentiel(inv,stat,arme,armure):
    print("af")
    jungle(inv,stat,arme,armure)


def desert(inv,stat,arme,armure):
    print("af")
    jungle(inv,stat,arme,armure)

def ile_repos(inv,stat,arme,armure):
    print("af")
    desert(inv,stat,arme,armure)

def mer(inv,stat,arme,armure):
    print("af")
    desert(inv,stat,arme,armure)

def port(inv,stat,arme,armure):
    print("af")
    mer(inv,stat,arme,armure)
from random import shuffle
def grande_foret(inv,stat,arme,armure):
    zone=4
    update_joueur(nom=Classes.nom, zone=4)
    hist = scen()
    objets = obj()
    zone = 4
    print(hist[7]['scen1'])
    print("------------------------------------------------")
    choix_debut_f = "0dqqdzdqzd"
    while choix_debut_f != "1" and choix_debut_f != "2" and choix_debut_f != "3":
        choix_debut_f = input("Comment allez-vous entrer dans cette forêt? \n1-En faisant très attention \n2-Le plus vite possible! \n3-Normalement \n-> ")
        print("------------------------------------------------")
    if choix_debut_f == "1":
        print("Vous faites très attention aux alentours. Il pourrait y avoir des brigants qui trainent ou des monstres qui se cachent...")
        print("En observant bien, tout en marchant doucement, vous trouvez un objet!")
        print("------------------------------------------------")
        print("Vous obtenez...")
        loot_ind = int(chest(zone))
        loot = objets[loot_ind]['nom']
        print(Fore.RED + "-",loot)
        print(Style.RESET_ALL)
        if loot in inv:
            inv[loot] += 1
        else:
            inv[loot] = 1
        print("------------------------------------------------")
    elif choix_debut_f == "2":
        print("Vous allez si vite que vous ne faites pas attention. Vous tombez, perdez 3 points de vie et 3 ennemis tombent sur vous!")
        stat['vie'] = int(stat['vie']) - 3
        if int(stat['vie']) <= 0:
            stat['vie'] = 0
            mauvaise_fin(stat,inv,arme,armure)
        time.sleep(3)
        for i in range(0,2):
            main()
    elif choix_debut_f == "3":
        print("Aussi normal que vous pourriez l'être, vous marchez normalement, c'est normal! En suivant le chemin, vous tombez sur une sorcière...")
        print("------------------------------------------------")
        time.sleep(1)
        print("Elle vous dit : Cher(e) aventurier(e), auriez-vous l'amabilité de m'aider?")
        print("------------------------------------------------")
        choix_sorciere = "93ejqiodjkqdsp"
        while choix_sorciere != "1" and choix_sorciere != "2":
            choix_sorciere = input("1-Volontier \n2-Non Ahah! \n3-Voir l'inventaire \n-> ")
            print("------------------------------------------------")
            if choix_sorciere == "3":
                inventory_main("2",stat,inv,arme,armure)
        if choix_sorciere == "1":
            print("Vous aidez la sorcière du mieux que vous pouvez.")
            time.sleep(1.2)
            print("Reconnaissante, elle vous offre quelques potions et elixirs.")
            print("------------------------------------------------")
            print("Vous obtenez...")
            time.sleep(2)
            F = [t['ind'] for t in objets if t['elixir'] == "1"]
            shuffle(F)
            randomint = randint(0,len(F))
            for i in range(randomint):
                choix_obj = int(F[i])
                if int(objets[choix_obj]['chanceloot']) >= randint(0,100):
                    print(Fore.RED + "-",objets[choix_obj]["nom"])
                    print(Style.RESET_ALL)
                    if objets[choix_obj]["nom"] in inv:
                        inv[objets[choix_obj]["nom"]] += 1
                    else:
                        inv[objets[choix_obj]["nom"]] = 1
        elif choix_sorciere == "2":
            print("Tu vas voir, petit ingrat! Je vais t'apprendre les bonnes manières!")
            specifique(85,stat,25,inv,arme,armure)
    print(hist[7]['scen2'])
    time.sleep(0.5)
    print(hist[7]['scen3'])
    time.sleep(1.5)
    for i in range(2):
        main()
    print("------------------------------------------------")
    print(hist[7]['scen4'])
    choix_g = "0"
    while choix_g != "1" and choix_g != "2":
        choix_g = input("1-Entrer dans la grotte \n2-La contourner \n-> ")
        print("------------------------------------------------")
    if choix_g == "1":
        print("Un ours des cavernes vous tombe dessus!")
        specifique(107,35)
        time.sleep(2)
        print("Derrière l'ours se trouve quelques coffres! Vous les ouvrez...")
        print("Vous obtenez...")
        for i in range(0,3):
            loot = chest(zone)
            nombre = randint(0,4)
            print(Fore.RED + "-",objets[int(loot)]["nom"])
            print(Style.RESET_ALL)
            if objets[int(loot)]["nom"] in inv:
                inv[objets[int(loot)]["nom"]] += nombre
            else:
                inv[objets[int(loot)]["nom"]] = nombre
    elif choix_g == "2":
        print("Cette grotte ne vous fait pas confiance. Il est préférable de la contourner...")
        print("------------------------------------------------")
        time.sleep(2)
    print(hist[7]['scen5'])
    print("------------------------------------------------")
    g_choix = "qdjioqozdidpzidpqz,kd"
    while g_choix != "1" and g_choix != "2" and g_choix != "3":
        g_choix = input("Comment traverser cette rivière? \n1-Avec la bûche \n2-Les rochers \n3-Dans l'eau!\n-> ")
        print("------------------------------------------------")
    if g_choix == "1":
        print("Cette bûche à l'air d'être le meilleur chemin...")
        time.sleep(1.2)
        print("Vous avez traversé sans problème! Vous gagnez 2 points de chance.")
        print("------------------------------------------------")
        stat['chance'] = int(stat['chance']) + 2
    elif g_choix == "2":
        print("Vous vous empressez vers les rochers. Vous tentez le saut. Et vous glissez! Plouf... Vous êtes dans l'eau!")
        specifique(142, 10)
    elif g_choix == "3":
        print("Courageux, vous traversez la rivière de toutes vos forces... Et vous voilà de l'autre côté. Simple!")
        print("------------------------------------------------")
    print(hist[7]['scen6'])        
    nbr_max = randint(4,12)
    all_f = [y['ind'] for y in objets if y['typ'] == "baie"]
    all_fruit = [y['ind'] for y in objets if y['typ'] == "fruit"]
    e=0
    cueillette = "0"
    while cueillette != "1" and cueillette != "2":
        cueillette = input("\n1-Mmhhm Des baies! \n2-Mmmhmm Des fruits! \n3-J'ai autre chose à faire \n-> ")
        print("------------------------------------------------")
    if cueillette == "1":
        print("Vous vous empressez d'aller chercher le plus de baies possible..")
        choix_b = "iodqpjkpodsk"
        while choix_b != "2":
            choix_b = input("Voulez-vous cueillir? \n1-OUI \n2-NON \n-> ")
            print("------------------------------------------------")
            if choix_b == "1":
                random_object = randint(0,len(all_f)-1)
                print("Vous obtenez...")
                quantitee = randint(1,5)
                if objets[int(all_f[random_object])]["nom"] in inv:
                    inv[objets[int(all_f[random_object])]["nom"]] += quantitee
                else:
                    inv[objets[int(all_f[random_object])]["nom"]] = quantitee
                print(Fore.RED + "-",quantitee,objets[int(all_f[random_object])]["nom"])
                print(Style.RESET_ALL)
                e+=1
                if e>=nbr_max:
                    print("Vous avez été trop avide! Un petit groupe de monstres en ont profité pour vous encercler!!!!")
                    for i in range(4):
                        main()
                    choix_b = 2
        print("C'est assez ! Comme on le dit : Pour l'Homme avide, même la tombe est étroite.")
        print("------------------------------------------------")
    elif cueillette == "2":
        print("Vous vous empressez d'aller chercher le plus de fruits possible..")
        choix_b = "iodqpjkpodsk"
        while choix_b != "2":
            choix_b = input("Voulez-vous cueillir? \n1-OUI \n2-NON \n-> ")
            print("------------------------------------------------")
            if choix_b == "1":
                random_object = randint(1,len(all_fruit))
                print("Vous obtenez...")
                quantitee = randint(1,5)
                if objets[int(all_fruit[random_object])]["nom"] in inv:
                    inv[objets[int(all_fruit[random_object])]["nom"]] += quantitee
                else:
                    inv[objets[int(all_fruit[random_object])]["nom"]] = quantitee
                print(Fore.RED + "-",quantitee,objets[int(all_fruit[random_object])]["nom"])
                print(Style.RESET_ALL)
                e+=1
                if e >= nbr_max:
                    print("Vous avez été trop avide! Un petit groupe de monstres en ont profité pour vous encercler!!!!")
                    print("------------------------------------------------")
                    for i in range(4):
                        main()
                    choix_b = 2
        print("C'est assez ! Comme on le dit : Pour l'Homme avide, même la tombe est étroite.")
        print("------------------------------------------------")
    elif cueillette == "3":
        print("Des baies ? et puis quoi encore..?")
        print("------------------------------------------------")
    print(hist[7]['scen7'])
    for i in range(4):
        main()
    print(hist[7]['scen8'])
    print("------------------------------------------------")
    port(inv,stat,arme,armure)
#grande_foret({'Potion de vie':1},{'vie':100,'attaque':3,'defense':1,'chance':7,'argent':100},[],[])

def fin_prison_capitale(inv,stat):
    print(Fore.BLUE + "Étant trop suspicieux, les gardes vous ont emmené en prison. Et ce, pour le reste de vos jours. Alala, j'ai oublié de vous dire, ce pays ne possède pas de loi, et il n'y a pas de juge")
    print("Donc, je suppose que vous le savez mais c'est la fin des haricots pour vous...")
    print("Vous restez pendant plusieurs décennies en prison jusqu'à qu'ils vous libèrent pour avoir plus de place.")
    print("Le problème étant que vous n'avez plus rien, ni vie, ni chance, ni objets. En conséquent, vous ne vivez pas longtemps et ne vivez même pas un mois...")
    print(Style.RESET_ALL)
    mauvaise_fin({'vie':0,'attaque':1,'defense':0,'chance':-1,'argent':0},{},[],[])

def capitale(inv,stat,arme,armure):
    zone=3
    update_joueur(nom=Classes.nom, zone=3)
    hist = scen()
    print("------------------------------------------------")
    print(hist[6]['scen1'])
    print("Comment voulez-vous laisser paraître?")
    print("1. NIAIS")
    print("2. COOL")
    print("3. SUSPICIEUX")
    print("4. ABSOLUMENT NORMAL")
    print("5. EN COLERE")
    print("6. DÉPRIMÉ")
    print("------------------------------------------------")
    choix_cara = "0"
    while choix_cara != "1" and choix_cara != "2" and choix_cara != "3" and choix_cara != "4" and choix_cara != "5" and choix_cara != "6":
        choix_cara = input("Alors ? -> ")
        print("------------------------------------------------")
    if choix_cara == "1":
        print("Vous passez devant tout le monde d'un air très stupide... Vous jouez tellement bien le jeu qu'on vous vole 10 pièces!")
        stat['argent'] = int(stat['argent']) - 10
        print("Vous avez maintenant ",stat['argent']," pièces.")
        print("------------------------------------------------")
    elif choix_cara == "2":
        print("Vous êtes tellement pretentieux qu'un habitant vous défie en combat...")
        print("------------------------------------------------")
        specifique(122, 10)
    elif choix_cara == "3":
        fin_prison_capitale(inv,stat)
        return -1
    elif choix_cara == "4":
        print("Vous passez devant tout le monde, d'un air très normal, pour ne pas se faire remarquer...")
        print("Quand tout d'un coup, vous vous faites attaquer par un bandit! MAIS QUE FONT LES GARDES?!")
        print("------------------------------------------------")
        specifique(9, 10)
    elif choix_cara == "5":
        print("Vous passez devant tout le monde, d'un air colérique... Vous faites peur à tout le monde mais vous avancez.")
        print("Malheuresement, vous avanciez tellement rapidement que vous n'avez pas vu que vous êtes passé sous une échelle... Cela baisse vos points de chance de 3 points les descendant à : ",stat['chance'])
        print("------------------------------------------------")
    elif choix_cara == "6":
        print("Vous avez l'air si triste qu'on vous prend pour un mendiant... Vous gagnez 50 pièces!!")
        stat['argent'] = int(stat['argent']) + 50
        print("------------------------------------------------")
    print(hist[6]['scen2'])
    print("------------------------------------------------")
    print("ALLER A LA BOUTIQUE ?")
    print("1. OUI")
    print("2. NON")
    print("------------------------------------------------")
    choix_boutique = "0"
    while choix_boutique != "1" and choix_boutique != "2":
        choix_boutique = input("Faites un choix ! -> ")
        print("------------------------------------------------")
    if choix_boutique == "1":
        print(hist[6]['scen3'])
        print("...")
        time.sleep(4)
        boutique_debut(1,stat,inv,arme,armure)
    elif choix_boutique == "2":
        print("Vous vous dites que ce n'est pas nécéssaire et vous passez votre chemin..")
    print(hist[6]['scen4'])
    print("------------------------------------------------")
    continuer = "9zdqd95w9dfs759cxw99vcxv21299fluls99999"
    while continuer == "9zdqd95w9dfs759cxw99vcxv21299fluls99999":
        continuer = input("Tapez n'importe quoi pour continuer...")
        print("------------------------------------------------")
    print(hist[6]['scen5'])
    print("------------------------------------------------")
    print("QUE CHOISISSEZ-VOUS DE FAIRE?")
    print("1. J'accepte la quête !")
    print("2. Je décline la quête.")
    print("------------------------------------------------")
    accepter = "0"
    while accepter != "1" and accepter != "2":
        accepter = input("Acceptez-vous la quête du Roi ?")
        print("------------------------------------------------")
    if accepter == "1":
        print(hist[6]['scen7'])
        print("------------------------------------------------")
        print("Pour vous aider dans votre quête, le roi vous a fourni 100 pièces ! (soit il est radin, soit ce royaume est dans la pauvreté!)")
        print("------------------------------------------------")
        stat['argent'] = int(stat['argent']) + 100
    elif accepter == "2":
        print(hist[6]['scen6'])
        return -1
    ####
    time.sleep(3)
    print(hist[6]['scen8'])
    print("------------------------------------------------")
    print(hist[6]['scen9'])
    print("------------------------------------------------")
    print("Vous re-passez devant la boutique... voulez-vous y aller/retourner?")
    print("1. OUI")
    print("2. NON")
    boutique_2 = "0"
    while boutique_2 != "1" and boutique_2 != "2":
        boutique_2 = input("Alors ? -> ")
        print("------------------------------------------------")
    if boutique_2 == "1":
        boutique_debut(1,stat,inv,arme,armure)
    elif boutique_2 == "2":
        print("Vous êtes sûr de vous, le vent dans les cheveux, vous décidez que NON. Vous ne voulez pas aller à la boutique.")
        print("------------------------------------------------")
    print(hist[6]['scen10'])
    time.sleep(5)
    grande_foret(inv,stat,arme,armure)



def foret_continue(inv,stat,arme,armure):
    zone = 111
    objets = obj()
    hist = scen()
    print(hist[5]['scen1'])
    main()
    print(hist[5]['scen4'])
    print(hist[5]['scen11'])
    print(hist[5]['scen12'])
    choix = "0"
    print("------------------------------------------------")
    print("Il faudrait qu'on puisse lui traduire ce qu'elle dit...")
    print("------------------------------------------------")
    print("Choix :")
    print("1- La réponse est...")
    print("2- Aurevoir!")
    print("3- Voler des plantations et s'enfuir")
    print("------------------------------------------------")
    while ((choix != "1") and (choix !="2") and (choix != "3")):
        choix = input("Que voulez-vous faire? -> ")
        print("------------------------------------------------")
    if choix == "1":
        essaies = 0
        essais_totaux = 5
        essais_input = "rtcdtrfyugi"
        print("Vous avez 5 essais avant que le fermier abandonne son code promo pour des graines de patate gratuites...")
        print("------------------------------------------------")
        while essaies != 5 and essais_input != "NUTELLA":
            essais_input = input("Alors ? Quel est le code(en majuscules), étant donné que sa femme ENITSUJ lui dit ALLETUN? -> ")
            print("------------------------------------------------")
            if essais_input != "NUTELLA" :
                essaies += 1
                print("Il vous reste ",essais_totaux - essaies," essais.")
                print("------------------------------------------------")
            else:
                print(hist[5]['scen13'])
    elif choix == "2":
        print(hist[5]['scen14'])
        print("Étant dans la coutume du village, le fermier vous donne, cependant, un petit cadeau!")
        objet = objets[103]["nom"]
        if 'Tomate dorée' in inv:
            inv['Tomate dorée'] = inv['Tomate dorée'] + 1
        else:
            inv['Tomate dorée'] = 1
        print("Vous obtenez...")
        print(Fore.RED + "-",objet)
        print(Style.RESET_ALL)
    elif choix == "3":
        print("Vous vous empressez dans son jardin et vous volez tout ce que vous pouvez trouver...")
        print("------------------------------------------------")
        print("Vous obtenez...")
        print(Fore.RED)
        T = [int(e['ind']) for e in objets if e['typ'] == "legume"]
        for i in range(3):
            for i in range(len(T)):
                if randint(0,50)>25:
                    if objets[T[i]]["nom"] in inv:
                        inv[objets[T[i]]["nom"]] +=1
                    else:
                        inv[objets[T[i]]["nom"]] = 1
                    print(" - ",objets[T[i]]["nom"])
        inv[objets[72]["nom"]] = 1
        print(Style.RESET_ALL)
        inventory_main(0,stat,inv,arme,armure)
    capitale(inv,stat,arme,armure)


def montagne_continue(inv,stat,arme,armure):
    zone = 113
    hist = scen()
    print(hist[5]['scen1'])
    main()
    print(hist[5]['scen2'])
    if int(stat['chance']) < 0:
        print("Quand Soudain, vous trebuchez à cause du changement de terrain...Flute! Vous perdez 2 points de vie.")
        stat['vie'] = int(stat['vie']) - 2
        if stat['vie'] <= 0:
            stat['vie'] = 0
            mauvaise_fin(stat,inv,arme,armure)
    print(hist[5]['scen8'])
    choix = "0"
    print("1- Voler le butin")
    print("2- Interpeller le noble")
    print("3- Le combattre")
    print("4- Voir l'inventaire")
    while ((choix != "1") and (choix != "2") and (choix != "3") and (choix !="4")):
        choix = input("Que voulez-vous faire? ->")
    if choix == "4":
        inventory_main(0,stat,inv,arme,armure)
        print("Vous vous décidez de...")
        print("1- Voler le butin")
        print("2- Interpeller le noble")
        print("3- Le combattre")
        while ((choix != "1") and (choix != "2") and (choix != "3")):
            choix = input("Que voulez-vous faire? ->")
    if choix == "1":
        print(hist[5]['scen9'])
        stat['vie'] = int(stat['vie']) - 5
        if stat['vie'] <= 0:
            stat['vie'] = 0
            mauvaise_fin(stat,inv,arme,armure)
    elif choix == "2":
        print(hist[5]['scen10'])
        stat['argent'] = int(stat['argent']) + 30
    elif choix == "3":
        print("En garde contre le noble! (bonne chance!)")
        specifique(112, 30)
    capitale(inv,stat,arme,armure)

def plaine_continue(inv,stat,arme,armure):
    zone = 112
    objets = obj()
    hist = scen()
    print(hist[5]['scen1'])
    main()
    print(hist[5]['scen3'])
    print(hist[5]['scen5'])
    choix = 0
    print("1- Le pont")
    print("2- Le lac")
    while ((choix != "1") and (choix != "2")):
        choix = input("Le pont ou le lac ? -> ")
    if choix == "1":
        print(hist[5]['scen6'])
        loot = int(chest(zone))
        print("Vous obtenez... ",objets[loot]["nom"])
        if objets[loot]["nom"] in inv:
            inv[objets[loot]["nom"]] = inv[objets[loot]["nom"]]+1
        else:
            inv[objets[loot]["nom"]] = 1
    elif choix == "2":
        print(hist[5]['scen7'])
        print("Soudain, vous croisez le regard d'un chat noir, votre chance diminue de 3 points...")
        stat['chance'] = int(stat['chance']) - 3
    capitale(inv,stat,arme,armure)

def foret(inv,stat,arme,armure):
    hist = scen()
    objets = obj()
    zone=111
    print("------------------------------------------------")
    print(hist[2]['scen1'])
    time.sleep(1.5)
    print(hist[2]['scen2'])
    main()
    print(hist[2]['scen3'])
    time.sleep(1.5)
    print(hist[2]['scen4'])
    main()
    print(hist[2]['scen5'])
    print("------------------------------------------------")
    choix_chemin_2 = "0"
    while choix_chemin_2!="1" and choix_chemin_2!="2":
        choix_chemin_2=input("Vous prenez le chemin de :\n1-Droite \n2-Gauche \n->")
        print("------------------------------------------------")
    if choix_chemin_2=="1":
        print(hist[2]['scen6'])
        print("------------------------------------------------")
        print("Vous obtenez...")
        loot = int(chest(zone))
        loot_objet = objets[loot]["nom"]
        if loot_objet in inv:
            inv[loot_objet] += 1
        else:
            inv[loot_objet] = 1
        time.sleep(0.5)
        print(Fore.RED + "-",loot_objet)
        print(Style.RESET_ALL)
        time.sleep(3.7)
        print("------------------------------------------------")
        stat['vie']=int(stat['vie'])-5
        if int(stat['vie']) <= 0:
            mauvaise_fin(stat,inv,arme,armure)
        
    elif choix_chemin_2=="2":
        print(hist[2]['scen7'])
        main()
        print(hist[2]['scen8'])
        main()
        print(hist[2]['scen9'])
        print("------------------------------------------------")
        choix_coffre_1 = "0"
        while choix_coffre_1!="1" and choix_coffre_1!="2":
            choix_coffre_1=input("Que choisissez vous de faire ? \n1-Fouiller la maisonnette \n2-Continuer votre chemin \n-> ")
        if choix_coffre_1=="1":
            print("------------------------------------------------")
            print(hist[2]['scen10'])
            print("------------------------------------------------")
            print("Vous obtenez...")
            objets = obj()
            loot = int(chest(zone))
            print(Fore.RED + "-",objets[loot]["nom"])
            print(Style.RESET_ALL)
            if objets[loot]["nom"] in inv:
                inv[objets[loot]["nom"]] = inv[objets[loot]["nom"]]+1
            else:
                inv[objets[loot]["nom"]] = 1
            print("votre inventaire:")
            print(inv)
        elif choix_coffre_1=="2":
            print("------------------------------------------------")
            print(hist[2]['scen11'])
            print("------------------------------------------------")
    print(hist[2]['scen12'])
    print(hist[2]['scen13'])
    print("Vous obtenez...")
    objets = obj()
    loot = int(chest(zone))
    print(Fore.RED + "-", objets[loot]["nom"])
    print(Style.RESET_ALL)
    if objets[loot]["nom"] in inv:
        inv[objets[loot]["nom"]] = inv[objets[loot]["nom"]]+1
    else:
        inv[objets[loot]["nom"]] = 1
    print("Votre inventaire:")
    for key,value in inv.items():
        print("-",key,":",value)
    time.sleep(3)
    print("------------------------------------------------")
    print(hist[2]['scen14'])
    time.sleep(0.5)
    print(hist[2]['scen15'])
    print("------------------------------------------------")
    #fin forêt
    foret_continue(inv,stat,arme,armure)
#foret({'Potion de vie':1},{'vie':100,'attaque':3,'defense':1,'chance':7,'argent':100},[],[])

def plaine(inv,stat,arme,armure):
    hist=scen()
    zone=112
    print("------------------------------------------------")
    print(hist[3]['scen1'])
    print(hist[3]['scen2'])
    print(hist[3]['scen3'])
    print("------------------------------------------------")
    choix_chemin_3="0"
    while (choix_chemin_3!="1") and (choix_chemin_3!="2"):
        choix_chemin_3=input("1-Vous décidez de vous y rendre \n2-Vous continuez votre chemin.")
        print("------------------------------------------------")
        if choix_chemin_3=="1":
            print("------------------------------------------------")
            print(hist[3]['scen4'])
            specifique(9, 8)
        elif choix_chemin_3=="2":
            print("------------------------------------------------")
            print(hist[3]['scen5'])
            print("------------------------------------------------")
            print(hist[3]['scen6'])
            print(hist[3]['scen7'])
            print("------------------------------------------------")
            #fin plaine
    plaine_continue(inv,stat,arme,armure)

def montagne(inv,stat,arme,armure):
    hist = scen()
    zone=113
    print("------------------------------------------------")
    print(hist[4]['scen1'])
    print(hist[4]['scen2'])
    stat['vie'] = int(stat['vie']) - 3       #PERD 3 POINTS DE VIE
    if int(stat['vie']) <= 0:
        mauvaise_fin(stat,inv,arme,armure)
    print(hist[4]['scen3'])
    stat['vie'] = int(stat['vie']) - 3           #IDEM
    if int(stat['vie']) <= 0:
        mauvaise_fin(stat,inv,arme,armure)
    print("------------------------------------------------")
    choix_chemin_4 = "0"
    while (choix_chemin_4!="1") and (choix_chemin_4!="2"):
        choix_chemin_4=input("1- Vous vous arrêter pour vous reposer \n2- Vous continuez.")
    if choix_chemin_4=="1":
        print("------------------------------------------------")
        print(hist[4]['scen4'])
        stat['vie'] = stat['vie'] + 10
        if stat['vie'] > 100:
            stat['vie'] = 100
        print("------------------------------------------------")
    elif choix_chemin_4=="2":
        print("------------------------------------------------")
        print(hist[4]['scen5'])
        stat['vie'] = stat['vie']-3
    print("------------------------------------------------")
    print(hist[4]['scen6'])
    print("------------------------------------------------")
    main()
    choix_chemin_5 = "0"
    while choix_chemin_5!="1" and choix_chemin_5!="2":
        choix_chemin_5=input("1-Vous décidez de grimper au sommet \n2-Vous décidez de prendre le côté.")
    if choix_chemin_5=="1":
        print("------------------------------------------------")
        print(hist[4]['scen7'])
    elif choix_chemin_5=="2":
        print("------------------------------------------------")
        print(hist[4]['scen8'])
    print("------------------------------------------------")
    print(hist[4]['scen9'])
    print("Vous obtenez...")
    objets = obj()
    for i in range(0,3):
        loot = int(chest(zone))
        print(objets[loot]["nom"])
        if objets[loot]["nom"] in inv:
            inv[objets[loot]["nom"]] = inv[objets[loot]["nom"]]+1
        else:
            inv[objets[loot]["nom"]] = 1
    print("votre inventaire:")
    print(inv)
    print(hist[4]['scen10'])
    print("------------------------------------------------")
    montagne_continue(inv,stat,arme,armure)

def histoire_principale_d():
    """
    Ce programme est le programme principal du jeux c'est là que l'histoire est développée.
    C'est un peu la mise en place, le début de l'histoire.
    """
    hist = scen()
    update_joueur(nom=Classes.nom, zone=0)
    print("------------------------------------------------")
    print(hist[1]['scen1'])
    time.sleep(3)
    print(hist[1]['scen2'])
    print("------------------------------------------------")
    time.sleep(3)
    print(hist[1]['scen3'])
    ajouter_inventaire("Petit couteaux")
    ajouter_inventaire("Côte de boeuf")
    print("------------------------------------------------")
    afficher_inventaire(classic = True)
    time.sleep(0.5)
    wait_spacebar()
    print(hist[1]['scen4'])
    wait_spacebar()
    print("------------------------------------------------")
    choix_1 = "0"
    while ((choix_1!="1") and (choix_1!="2")) and type(choix_1) != int:
        print("1-Vous partez à gauche vers le centre ville")
        print("2-Vous prenez à droite direction la grotte.")
        choix_1= (input("Que Faire ? -> "))

    if choix_1=="2":
        print(hist[1]['scen7'])
        time.sleep(1.5)
        print(hist[1]['scen8'])
        time.sleep(1.5)
        print(hist[1]['scen9'])
        time.sleep(1.5)
        print(hist[1]['scen10'])
        time.sleep(1.5)
        print(hist[1]['scen11'])
        print("------------------------------------------------")
        
        specifique(107, 90)
        print("Vous auriez du écouter les interdictions de vos parents.")
        histoire_principale_d()
    elif choix_1=="1":
        print(hist[1]['scen12'])
        print("------------------------------------------------")
        print("1-Vous décidez d'aller faire des achats dans une boutique.\n2-Vous partez sans aucuns remords en direction de la sortie du village.")
        choix_2= input("Que Faire? -> ")
        while choix_2!="1" and choix_2!="2":
            choix_2= input("Que Faire? -> ")
        if choix_2=="1":
            print("------------------------------------------------")
            print("Vous vous dirigez vers une grande boutique dont l'enseigne ne tient en place que par la volonté de dieu.")
            print("Vous y entrez d'un pas déterminé !")
            print("------------------------------------------------")
            boutique_debut(0, afficher_inventaire)
        elif choix_2=="2":
            print("Vous pensez que ce n'est qu'une perte de temps, donc, vous sortez directement du village.")
        print("Vous arrivez à la sortie du village, 3 chemins s'offrent à vous.")
        print("------------------------------------------------")
        
        choix_chemin_1 = "0"
        while (choix_chemin_1!= "1") and (choix_chemin_1!="2") and (choix_chemin_1!="3"):
            print("Vous voulez aller en direction de :")
            print(Fore.RED + "\n1-La forêt \n2-Les plaines \n3-Les montagnes \n4-Regarder l'inventaire")
            print(Style.RESET_ALL)
            choix_chemin_1= input("Que faire...où aller...? -> ")
            if choix_chemin_1 == "4":
                inventory_main(afficher_inventaire)
        if choix_chemin_1=="1": #début de la forêt
            foret(afficher_inventaire)
        elif choix_chemin_1=="2": #début plaine
            plaine(afficher_inventaire)
        elif choix_chemin_1=="3":
            montagne(afficher_inventaire)
#histoire_principale_d({"vie":100,"attaque":3,"defense":20,"chance":7,"argent":100},[],[])

if __name__ == "__main__":
    pass