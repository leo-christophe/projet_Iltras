from random import randint
from random import choice
import csv
import codecs
def hist():
    T_hist_1=[]
    with codecs.open('histoire;csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=';')
        for row in r:
            histoire;append(dict(row))
        return histoire
def obj():
    T_obj_1=[]
    with codecs.open('liste_objet;csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=';')
        for row in r:
            liste_objet;append(dict(row))
        return liste_objet

def Debut():
    '''Ce programme sert à choisir sa classe de personnage.
    préconditions: le joueur doit choisir une classe avec un numéro allant de 1 à 3.
    postconditions: le programme renvoit un numéro associer à une classe (1,2 ou 3)'''
    choix_joueur=input("Quel personnage rêve tu de devenir ? 1-Chevalier; 2-Clypeus; 3-Lutin.")
    while choix_joueur!=1 or choix_joueur!=2 or choix_joueur!=3:
        choix_joueur=input("choisit un personnage entre 1-Chevalier , 2-Clypeus , 3-Lutin.")
    return choix_joueur

def choix_nom():
    '''Ce programme permet au joueur de choisir son nom d'aventurier/aventurière.'''
    choix_nom=input("Quel est ton nom aventurier/ aventuriere ?")
    return choix_nom

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

def marchand_plaine():
    objet=obj()
    print("************************************************")
    print("Bonjour, cher aventurier et bienvenue à l'auberge du Cochon doré !")
    print("************************************************")
    choix_marchand_1=input("1- Acheter ; 2- Vendre ; Partir")
    while choix_marchand_1!=1 or choix_marchand_1!=2 or choix_marchand_1!=3:
        choix_marchand_1=input("1- Acheter ; 2- Vendre ; 3- Partir")
    if choix_marchand_1==1:
        print("************************************************")
        print("Je possède quelques articles qui devraient surement vous intéresser !")
        print("************************************************")
        print("Objets :")
        print("1-",obj[8]['nom'],"prix :",obj[8]['val'],"Inflige ",obj[8]['att'],"de dégats.")
        print("2-",obj[21]['nom'],"prix :",obj[21]['val'],"Augmente de ",obj[21]['def'],"de protection.")
        print("3-",obj[33]['nom'],"prix :",obj[33]['val'],"Donne ",obj[33]['vie'],"de vie et",obj[33]['att'],"d'attaque.")
        print("4-",obj[31]['nom'],"prix :",obj[31]['val'],"Augmente de  ",obj[31]['def'],"de protection.")
        dem_achat_2=input("Que choisissez vous d'acheter ? entrez -1 pour sortir sans achat.")
        while dem_achat_2!=1 or dem_achat_2!=2 or dem_achat_2!=3 or dem_achat_2!=3:
            dem_achat_2=input("Il faut entrez un numéro d'objet si vous voulez acheter quelque chose.")
        if dem_achat_2==1:
            return 8
        elif dem_achat_2==2:
            return 21
        elif dem_achat_2==3:
            return 33
        elif dem_achat_2==4:
            return 31
        elif dem_achat_2==-1:
            return -1
    elif choix_marchand_1==2:
        #vendre qqc
    elif choix_marchand_1==3:
        print("************************************************")
        print("Au revoir et bonne route !")
        print("************************************************")
        return -1

def chest():
    nbr=randint(0,100)
    t=[]
    for i in range obj['ind']+1:
        if obj['cof']==1:
            if nbr<=obj['ctl']:
                t.append([obj['ind']])
    n=randint(0,len(t))
    return t[n]

def loot():
    nbra=randint(0,100)
    T=[]
    for i in range obj['ind']+1:
        if obj['lms']==1:
            if nbra<=obj['clm']:
                T.append(obk['ind'])
    na=randint(0,len(T))
    return T[n]

def nombre_aleatoire():
    nbr=randint(0,100)
    return nbr

def partie():
    '''Ce programme est le programme principal du jeux c'est là que l'histoire est dévellopée.'''
    obj=objet()
    inv={}
    stat={}
    print("------------------------------------------------")
    print("Bonjour, à toi aventurier bienvenue dans le monde d'Iltras !'")
    print("------------------------------------------------")
    nom=choix_nom()
    print("Maintenant,",nom,",tu dois choisir une classe.")
    print("------------------------------------------------")
    c_c=Debut()
    if c_c==1:
        print("Par la bénédiction de la sainte frite te voila Chevalier !!")
        stat={"vie":100,"att":10,"def":5,"cha":5,"arg":200}
    if c_c==2:
        print("Mais que voila est-ce un mur,non ça m'a l'air plus dur, voici donc le fameux Clypeus !!")
        stat={"vie":100,"att":3,"def":20,"cha":7,"arg":100}
    if c_c==3:
        print("Saperlipopette ! Par la magie des bottes de Merlin ! Enchanté! This is THE Lutin !!")
        stat={"vie":100,"att":1,"def":3,"cha":75,"arg":1000}
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