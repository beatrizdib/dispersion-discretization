import numpy as np

class DispersionDiscretization:
    def __init__(self):
        pass
    def fit (self, X):
        Xlinha = np.array(X)
        print Xlinha
        print 
        print np.mean(Xlinha[:,0])

dd = DispersionDiscretization()
X = [[1,2,3],[3,2,2],[3,2,2],[3,2,2]]
dd.fit(X)