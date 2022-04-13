from random import randint
from random import choice
import csv
import codecs
def hist():
    T_hist_1=[]
    with codecs.open('histoire;csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=',')
        for row in r:
            histoire;append(dict(row))
        return histoire
def obj():
    T_obj_1=[]
    with codecs.open('liste_objet;csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=',')
        for row in r:
            liste_objet;append(dict(row))
        return liste_objet

def marchand_spawn():
    objet=obj()
    print("************************************************")
    print("Bonjour, cher mouto... euh client, bienvenue dans ma modeste boutique. Comment puis-je vous aider ?")
    print("************************************************")
    choix_march=input("1-Acheter ; 2-Vendre ; 3- Partir")
    while choix_march!=1 or choix_march!=2:
        choix_march=input("Bon j'ai une livraison qui m'attend. Que puis-je faire pour vous ?   1- Acheter ; 2- Vendre ;3- Partir")
    print("************************************************")
    if choix_march ==1:
        print("************************************************")
        print("Cela tombe bien je viens de recevoir de nouveaux articles qui vont surement vous plaire !")
        print("************************************************")
        print("Equipement:")
        print("1-",obj[24]['nom'],"prix :",obj[24]['val'],"Augmente la défense de",obj[24]['def'])
        print("2-",obj[25]['nom'],"prix :",obj[25]['val'],"Augmente la défense de",obj[25]['def'])
        print("************************************************")
        print("Armes :")
        print("3-",obj[7]['nom'],"prix :",obj[7]['val'],"Inflige ",obj[7]['att']," de dégats.")
        print("4-",obj[10]['nom'],"prix :",obj[10]['val'],"Inflige ",obj[10]['att']," de dégats.")
        print("************************************************")
        print("Potions :")
        print("5-",obj[0]['nom'],"prix :",obj[0]['val'],"Soigne ",obj[0]['vie']," point de vie.")
        print("************************************************")
        dem_achat=input("Que choisissez vous ? entrez -1 pour sortir sans rien acheter.")
        while dem_achat!=1 or dem_achat!=2 or dem_achat!=3 or dem_achat!=4 or dem_achat!=5:
            dem_achat=input("Cher client donner moi un numéro de rayon je suis un peut myope...")
        if dem_achat==1:
            return 24
        elif dem_achat==2:
            return 25
        elif dem_achat==3:
            return 7
        elif dem_achat==4:
            return 10
        elif dem_achat==5:
            return 0
        elif dem_achat_2==-1:
            return -1
    elif choix_march==2:
        return -2
    elif choix_march==3:
        print("************************************************")
        print("Au revoir cher client !(Grmml c'était bien la peine de me déranger)'")
        print("************************************************")
    return -1

def histoire_principale():
    '''Ce programme est le programme principal du jeux c'est là que l'histoire est dévellopée.'''
    print("------------------------------------------------")
    print(hist[1]['scen1'])
    print(hist[1]['scen2'])
    print("------------------------------------------------")
    print(hist[1]['scen3'])
    print("------------------------------------------------")
    if 'Petit couteaux' in inv:
        inv['Petit couteaux']=inv['Petit couteaux']+1
    else:
        inv['Petit couteaux']=1
    if 'Côte de boeuf' in inv:
        inv['Côte de boeuf']=inv['Côte de boeuf']+1
    else:
        inv['Côte de boeuf']=1
    print("------------------------------------------------")
    print(inv)
    print("------------------------------------------------")
    print(hist[1]['scen4'])
    print("------------------------------------------------")
    choix_1=input("1-Vous partez à gauche vers le centre ville ; 2-Vous prenez à droite direction la grotte.")
    while choix_1!=1 or choix_1!=2:
         choix_1=input("1-Vous partez à gauche vers le centre ville 2-Vous prenez à droite direction la grotte.")
    if choix_1==2:
        print("------------------------------------------------")
        print(hist[1]['scen5'])
        print(hist[1]['scen6'])
        print(hist[1]['scen7'])
        print(hist[1]['scen8'])
        print(hist[1]['scen9'])
        print(hist[1]['scen10'])
        print(hist[1]['scen11'])
        print("------------------------------------------------")
        return ("Vous auriez du écouter les interdictions de vos parents.")
    print("------------------------------------------------")
    print(hist[1]['scen12'])
    print("------------------------------------------------")
    choix_2=input("1-Vous décidez d'aller faire des achats dans une boutique ; 2-Vous partez sans aucuns remords en direction de la sortie du village.")
    while choix_2!=1 or choix_2!=2:
        choix_2=input("1-Vous décidez d'aller faire des achats dans une boutique ; 2-Vous partez sans aucuns remords en direction de la sortie du village.")
    if choix_2==1:
        print("------------------------------------------------")
        print("Vous vous dirigé vers une grande boutiques dont l'enseigne ne tient en place que par la volonté de dieux.'")
        print("Vous y entrez d'un pas déterminé !'")
        print("------------------------------------------------")
        v=0
        while v!=1:
            achat=marchand_spawn()
            if achat ==-1:
                print("------------------------------------------------")
                print("Vous sortez de la boutique est cette fois vous êtes déterminé à partir pour de bon.")
                print("HOP ! Au pas de course jusqu'à la sortie du village !")
                print("------------------------------------------------")
                v=v+1
            elif achat==-2:
                print("------------------------------------------------")
                print("Pour le moment vous n'avez rien à vendre.'")
                print("------------------------------------------------")
            elif achat ==24:
                if (stat['arg'])>=30:
                    print("------------------------------------------------")
                    print("Vous ajoutez cet objet à votre inventaire")
                    print("------------------------------------------------")
                    if 'Tunique en cuir' in inv:
                        inv['Tunique en cuir']=inv['Tunique en cuir']+1
                    else:
                        inv['Tunique en cuir']=1
                    stat['arg']=stat['arg']-30
                else:
                    print("------------------------------------------------")
                    print("Vous ne possédez pas assez d'argent pour acheter cet objet.")
                    print("------------------------------------------------")
            elif achat ==25:
                if (stat['arg'])>=110:
                    print("------------------------------------------------")
                    print("Vous ajoutez cet objet à votre inventaire")
                    print("------------------------------------------------")
                    if 'Cote de maille' in inv:
                        inv['Cote de maille']=inv['Cote de maille']+1
                    else:
                        inv['Cote de maille']=1
                    stat['arg']=stat['arg']-110
                else:
                    print("------------------------------------------------")
                    print("Vous ne possédez pas assez d'argent pour acheter cet objet.")
                    print("------------------------------------------------")
            elif achat ==7:
                if (stat['arg'])>=70:
                    print("------------------------------------------------")
                    print("Vous ajoutez cet objet à votre inventaire")
                    print("------------------------------------------------")
                    if 'Arc humain' in inv:
                        inv['Arc humain']=inv['Arc humain,']+1
                    else:
                        inv['Arc humain']=1
                    stat['arg']=stat['arg']-70
                else:
                    print("------------------------------------------------")
                    print("Vous ne possédez pas assez d'argent pour acheter cet objet.")
                    print("------------------------------------------------")
            elif achat ==10:
                if (stat['arg'])>=10:
                    print("------------------------------------------------")
                    print("Vous ajoutez cet objet à votre inventaire")
                    print("------------------------------------------------")
                    if 'Poignard' in inv:
                        inv['Poignard']=inv['Poignard']+1
                    else:
                        inv['Poignard']=1
                    stat['arg']=stat['arg']-10
                else:
                    print("------------------------------------------------")
                    print("Vous ne possédez pas assez d'argent pour acheter cet objet.")
                    print("------------------------------------------------")
            elif achat ==0:
                if (stat['arg'])>=20:
                    print("------------------------------------------------")
                    print("Vous ajoutez cet objet à votre inventaire")
                    print("------------------------------------------------")
                    if 'Potion de vie' in inv:
                        inv['Potion de vie']=inv['Potion de vie']+1
                    else:
                        inv['Potion de vie']=1
                    stat['arg']=stat['arg']-20
                else:
                    print("------------------------------------------------")
                    print("Vous ne possédez pas assez d'argent pour acheter cet objet.")
                    print("------------------------------------------------")
        print("Vous arrivez à la sortie du village,3 chemins s'offrent à vous.")
        print("------------------------------------------------")
    choix_chemin_1=input("Vous décidez de partir en direction: 1-De la foret ; 2-Des plaines ; 3-Des montagnes.")
    while choix_chemin_1!= 1 or choix_chemin_1!=2 or choix_chemin_1!=3:
        choix_chemin_1=input("Vous décidez de partir en direction: 1-De la foret ; 2-Des plaines ; 3-Des montagnes.")
    if choix_chemin_1==1: #début de la forêt
        print("------------------------------------------------")
        print(hist[2]['scen1'])
        print(hist[2]['scen2'])
        print(hist[2]['scen3'])
        print(hist[2]['scen4'])
        print("------------------------------------------------")
        choix_chemin_2=input("Vous prenez 1- à droite 2- à gauche ou 3- Vous explorer les environs.")
        while choix_chemin_2!=1 or choix_chemin_2!=2 or choix_chemin_2!=3:
            choix_chemin_2=input("Vous prenez 1- à droite 2- à gauche ou 3- Vous explorer les environs.")
        if choix_chemin_2==1:
            print("------------------------------------------------")
            print(hist[2]['scen5'])
            print("------------------------------------------------")
            if randint(0,2)>1:
                #combat aléatoire
            else:
                loot=chest()
                print("------------------------------------------------")
                print("Vous trouvez", obj[loot]['nom']"!")
                print("------------------------------------------------")
                print("Vous ajoutez cet objet à votre inventaire")
                print("------------------------------------------------")
                if obj[loot]['nom'] in inv:
                    nom_objet=obj[loot]['nom']
                    inv[nom_objet]=inv[nom_objet]+1
                else:
                    inv[nom_objet]=1
        elif choix_chemin_2==2:
            print("------------------------------------------------")
            print(hist[2]['scen6'])
            print(hist[2]['scen7'])
            print("------------------------------------------------")
            choix_coffre_1=input("Que choisissez vous de faire ? 1- Fouiller la caravanne 2- Continuer votre chemin .")
            while choix_coffre_1!=1 or choix_coffre_1!=2:
                choix_coffre_1=input("Que choisissez vous de faire ? 1- Fouiller la caravanne 2- Continuer votre chemin .")
            if choix_coffre_1==1:
                print("------------------------------------------------")
                print(hist[2]['scen8'])
                print("------------------------------------------------")
                nbr=nombre_aleatoire()
                if nbr<=stat['cha']:
                    chest()
            elif choix_coffre_1==2:
                print("------------------------------------------------")
                print(hist[2]['scen9'])
                print("------------------------------------------------")