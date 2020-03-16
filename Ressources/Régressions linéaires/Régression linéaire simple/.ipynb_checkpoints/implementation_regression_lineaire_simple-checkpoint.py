import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt5

# Données au choix (tester pour les 2)
#data = np.genfromtxt('salaires.csv',delimiter=',',skip_header=True)
#x = data[:,:-1]
#y = data[:,-1:]

#possibilité de générer des données aléatoirement avec sklearn
from sklearn.datasets import make_regression
x, y = make_regression(n_samples = 100, n_features = 1, noise = 10)
y = y.reshape(y.shape[0],1)
plt.scatter(x,y)

# Matrice X
X = np.hstack((x,np.ones(x.shape)))

# Initialisation theta
theta = 50*np.random.randn(2,1)

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
theta_hat, couts = desc_grad(X,y,theta,alpha=0.05,n_max=500)

print(theta_hat,sol_exacte(X,y))

# Visualisation
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,8))
ax1.scatter(x,y)
ax1.plot(x,model(X,theta_hat),c='red')
ax1.plot(x,model(X,sol_exacte(X,y)),c='green')

ax2.plot(couts)

# Évaluation de la régression avec le coefficient R²
def R_2(y,y_pred):
    num = np.sum((y-y_pred)**2)
    den = np.sum((y-np.mean(y))**2)
    return 1-num/den

