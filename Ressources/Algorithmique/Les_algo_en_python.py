### algo 1
for i in range(0,10,2):
    print(i)

k=1    
while k<10:
   print(k)
   k+=1
   
### algo 2
def swap(a,b):
    c=a
    a=b
    b=c
    return a,b

a = 2
b = 'trois'

a,b = swap(a,b)

print(a,' et ',b)


### algo 3
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


### algo 4
def fibo_i(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

f10 = fibo_i(10)
print(f10)


### algo 5
def fibo_r1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_r1(n-1)+fibo_r1(n-2)
    
def fibo_r2(n):
    if n<2:
        return n
    else:
        return fibo_r2(n-1)+fibo_r2(n-2)
    
print(fibo_r1(10),fibo_r2(10))


### algo 6
for u1 in range(10):
    for d1 in range(10):
        for u2 in range(10):
            for d2 in range(10):
                print(str(u1)+str(d1),' ',str(u2)+str(d2),',')

### algo 7
def epeler(mot):
    for l in mot:
        print(l)

epeler('salut')

### algo 8
mot= 'salut a vous la promo IA'

dic={}
for l in mot:
    if l in dic:
        dic[l]+=1
    else:
        dic[l]=1
print(dic)

dic2={}
for l in mot:
    dic2[l]=mot.count(l)
print(dic2)


### algo 9
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


                

    