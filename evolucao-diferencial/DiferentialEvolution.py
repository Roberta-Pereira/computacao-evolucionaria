import random as rd
import numpy as np
from itertools import product

def peaks(x): 
    x = x.T
    F = 3*(1-x[0])**2 * np.exp(-(x[0]**2) - (x[1]+1)**2) - 10*(x[0]/5 - x[0]**3 - x[1]**5) * np.exp(-x[0]**2-x[1]**2) - 1/3*np.exp(-(x[0]+1)**2 - x[1]**2)
    return F,x[0],x[1]

def rastrigin(x):  
    x = x.reshape(1, -1).T
    Q = np.eye(len(x))
    X = Q.dot(x)

    n = len(X)
    F = 0
    
    for i in range(n):
        F = F + X[i]**2 - 10*np.cos(2*np.pi*X[i])
    
    return F[0],float(X[0]),float(X[1])

def main_loop(funcao):
    t = 1

    x1 = x2 = np.linspace(-2, 2, 10)
    X = np.array(list(product(x1,x2)))  #população inicial de soluções candidatas

    N, n = X.shape                      #quantidade de soluções candidatas e variaveis de decisão
    u = np.zeros_like(X)

    C = rd.uniform(0.6, 0.9) #probabilidade de recombinação
    unif = rd.uniform(0,1)  #amostração com distribuição uniforme entre 0 e 1

    while t < 75:

        for i in range(N):
            r1_base = X[np.random.randint(N)]
            r2_diff = X[np.random.randint(N)]
            r3_diff = X[np.random.randint(N)]
            F = rd.uniform(0.7, 0.9) #fator de escala
            delta  = rd.randint(0,1)

            #Mutação + Recombinação
            for j in range(n):
                if unif <= C or j == delta:
                    u[i][j] = r1_base[j] + F*(r2_diff[j]-r3_diff[j])
                else:
                    u[i][j] = X[i][j]

            #Seleção de sobrevivência
            if funcao(u[i]) <= funcao(X[i]):
                X[i] = u[i]

        solucao = min(funcao(x) for x in X)
       
        t = t + 1

    solucao = (round(i,4) for i in solucao)

    return solucao

minimo_gl, x1, x2 = main_loop(peaks)
print("Solução para função Peaks: \nMinímo Global: {} Pontos: {} \n".format(minimo_gl,  (x1,x2)))

minimo_gl, x1, x2 = main_loop(rastrigin)
print("Solução para função Rastringin: \nMinímo Global: {} Pontos: {}".format(minimo_gl,  (x1,x2)))