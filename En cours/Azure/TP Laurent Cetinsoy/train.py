from sklearn.linear_model import LinearRegression
from azureml.core.run import Run
import numpy as np
import os
import pickle

run = Run.get_context()

def main():
    X = np.random.randn(10, 3)
    y = np.sum(X, axis=1) + np.random.rand(10)*10**-2


    model = LinearRegression()
    print('training')
    model.fit(X, y)
    print('done')
    run.log("r2 coefficient", model.score(X, y))
    run.log("MSE", np.mean((y-model.predict(X))**2))
    
    os.makedirs('./outputs', exist_ok=True)    
    with open('outputs/monsupermodel.pkl', 'wb') as f:
        pickle.dump(model, f)
        
if __name__ == "__main__":
    main()