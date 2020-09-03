### import de librairies
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
%matplotlib qt5

###############################################################################
def derive(f,a):
    h=1e-10
    return (f(a+h)-f(a-h))/(2*h)

###############################################################################
def desc_grad(f, alpha = 0.05, epsilon = 0.001, imax = 1000,
              inf=-10, sup=10): #inf et sup pour l'échelle de variation de "x"
    
    a = uniform(inf,sup)  
    d = derive(f,a)
    i = 0

    Iplot, Aplot  = [i], [a]
    
    while abs(d) > epsilon and i<imax : #i<imax pour stoper la boucle si besoin
        a -= alpha*d
        d = derive(f,a)
        i+=1       
        Iplot.append(i)
        Aplot.append(a)

    return Iplot, Aplot


###############################################################################
##########        CALCUL DU GRADIENT DE AFFICHAGE DES COURBES        ##########
###############################################################################


#fonctions à tester
#f = lambda x : x**2 - x + 1
#f = lambda x : (x-1)*(x-2)*(x-3)*(x-5)
#f = lambda x : 2 * x * x * np.cos(x) - 5 * x
#f = lambda x : x * np.cos(x)
f = lambda x : np.arctan(x*x)

#descente de gradient et stockage des résultats
Iplot, Aplot = desc_grad(f,alpha = 0.05, inf=-5,sup=5)

#calcul des images par f des différents points de la descente de gradient
FAplot = list(map(f,Aplot))

#initialisation des graphiques
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(18,10))
scat1 = ax1.scatter([],[], c='red')
scat2 = ax2.scatter([],[], c='red')


#tracé de la courbe de la fonction f sur le premier sous-graphique
Xplot = np.linspace(-10, 10, 100)
ax1.plot(Xplot,list(map(f,Xplot)))

#fonction de mise à jour des graphiques
def update_scat(i):
    a_i = Aplot[:i] #pour afficher uniquement les i premiers éléments
    i_i = Iplot[:i] #mettre [:i:2] pour avoir un point sur 2 par exemple
    fa_i = FAplot[:i]
    scat1.set_offsets(np.c_[a_i,fa_i]) #mise à jour des données des graphiques
    scat2.set_offsets(np.c_[i_i,fa_i]) #
    #ajout de titre et infos sur les graphiques
    ax1.set_title(f'dernière valeur prise par x : {Aplot[i]}', size = 16)
    ax2.set_title(f'dernière valeur prise par f(x) : {FAplot[i]}', size = 16)
    fig.suptitle(f'itération {i} et bon anniversaire Fred !', size=50)

  
#échelles des axes : limites dépendant des valeurs des positions et de f 
ax1.set(xlim=(min(Aplot)-5,max(Aplot)+5),ylim=(min(FAplot)-1,max(FAplot)+1))
ax2.set(xlim=(0,len(Iplot)),ylim=(min(FAplot)-1,max(FAplot)+1))
    
#tracé des graphiques
anim = animation.FuncAnimation(fig, update_scat, interval=100)
plt.show()


