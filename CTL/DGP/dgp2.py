import pandas as pd
import numpy as np

def dgp2(n):
    
    p=[1./2, 1./2]
    d = np.random.choice([0, 1], size=(n,1), p=p)
    x1 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x2 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x3 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x4 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))    
    e = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    #print(x1)
    ind = np.zeros((n,1))
    #print(d)
    ind[np.where(x1 >= 0)] = 1
    #print(ind)
    y1 = np.add(d*-1, np.multiply(2, np.multiply(ind,d)))
    #print(y1)
    y2 = np.add(y1, x2)
    y3 = np.add(y2, x3)
    y4 = np.add(y2, x4)
    y = np.add(y4, e)



    X = np.concatenate((x1,x2), axis=1)
    X = np.concatenate((X,x3), axis=1)
    X = np.concatenate((X,x4), axis = 1)
    X = np.concatenate((X,d), axis = 1)
    return X, y