import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt5

# Données générées aléatoirement avec sklearn
from sklearn.datasets import make_regression
x, y = make_regression(n_samples = 100, n_features = 1, noise = 10)
y = y.reshape(y.shape[0],1)
# On veut des données non-linéaires donc il faut modifier un peu y
y = y**2 + 2 * y + abs(y/2) 
plt.scatter(x,y)

# Matrice X
X = np.hstack((x**2,x,np.ones(x.shape)))

# Initialisation theta
theta = 50*np.random.randn(3,1)

# Modèle
def model(X,theta):
    return X @ theta

# Fonction de coût
def cout(X,y,theta):
    return 1/(2*len(y))*np.sum((model(X,theta)-y)**2)
    #return 1/(2*len(y))*(model(X,theta)-y).T @ (model(X,theta)-y)

# Calcul du gradient
def grad(X,y,theta):
    return 1/(len(y))*X.T @ (model(X,theta)-y)
    
# Descente de gradient
def desc_grad(X,y,theta,alpha=0.01,n_max=1000):
    couts = np.zeros(n_max)
    for i in range(n_max):        
        theta = theta - alpha * grad(X,y,theta)
        couts[i]=cout(X,y,theta)
    return theta, couts

# Solution exacte au problème
def sol_exacte(X,y):
    return np.linalg.inv(X.T @ X) @ X.T @ y

# Optimisation : recherche du meilleur theta
theta_hat, couts = desc_grad(X,y,theta,alpha=0.01,n_max=500)

print(theta_hat,sol_exacte(X,y))

# Tri des données pour l'affichage
data_plt = np.hstack((x,model(X,theta_hat)))
data_plt = np.array(sorted(data_plt, key = lambda x: x[0]))

# Visualisation
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,8))
ax1.scatter(x,y)
ax1.plot(data_plt[:,0], data_plt[:,1],c='red')
ax2.plot(couts)


# Évaluation de la régression avec le coefficient R²
def R_2(y,y_pred):
    num = np.sum((y-y_pred)**2)
    den = np.sum((y-np.mean(y))**2)
    return 1-num/den

print(R_2(y,model(X,theta)))

