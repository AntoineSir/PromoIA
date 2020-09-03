from sklearn.linear_model import LinearRegression
from azureml.core.run import Run
from azureml.core import Model
import numpy as np
import os
import pickle
import time

timestr = time.strftime("%Hh%M")

run = Run.get_context()
ws = Run.get_context().experiment.workspace

def main():
    X = np.random.randn(10, 3)
    y = np.sum(X, axis=1) + np.random.rand(10)*10**-2

    model = LinearRegression()
    print('training')
    model.fit(X, y)
    print('done')
    run.log("r2 coefficient", model.score(X, y))
    run.log("MSE", np.mean((y-model.predict(X))**2))
    
    model_name = 'regmodel_' + timestr + '.pkl'
    with open(model_name, 'wb') as f:
        pickle.dump(model, f)
        
    Model.register(ws, './' + model_name, "regression_pipeline_model")
        
if __name__ == "__main__":
    main()