import numpy as np

class DispersionDiscretization:
    def __init__(self):
    	pass
    #index_list must be a list containing the index numbers from each column from the array to be modified
    #X must be an array typed in the format of a list, in which each list within the main list must be a line of the array
    #lmbda_list must be a list containing numbers which the standard deviation from each column correspondent to their index will be divided by
    def fit (self, X, index_list, lmbda_list):
        #Handling Exceptions and Errors:
        if not type (X) is list:
        	raise (ValueError ("X must be a list"))
        if not type (index_list) is list:
        	raise (ValueError ("index_list must be a list"))
        if not type (lmbda_list) is list:
        	raise (ValueError ("lmbda_list must be a list"))
        for i in xrange(len(X)):
            for j in xrange(len(X[i])):
                if not (type(X[i][j]) is float or type(X[i][j]) is int):
                    raise(ValueError("All elements in array X must be integers or floats"))
        for e in index_list:
            if not (type(e) is int or type(e) is float):
                raise (ValueError("All indices must be integers or floats"))
        for e in lmbda_list:
            if not (type(e) is int or type(e) is float):
                raise (ValueError("All lmbdas must be integers or floats"))
            if e == 0:
            	raise (ZeroDivisionError("lmbda must not be 0"))
        for i in xrange(len(X)):
            if len(X[i]) != len(X[0]):
                raise(IndexError("All lines in the array must have the same length"))
        for e in index_list:
            if e>len(X):
                raise(IndexError("Index "+str(e)+" is out of range for array X:"+str(X)))
        if len(index_list)!=len(lmbda_list):
            raise IndexError("lmbda list must have the same length as index list")
        for i in xrange(len(index_list)):
        	for j in xrange(len(index_list)):
        		if i!=j:
        			if index_list[i]==index_list[j]:
        				raise (ValueError("All indices in index_list must be different"))
        

        mean_list = []
        sd_list = []
        lmbdaxsd_list =[]
        Xlinha = np.array(X)
        i=0
        for e in index_list:
            i=+1
            m = np.mean(Xlinha[:,e])
            sd = np.std(Xlinha[:,e])
            w =sd/(lmbda_list[i])
            lmbdaxsd_list.append(w)
            mean_list.append (m)
            sd_list.append (sd)
        print mean_list
        print sd_list
    	self.sd = sd_list
    	self.mean = mean_list
    	self.lmbda = lmbda_list
    	self.lmbdaxsd = lmbdaxsd_list

    def transform(self, X):
    	l=[]
    	for i in xrange(len(self.lmbda)):
    		l1=[]
    		for e in range(((-self.lmbda[i])-1),((self.lmbda[i])+2)):
    			if e <0:
    				if (self.lmbdaxsd[i])<=e:
    					l1.append(1)
    				else:
    					l1.append(0)
    			else:
    				if self.lmbdaxsd[i]>=e:
    					l1.append(1)
    				else:
    					l1.append(0)
    		l.append(l1)
    	print l







if __name__ == '__main__':

	dd = DispersionDiscretization()
	X=[[1,2,3],[4,7,8],[2,3,3]]
	dd.fit(X,[1,2],[2,1])
	dd.transform(X)



