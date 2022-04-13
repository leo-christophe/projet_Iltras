import sqlite3
from datetime import datetime
from classes import *
from random import *

DB_FILE = 'assets'

def creer_connexion(DB_FILE):
    """ cree une connexion a la base de donnees SQLite
        specifiee par db_file
        le fichier est cree s'il n'existe pas.
    :param db_file: fichier BD (.db)
    :return: objet connexion ou None
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        #On active les foreign keys
        conn.execute("PRAGMA foreign_keys = 1")
        return conn
    except sqlite3.Error as e:
        print(e)

    return None


def majBD(conn, file):
    """ execute les requetes SQL de file pour modifier la DB conn
    :param conn: objet connexion
    :param file: fichier SQL (.SQL)
    :return: 
    """
    # Lecture du fichier et placement des requetes dans un tableau
    createFile = open(file, 'r')
    createSql = createFile.read()
    createFile.close()
    sqlQueries = createSql.split(";")

    # Execution de toutes les requetes du tableau
    cursor = conn.cursor()
    for query in sqlQueries:
        cursor.execute(query)

    # commit des modifications
    conn.commit()


def get_time():
    j = datetime.now()
    return j.strftime("%d/%m/%Y - %Hh%Mm%Ss%fms")

def use(current):
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
        """
        DELETE FROM use
        """
    )
    cur.fetchall()
    conn.commit()
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO use(current_save)
        VALUES({current})
        """
    )
    cur.fetchall()
    conn.commit()
    conn.close()
    return 1

def get_use():
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT current_save FROM use
        """
    )
    current = cur.fetchall()
    conn.close()
    return current[0][0]

def sauvegardes():
    
    if afficher_joueur() != []:
        print(">>> Tu dois choisir une sauvegarde active ou en créer une pour commencer.")
        tableau = [elt for elt in afficher_joueur()]
        ids = [elt[2] for elt in afficher_joueur()]
        for elt in tableau:
            print(tableau.index(elt), "-", elt[0], "- Date : ",elt[1])
        print("Où bien tapez -1 pour en créer une autre.")
        choix_save = -2
        while choix_save not in ids and choix_save != -1:
            try:
                choix_save = int(input("Quelle sauvegarde?\n -> "))
            except ValueError:
                print("Choisissez un numéro valide...")
        if choix_save == -1:
            return len(ids)
        else:
            return choix_save
    else:
        return 0


def afficher_joueur():
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT *
        FROM Joueurs
        """
    )
    liste=cur.fetchall()
    conn.close()
    return liste


def ajout_joueur(nom, zone=404, vie=100, attaque=5, defense=0, chance=0, argent=0, arme="x", armure="x"):
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    liste_joueurs = afficher_joueur()
    if liste_joueurs != []:
        for elt in liste_joueurs:
            new_save = elt[2]
        new_save += 1
    else:
        new_save = 0
    
    cur.execute(
        f"""
        INSERT INTO Joueurs(nom, date, id_save, zone, vie, attaque, defense, chance, argent, arme, armure)\
        VALUES('{nom}', '{get_time()}', '{new_save}', '{zone}', '{vie}', '{attaque}', '{defense}', '{chance}', '{argent}', '{arme}', '{armure}');
        """
    )
    cur.fetchall()
    conn.commit()
    conn.close()
    use(new_save)
    return 1

def update_joueur(nom=Classes.nom, zone="X", vie=0, attaque=0, defense=0, chance=0, argent=0, arme_changement = False, arme="", armure_changement=False, armure=""):
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    liste_joueurs = afficher_joueur()
    if type(zone) != int:
        change_zone = False
    else:
        change_zone = True
    choix_save = get_use()
    if arme_changement == True:
        cur.execute(
        f"""
        UPDATE Joueurs
        SET arme = '{arme}'
        WHERE id_save = '{choix_save}'
        """
        )
        cur.fetchall()
        conn.commit()

    if armure_changement == True:
        cur.execute(
        f"""
        UPDATE Joueurs
        SET armure = '{armure}'
        WHERE id_save = '{choix_save}'
        """
        )
        cur.fetchall()
        conn.commit()

    if change_zone == True:
        cur.execute(
            f"""
            UPDATE Joueurs
            SET zone = '{zone}',
                vie = vie + '{vie}',
                attaque = attaque + '{attaque}',
                defense = defense + '{defense}',
                chance = chance + '{chance}',
                argent = argent + '{argent}'
            WHERE 
                id_save = '{choix_save}'
            """
        )
    else:
        cur.execute(
        f"""
        UPDATE Joueurs
        SET vie = vie + '{vie}',
            attaque = attaque + '{attaque}',
            defense = defense + '{defense}',
            chance = chance + '{chance}',
            argent = argent + '{argent}'
        WHERE 
            id_save = '{choix_save}'
        """
        )
    cur.fetchall()
    conn.commit()
    conn.close()
    return 1

