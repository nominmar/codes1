import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def dgp4(n, var_e):
    np.random.seed()
    p=[1./2, 1./2]
    d = np.random.choice([0, 1], size=(n,1), p=p)
    x1 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x2 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x3 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x4 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))    
    e = np.random.normal(loc = 0.0, scale = var_e, size = (n,1))

    ind = np.zeros((n,1))
    ind[np.where(x1 >= 0)] = 1
    y = np.add(np.add(np.add(np.add(np.add(d*-1.5, np.multiply(3*d, ind)),x2),x3),x4),e)

    X = np.concatenate((x1,x2,x3,x4), axis=1)


    #X = np.concatenate((X,d), axis = 1)
    x_train, x_test, y_train, y_test, treat_train, treat_test = train_test_split(X, y, d, test_size=0.5)

    return x_train, x_test, y_train, y_test, treat_train, treat_test