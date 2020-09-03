############## algo 1 ############## 
#1
for i in range(0,10,2):
    print(i)

#2
k=1    
while k<10:
   print(k)
   k+=1
   
############## algo 2 ##############
def swap(a,b):
    c=a
    a=b
    b=c
    return a,b

a = 2
b = 'trois'

a,b = swap(a,b)

print(a,' et ',b)


############## algo 3 ##############
import string

#1
abc = list(string.ascii_lowercase)
abc.reverse()
for l in abc:
    print(l)
    
#2
abc = list(string.ascii_lowercase)
for i in range(len(abc)):
    lettre = abc.pop()
    print(lettre)

#3
abc = string.ascii_lowercase
i = len(abc)
while i > 0:
    print(abc[i-1])
    i-=1
    
#4
abc = string.ascii_lowercase
abc = abc[::-1]
print(abc)


############## algo 4 ##############
def fibo_i(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

f10 = fibo_i(10)
print(f10)


############## algo 5 ##############
#1
def fibo_r1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_r1(n-1)+fibo_r1(n-2)
    
#2    
def fibo_r2(n):
    if n<2:
        return n
    else:
        return fibo_r2(n-1)+fibo_r2(n-2)
    
print(fibo_r1(10),fibo_r2(10))


############## algo 6 ##############
#1
cpt = 0
for d1 in range(10):
    for u1 in range(10):
        for d2 in range(10):
            for u2 in range(10):
                if d1*10 + u1 >= d2*10 + u2:
                    pass
                else:
                    print(str(d1)+str(u1),' ',str(d2)+str(u2),',',sep='')
                    cpt += 1
cpt
#le compteur sert juste à s'assurer qu'on a le bon nombre de combinaisons
#le nombre de combinaisons de 2 éléments parmi 100 étant de 4950


############## algo 7 ##############
def epeler(mot):
    for l in mot:
        print(l)

epeler('salut')

############## algo 8 ##############
mot= 'salut a vous la promo IA'

#1
dic={}
for l in mot:
    if l in dic:
        dic[l]+=1
    else:
        dic[l]=1
print(dic)

#2
dic2={}
for l in mot:
    dic2[l]=mot.count(l)
print(dic2)


############## algo 9 ##############
def nombre(inf=10,sup=20):
    nb = eval(input("Entrez un nombre : "))
    if nb > sup:
        print('Plus petit !')
        nombre(inf,sup)
    elif nb < inf:
        print('Plus grand !')
        nombre(inf,sup)
    else:
        print('Très bien')
        
nombre()


############## algo 10 ##############
def aire_triangle(b,h):
    return (b*h)/2

aire_triangle(3,4)


############## algo 11 ##############
def total_ttc(quantite,prix,tva):
    return prix*quantite*(1+tva)/100

total_ttc(12, 88, 19.8)


############## algo 12 ##############
#1
def moyenne(notes,poids):
    somme=0
    somme_p=0
    for i in range(len(notes)):
        somme += notes[i]*poids[i]
        somme_p += poids[i]        
    return somme/somme_p*5 #*5 pour exprimer en pourcentage

notes=[10,14,18]
poids=[1,3,2]
moyenne(notes,poids)

#2
def moyenne2(notes,poids):
    liste=[]
    for i in range(len(notes)):
        liste.append(notes[i]*poids[i])
    return sum(liste)/sum(poids)*5 #*5 pour exprimer en pourcentage

notes=[10,14,18]
poids=[1,3,2]
moyenne2(notes,poids)


############## algo 13 ##############
#1
def som_dig(a):
    som = 0
    a=str(a)
    for i in range(len(a)):
        som+=int(a[i])
    return som
som_dig(1457)

#2
def som_dig2(a):
    return sum([int(i) for i in str(a)])
som_dig2(1457)

#3 sans la conversion en string, pour un nombre à 3 chiffres
def som_dig3(a):
    c = a//100
    d = (a-c*100)//10
    u = a-c*100-d*10
    return c+d+u
som_dig3(123)

#4 sans la conversion en string en généralisant
def som_dig4(a):
    i_max = 1
    while a % 10**i_max != a:
        i_max+=1
    
    chiffres = []
    for k in range(i_max,0,-1):
        coef = a//(10**(k-1))
        chiffres.append(coef)
        a -= coef*10**(k-1)
    
    return sum(chiffres)

l=[6,15,89,123,999,1005,9999,15032]
for i in l:
    print(som_dig4(i))
    
#4 encore une autre méthode (celle de Pierre-Vincent)
def som_dig5(a):
    som = 0
    while a != 0:
        som += a % 10
        a = int((a-a%10)/10)
    return som

        
####### Bonus somme et factorielle #######
#somme
def som_i(n):
    res = 0
    for nb in range(1,n+1):
        res += nb
    return res

def som_r(n):
    if n==0:
        return 0
    else:
        return n+som_r(n-1)

#factorielle
def fac_i(n):
    res = 1
    for nb in range(1,n+1):
        res *= nb
    return res

def fac_r(n):
    if n==0:
        return 1
    else:
        return n*fac_r(n-1)


