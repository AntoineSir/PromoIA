""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""" EXERCICES DE BASE PYTHON """""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



""""""""""""
""" Exo1 """
""""""""""""
from math import *

def impairs(a,b):
    a = ceil(a)
    b = floor(b)
    #res = ''
    for i in range(a,b+1):
        if i % 2 == 1:
            print(i,end=' ')
            #res += str(i)+' '
    #print(res)
impairs(12.3,26.9)



""""""""""""
""" Exo2 """
""""""""""""
##### La solution vue ensemble
import random
nb_a_trouver = random.randint(1,100)
nb = -1
while nb != nb_a_trouver:
    nb = eval(input("Entrer un nombre : "))
    if nb > nb_a_trouver:
        print("Trop grand")
    elif nb < nb_a_trouver:
        print("Trop petit")
    elif nb == nb_a_trouver:
        print("Bravo")
    else:
        print("erreur de nombre")

##### Une solution possible plus complète
def joueurs_et_scores():
    nb_joueurs = eval(input("Combien de joueurs êtes-vous ? "))
    scores = {}
    joueurs = []
    if nb_joueurs > 2:
        print(f"C'est 2 maximum donc y en a {nb_joueurs-2} qui vont regarder...")
    for i in range(min(nb_joueurs,2)):
        nom = input(f"Entrez un nom pour le joueur {i+1} : ")
        joueurs.append(nom.upper())
        scores[joueurs[i]] = 0       
    return scores, joueurs       

def deviner(joueur,diff):
    tentative = eval(input(f"{joueur}, veuillez entrer un nombre : "))
    while tentative > diff or tentative < 1:
        print(f"Non ça doit être un nombre entier entre 1 et {diff}")
        return deviner(joueur,diff)
    return tentative

def plus_ou_moins():    
    scores, joueurs = joueurs_et_scores()
    diff =  20*eval(input("Choisissez un niveau de difficulé entre 1 (très facile) et 5 (très difficile) : "))
    continuer = 'o'
    num_joueur = 0
    
    while continuer == 'o':
        joueur_actuel = joueurs[num_joueur]
        print(f"\n\n C'est à {joueur_actuel} de deviner")
        nb_a_trouver = random.randint(1,diff)
        tentative = deviner(joueur_actuel,diff)
        cpt = 1
        while tentative != nb_a_trouver:
            if tentative > nb_a_trouver:
                print("C'est trop grand")
            elif tentative < nb_a_trouver:
                print("C'est trop petit")
            tentative = deviner(joueur_actuel,diff)
            cpt+=1
        print(f"Bravo c'est ça ! T'as trouvé en {cpt} coups")
        scores[joueur_actuel]+=cpt
        print(f"Vos scores sont de {scores}")
        continuer =  input("Vous voulez continuer ? (o/n) ")
        num_joueur = (num_joueur + 1)%2
    
    try:
        if scores[joueurs[0]]>scores[joueurs[1]]:
            print(f"Victoire écrasante de {joueurs[0]} sur le score de {scores[joueurs[0]]} à {scores[joueurs[1]]}")
        elif scores[joueurs[1]]>scores[joueurs[0]]:
            print(f"Victoire écrasante de {joueurs[1]} sur le score de {scores[joueurs[1]]} à {scores[joueurs[0]]}")
        else:
            print("C'est un beau match nul")
    except:
        print(f"Ton score final est de {scores[joueurs[0]]}")



""""""""""""
""" Exo3 """
""""""""""""
import random
def genere(n=100,a=0,b=1000):
    liste = []
    for i in range(n):
        liste.append(random.randint(a,b))
    return liste

def les_n_plus_grands(liste,nb=10):
    best = []
    for i in range(10):
        maxi = max(liste)
        best.append(maxi)
        liste.remove(maxi)
    return best
les_n_plus_grands(genere())



""""""""""""
""" Exo4 """
""""""""""""
import random
l = [i for i in range(50)]+[i for i in range(21,78) if i%2==1]
random.shuffle(l)

### algo 1: en utilisant la fonction min
def tri_max(liste):
    tri = []
    for i in range(len(liste)):
        tri.append(min(liste))
        liste.pop(liste.index(min(liste)))
    return tri

### algo 2: le tri insertion
def tri_ins(liste):
    for i in range(1,len(liste)):
        tmp = liste[i]
        j = i
        while j>0 and tmp < liste[j-1]:
            liste[j] = liste[j-1]
            j-=1
        liste[j]=tmp
    return liste

### algo 3: le tri rapide ou tri quicksort ou tri par partitionnement
def tri_qck(liste):
    if liste == []:
        return []
    else:
        pivot_ind = random.randint(0,len(liste)-1)
        pivot = liste[pivot_ind]
        l1 = []
        l2 = []
        l = liste[0:pivot_ind]+liste[pivot_ind+1:len(liste)]
        for val in l :
            if val < pivot:
                l1.append(val)
            else:
                l2.append(val)
        return tri_qck(l1)+[pivot]+tri_qck(l2)

### algo 4: le tri fusion
def fusion(l1,l2):
    n1,n2 = len(l1),len(l2)
    l = [0]*(n1+n2)
    i1,i2,i = 0,0,0
    while i1<n1 and i2<n2:
        if l1[i1] < l2[i2]:
            l[i] = l1[i1]
            i1 += 1
        else:
            l[i] = l2[i2]
            i2 += 1
        i += 1
    while i1<n1:
    	l[i] = l1[i1]
    	i1 += 1
    	i += 1
    while i2<n2:
    	l[i] = l2[i2]
    	i2 += 1
    	i += 1 
    return l

def tri_fus(liste):
    n = len(liste)
    if n > 1:
        m = n//2
        l1 = liste[:m]
        l2 = liste[m:n]
        tri_fus(l1)
        tri_fus(l2)
        liste[:] = fusion(l1,l2)
        
### algo 5: le tri à bulles
def tri_bul(liste):
    permut = True
    k = 0
    while permut == True:
        k+=1
        permut = False
        for i in range(0,len(liste)-k):
            if liste[i] > liste[i+1]:
                permut = True
                liste[i],liste[i+1]=liste[i+1],liste[i]
    return liste

### comparaison des temps d'exécution
import time
durees = {}
fonctions = ['tri_max','tri_ins','tri_qck','tri_fus','tri_bul']
for i in range(5):     
    l = genere(10000,0,100)
    tri = eval(fonctions[i])
    debut = time.time()
    tri(l)
    durees[fonctions[i]] = time.time() - debut
durees
