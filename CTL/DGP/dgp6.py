import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def dgp6(n, var_e):
    np.random.seed()
    #treatment (randomly assigned)
    d = np.random.choice([0, 1], size=(n,1), p=[1./2, 1./2])
    #covariates (relevate to T.E.)
    x1 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x2 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    #covariates (relevant to outcome)
    x3 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x4 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x5 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    #covariates (irrelevant)
    x6 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    #error term
    e = np.random.normal(loc = 0.0, scale = var_e, size = (n,1))

    #indicator functions
    ind1 = np.zeros((n,1))
    ind2 = np.zeros((n,1))
    ind1[np.where(x1 >= 0)] = 1
    ind2[np.where(x2 >= 0)] = 1

    y = np.add(np.add(np.add(np.add(np.add(d*-2, np.multiply(np.add(3*ind1, ind2),d)),x3),x4),x5),e)
    X = np.concatenate((x1,x2,x3,x4,x5,x6), axis=1)
    
    x_train, x_test, y_train, y_test, treat_train, treat_test = train_test_split(X, y, d, test_size=0.5)
    
    return x_train, x_test, y_train, y_test, treat_train, treat_test

#x_train, x_test, y_train, y_test, treat_train, treat_test = dgp6(100000, 0.01)

#x1 = x_test[:,0].reshape(-1,1)
#x2 = x_test[:,1].reshape(-1,1)
#d = treat_test[:,0].reshape(-1,1)
#y = y_test[:,0].reshape(-1,1)
#print(np.mean(y[np.where((x1 >= 0) & (x2 >= 0) & (d == 1))]) - np.mean(y[np.where((x1 >= 0) & (x2 >= 0) & (d == 0))]))
#print(np.mean(y[np.where((x1 >= 0) & (x2 < 0) & (d == 1))]) - np.mean(y[np.where((x1 >= 0) & (x2 < 0) & (d == 0))]))
#print(np.mean(y[np.where((x1 < 0) & (x2 >= 0) & (d == 1))]) - np.mean(y[np.where((x1 < 0) & (x2 >= 0) & (d == 0))]))
#print(np.mean(y[np.where((x1 < 0) & (x2 < 0) & (d == 1))]) - np.mean(y[np.where((x1 < 0) & (x2 < 0) & (d == 0))]))