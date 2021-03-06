import numpy as np
import sys

class QR:

    def __init__(self,A):
        self.__A = A

    def rotacoes(self):
        m = np.shape(self.__A)[0] #Número de linhas de A
        n = np.shape(self.__A)[1] #Número de colunas de A

        if(m<n):
            sys.stderr.write("ERRO: a matriz não admite fatoração QR.")
            input()
            sys.exit()

        Q = np.identity(m, dtype=float) #Q^t
        R = A.astype('float')

        for i in range(n):
            for j in range(i+1, m):
                if(R[j,i] == 0): #A matriz de rotação é a identidade.
                    continue
                
                #Cálculo do cos() e sin()
                N = max([abs(R[i,i]),abs(R[j,i])]) #Fator de Normalização
                a = R[i,i]/N
                b = R[j,i]/N
                v = (a**2 + b**2)**0.5

                c = a/v #cos
                s = b/v #sin

                #Produto das matrizes
                #Matriz R
                Li = c*R[i] + s*R[j]
                Lj = c*R[j] - s*R[i]
                R[i] = Li.copy()
                R[j] = Lj.copy()

                #Matriz Q
                Li = c*Q[i] + s*Q[j]
                Lj = c*Q[j] - s*Q[i]
                Q[i] = Li.copy()
                Q[j] = Lj.copy()
                
        return Q.transpose(), R