def delete_profile(id):
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
        f"""
        DELETE FROM Inventaire
        WHERE id = '{id}'
        """
    )
    cur.fetchall()
    conn.commit()

    cur = conn.cursor()
    cur.execute(
        f"""
        DELETE FROM Joueurs
        WHERE id_save = '{id}'
        """
    )
    cur.fetchall()
    conn.commit()
    conn.close()
    return 1


def afficher_inventaire(classic = False):
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
        """
        SELECT *
        FROM Inventaire 
        ORDER BY nom
        """
    )
    liste = cur.fetchall()
    conn.close()

    if classic == True and liste != []:
        for i in range(len(liste)):
            print(i+1,"-",liste[i][1])
    elif liste == []:
        print("Vous n'avez rien dans votre inventaire!")
    return liste

def ajouter_inventaire(nom,quantite=1):
    liste = get_use()
    choix_save = liste
    conn = creer_connexion(DB_FILE + ".db")
    liste_inv = afficher_inventaire()
    for elt in liste_inv:
        if elt[1] == nom and elt[0] == choix_save:
            return update_inventaire(nom, quantite)
    date = get_time()
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO Inventaire(id, nom, quantite, date)\
        VALUES('{choix_save}', '{nom}', '{quantite}', '{date}');
        """
    )
    cur.fetchall()
    conn.commit()
    conn.close() 
    return 1   
    

def update_inventaire(nom ,quantite=1):
    save = get_use()
    if quantite >= 0:
        conn = creer_connexion(DB_FILE + ".db")
        cur = conn.cursor()
        cur.execute(
            f"""
            UPDATE Inventaire
            SET quantite = quantite + '{quantite}'
            WHERE nom = '{nom}' AND id = '{save}'
            """
        )
        cur.fetchall()
        conn.commit()
        conn.close()
        coherence()
        return 1    
    else:
        return delete_elt(nom)

def delete_elt(nom):
    """
    Cette fonction permet d'enlever un élément de la base de donnée gestion_stats_inventaire, dans la table Inventaire grace à un nom. 
    """
    conn = creer_connexion(DB_FILE + ".db")
    liste_objets = afficher_inventaire()
    if liste_objets == []:
        return 0
    else:
        cur = conn.cursor()
        cur.execute(
        f"""
        DELETE FROM Inventaire
        WHERE nom = '{nom}' 
        """
        )
        cur.fetchall()
        conn.commit()
        conn.close()
        coherence()
        return 1


def delete_everything():
    """
    Cette fonction permet de tout supprimer dans la table inventaire. 
    """
    conn = creer_connexion(DB_FILE + ".db")
    cur = conn.cursor()
    cur.execute(
    """
    DELETE FROM Inventaire
    """
    )
    cur.fetchall()
    conn.commit()
    conn.close()
    return 1

def recup_objet(nom, all=False):
    conn = creer_connexion(DB_FILE + ".db")

    if all==True:
        cur = conn.cursor()
        cur.execute(
        """
        SELECT * FROM Objets
        ORDER BY ind
        """
        )
        liste = cur.fetchall()
        conn.close()
        return liste   
    else:
        cur = conn.cursor()
        cur.execute(
        f"""
        SELECT * FROM Objets
        WHERE nom = '{nom}'
        """
        )
        liste = cur.fetchall()
        conn.close()
        return liste        

def recup_monstre(nom, all=False):
    conn = creer_connexion(DB_FILE + ".db")

    if all==True:
        cur = conn.cursor()
        cur.execute(
        """
        SELECT * FROM Ennemies
        ORDER BY indice
        """
        )
        liste = cur.fetchall()
        conn.close()
        return liste   
    else:
        cur = conn.cursor()
        cur.execute(
        f"""
        SELECT * FROM Ennemies
        WHERE nom = '{nom}'
        """
        )
        liste = cur.fetchall()
        conn.close()
        return liste        

def elt_save():
    id_save = get_use()
    liste_joueur = afficher_joueur()
    for elt in liste_joueur:
        if elt[2] == id_save:
            return elt

def coherence():
    #! Vérification cohérence inventaire
    conn = creer_connexion(DB_FILE + ".db")
    liste_objets = afficher_inventaire()
    for tuples in liste_objets:
        if int(tuples[2]) <= 0:
            cur = conn.cursor()
            cur.execute(
                f"""
                DELETE FROM Inventaire
                WHERE nom = '{tuples[1]}'
                """
            )
            cur.fetchall()
            conn.commit()
            conn.close()

if __name__ == "__main__":
    coherence()