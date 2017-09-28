import numpy as np

class DispersionDiscretization:
    def __init__(self):
        pass
    #index must be a list containing the index numbers from each column to be selected from the array, and X must be an array in the format of a list, in which each list within the main list must be a line of the array
    def fit (self, X, index, y):
        mean_list = []
        sd_list = []
        y_list =[]
        Xlinha = np.array(X)
        i=0
        for e in index:
            i=+1
            m = np.mean(Xlinha[:,e])
            sd = np.std(Xlinha[:,e])
            w =(y[i])*sd
            y_list.append(w)
            mean_list.append (m)
            sd_list.append (sd)
        print mean_list
        print sd_list
        print y_list
        #print np.mean(Xlinha[:,0])

dd = DispersionDiscretization()
X = [[1,2,3],[3,2,2],[3,2,2],[3,2,2]]
dd.fit(X, [1, 2], [1,0.5])