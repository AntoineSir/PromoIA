import numpy as np
import matplotlib.pyplot as plt

%matplotlib qt5

# Pour pouvoir reproduire l'aléatoire
np.random.seed(42)

# Données d'un dataset au choix apparts.csv ou entreprises.csv
#data = np.genfromtxt('apparts.csv',delimiter=',',skip_header=True)
#x = data[:,:-1]
#y = data[:,-1:]

# Données générées aléatoirement avec sklearn
from sklearn.datasets import make_regression
x, y = make_regression(n_samples=100, n_features=2, noise = 10)
y = y.reshape((y.shape[0],1))

# 2 variables donc on peut visualiser le nuage de points en 3D
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[:,0], x[:,1], y) 
ax.set_xlabel('x_1')
ax.set_ylabel('x_2')
ax.set_zlabel('y')
plt.show()

# Matrice X
X = np.hstack((x,np.ones((x.shape[0],1))))

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

# Visualisation
x1 = x[:,0]
x2 = x[:,1]
pred = model(X,theta_hat).reshape((len(y),))

fig = plt.figure()

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(336)

ax1.scatter(x1, x2, y, s =30, c='red') 
ax1.plot_trisurf(x1, x2, pred,cmap="inferno")
ax1.set_xlabel('x_1')
ax1.set_ylabel('x_2')
ax1.set_zlabel('y')

ax2.scatter(x1, x2, pred,color="green")
ax2.set_xlabel('x_1')
ax2.set_ylabel('x_2')
ax2.set_zlabel('y')

# Courbe d'apprentissage
ax3.plot(couts)

plt.show()

# Évaluation de la régression avec le coefficient R²
def R_2(y,y_pred):
    num = np.sum((y-y_pred)**2)
    den = np.sum((y-np.mean(y))**2)
    return 1-num/den

print(R_2(y,model(X,theta_hat)))

