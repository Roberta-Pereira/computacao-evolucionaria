import random as rd
import numpy as np

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

def main_loop(funcao, intervalo):
    t = 1
    tmax = 30
    
    #Inicialização nuvem de particulas
    X = np.random.uniform(intervalo[0],intervalo[1],size=(50,2))
    Vmax = rd.uniform(0.5, 1.5)
    v = np.random.uniform(-Vmax, Vmax, size=(50,2))              #Vetor de velocidade
    
    p_best = np.array(list(funcao(x) for x in X))                #Melhor posição visitada pela partícula
    g_best_ant,_,_ = min(funcao(x) for x in X)                       #Melhor posição global

    N, n = X.shape

    #Parâmetros para cálculo da velocidade
    w_max = 0.7
    w_min = 0.3
    w = rd.uniform(0.3,0.7)         #Inércia
    C1 = rd.uniform(0.5, 1.5)       #Fator de aprendizagem cognitiva
    C2 = rd.uniform(0.5, 1.5)       #Fator de aprendizagem social

    while True:     
        for i in range(N):
            p_i = funcao(X[i])

            if p_i[0] < p_best[i][0]:
                p_best[i] = p_i
            
            g_best = min(funcao(x) for x in X)
            
            for j in range(n):
                P1 = rd.random()
                P2 = rd.random()
                
                v[i][j] = w*v[i][j] + P1*C1*(p_best[i][j+1]-X[i][j]) + P2*C2*(g_best[j+1]-X[i][j])
               
                if not (-Vmax <= (v[i][0] or v[i][1]) <= Vmax):
                    v[i] = -v[i]
                    X[i] = -X[i]
                    break
            
            X[i] = (X[i] + v[i])        
        
        if (abs(g_best[0] - g_best_ant) <= 10**-6 and t > 1) or t>tmax:
            break
                
        w = w_max - (((w_max - w_min)/tmax) * t)
        g_best_ant = g_best[0]
        t = t + 1
             
    solucao = min(funcao(x) for x in X)
    solucao  = (round(i,4) for i in solucao)
    
    return solucao

minimo_gl, x1, x2 = main_loop(peaks, (-3,3))
print("Solução para função Peaks: \nMinímo Global: {} Pontos: {} \n".format(minimo_gl,  (x1,x2)))

minimo_gl, x1, x2 = main_loop(rastrigin, (-2,2))
print("Solução para função Rastringin: \nMinímo Global: {} Pontos: {}".format(minimo_gl,  (x1,x2)))