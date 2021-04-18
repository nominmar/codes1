import numpy as np

def dgp1(n):
    p=[1./2, 1./2]
    x1 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x2 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x3 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))
    x4 = np.random.normal(loc = 0.0, scale = 1.0, size = (n,1))    
    e = np.random.normal(loc = 0.0, scale = 0.1, size = (n,1))
    d = np.random.choice([0, 1], size=(n,1), p=p)

    
    t1 = np.subtract(d*2, np.ones((n,1))) #treatment effect sign
    t2 = np.multiply(t1, x1) #treatment effect w relevant var    
    
    y1 = np.add(t2, x2)
    y2 = np.add(y1, x3)
    y3 = np.add(y2, x4)
    y = np.add(y3, e)
    
    
    
    X = np.concatenate((x1,x2), axis=1)
    X = np.concatenate((X,x3), axis=1)
    X = np.concatenate((X,x4), axis = 1)
    X = np.concatenate((X,d), axis = 1)
    
    return X, y