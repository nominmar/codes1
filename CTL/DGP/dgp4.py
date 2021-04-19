import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def dgp4(n):
    np.random.seed()
    p=[1./2, 1./2]
    d = np.random.choice([0, 1], size=(n,1), p=p)
    x1 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x2 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x3 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x4 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))    
    e = np.random.normal(loc = 0.0, scale = 1.5, size = (n,1))
    #print(x1)
    ind = np.zeros((n,1))
    #print(d)
    ind[np.where(x1 >= 0)] = 1
    #print(ind)
    y1 = np.add(d*-1, np.multiply(2, np.multiply(ind,d)))
    #print(y1)
    y2 = np.add(y1, x2)
    y3 = np.add(y2, x3)
    y4 = np.add(y3, x4)
    y = np.add(y4, e)



    X = np.concatenate((x1,x2), axis=1)
    X = np.concatenate((X,x3), axis=1)
    X = np.concatenate((X,x4), axis = 1) #covariates

    #X = np.concatenate((X,d), axis = 1)
    x_train, x_test, y_train, y_test, treat_train, treat_test = train_test_split(X, y, d, test_size=0.5)

    return x_train, x_test, y_train, y_test, treat_train, treat_test