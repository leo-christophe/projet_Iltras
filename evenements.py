from random import randint
from random import shuffle
import csv
import codecs

def obj():
    T_obj_1=[]
    with codecs.open('liste_objets.csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=',')
        for row in r:
            T_obj_1.append(dict(row))
        return T_obj_1

#un coffre apparait...
def chest(zone):
    objets = obj()
    zone_minimum = zone
    coffre_loot= [e['ind'] for e in objets if int(e['cof']) == 1]
    objet = 0
    while objet != 1:
        shuffle(coffre_loot)
        for e in range(0,len(coffre_loot)-1):
            if zone_minimum == 111 or zone_minimum == 112 or zone_minimum == 113:
                zone_minimum = 1     
            if (int(objets[int(coffre_loot[e])]['ctl']) > randint(0,100)) and (int(objets[int(coffre_loot[e])]['zon_min']) <= zone_minimum):
                return coffre_loot[e]
