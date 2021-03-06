import numpy as np

class Vetor:
    
    def __init__(self, X):
        self.__X = X
        
    @property
    def vetor(self):
        return self.__X
    
    @property
    def dim(self):
        return np.shape(self.__X)[0]
        
    #Norma 1 de vetor.
    def norma1(self):
        n = 0 
        mod_x = np.abs(self.__X)
        for i in range(np.shape(self.__X)[0]):
            n = n + mod_x[i]
        return n
    
    #Norma 2 de vetor.
    def norma2(self):
        n = 0 
        b = self.__X.max()
        if b == 0:
            n = 0
        else:
            x = (1/b)*self.__X
            for i in range(np.shape(self.__X)[0]):
                n = n + x[i]**2
            n = b*n**(1/2)
        return n