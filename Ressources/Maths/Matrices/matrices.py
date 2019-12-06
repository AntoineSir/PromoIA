import numpy as np

########## Matrices carrées
def is_square(A):
    if A.shape[0] == A.shape[1]:
        return True
    else:
        return False
 
########## Trace
def trace(A):
    if A.shape[0] == A.shape[1]:
        som = 0
        for i in range(A.shape[0]):
            som += A[i,i]
        return som
    else:
        return "Pas carrée"

########## Matrices diagonales
def is_diag_pascal(A):
    if A.shape[0] == A.shape[1]:
        B = np.zeros(A.shape)
        for i in range(A.shape[0]):
            B[i,i]=A[i,i]
        print(B)
        if (A==B).all():
            return True
        else:
            return False
    else:
        raise TypeError("Matrice pas carrée")
        
def is_diag_ronan(A):
    if A.shape[0] == A.shape[1]:
        diag = True
        for i in range(A.shape[0]):
            for j in range(A.shape[0]):
                if i != j and A[i,j]!=0:
                    diag = False
                    break
        return diag
    else:
        raise TypeError("Matrice pas carrée")
        
def is_diag_romain(A):
    if is_square(A):
        diagonal = True
        i = 0
        for ligne in A:
            zeros_dans_ligne = (ligne == 0)
            if not False in zeros_dans_ligne[:i] and not False in zeros_dans_ligne[i+1:]:
                i += 1
            else:
                diagonal = False
                break
        return diagonal
    raise TypeError('matrice pas carrée')
    
def is_diag_fred(matrice):
    if is_square(matrice):
        nb1 = trace(abs(matrice))
        nb2 = sum(sum(abs(matrice)))
        if nb1 == nb2:
            return True
        else:
            return False
    else:
        return False

########## Matrices triangulaires
def is_trig_sup(A):
    if A.shape[0] == A.shape[1]:
        cpt=0
        for i in range(A.shape[0]):
            for j in range(i):
                if A[i,j]==0:
                    cpt+=1
        if cpt == (A.shape[0]**2-A.shape[0])/2:
            return True
        else:
            return False
    else:
        raise TypeError("Matrice pas carrée")

########## Produit matriciel
def coef_prod(A,B,i,j):
    if A.shape[1]==B.shape[0]:
        c_ij=0
        for k in range(A.shape[1]):
            c_ij += A[i,k]*B[k,j]
        return c_ij
    else:
        return 'Produit impossible'

A = np.array([[1,2,3],[0,2,3],[0,0,3]])
B = A.T+4*np.ones((3,3))
I = np.eye(A.shape[0])
#test produit matrice avec identité
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        print(coef_prod(A,I,i,j))





M = np.arange(1, 21).reshape((4,5), order='F')
print(M)

idx_row = [1, 2, 0]
idx_col = [1, 4, 2]
#la méthode suivante marche pas car Python créé 3 couples en fonction de 2 listes
print("FAUX:",M[idx_row, idx_col])

#une première méthode qui marche
print(M[idx_row][:,idx_col])

#une seconde méthode qui marche
idx = np.ix_(idx_row, idx_col)
print(idx)
print(M[idx])