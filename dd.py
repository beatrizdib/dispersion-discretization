import numpy as np

class DispersionDiscretization:
    def __init__(self):
        pass
    #index_list must be a list containing the index numbers from each column from the array to be modified
    #X must be an array typed in the format of a list, in which each list within the main list must be a line of the array
    #y must be a number which the standard deviation from each column will be divided by
    def fit (self, X, index_list, y):
        mean_list = []
        sd_list = []
        y_list =[]
        Xlinha = np.array(X)
        i=0
        for e in index:
            i=+1
            m = np.mean(Xlinha[:,e])
            sd = np.std(Xlinha[:,e])
            w =sd/(y[i])
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