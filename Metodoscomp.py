import numpy as np


def f(x):
    return 0.05*(x**3) - 0.4*(x**2) + 3*np.sin(x)*x

def g(x):
    return 0.5 * np.sqrt(10 - (x**3))

def edo(x,y):
    return x - 2*y + 1

class MetodosComputacionais:

    def __init__(self,funcao):
        self.funcao = funcao

    def Bissecao(self, a, b, erro, max):

        if (self.funcao(a)==0):
            k = a
            print('A raiz é o próprio ponto A: ', a)    # Retorna o ponto A caso seja a raiz

        elif (self.funcao(b)==0):
            k = b
            print('A raiz é o próprio ponto B: ', b)    # Retorna o ponto B caso seja a raiz

        elif (self.funcao(a)*self.funcao(b) < 0):    
            t = 1
            while (np.absolute(self.funcao(b)-self.funcao(a))/2 > erro): # Laço com sistema de erro
                k = (a+b)/2
                if self.funcao(k) == 0:
                    print('A raiz é: ', k)
                    break
                else:
                    if (self.funcao(a) * self.funcao(k) < 0):
                        b = k
                    else:
                        a = k
                t = t+1
                if t >= max:    # Sistema de parada caso exceda o número de iterações estipulada
                    break
            print('numero de iterações foi: ', t) 
            print('valor da raiz é: ', k)
            print('Prova: f(',k,'): ', f(k))

            return k

        else:
            print('nao há raiz no intervalo')

    def PontoFixo(self, ponto, max):
        if self.funcao(ponto) == 0:
            print('O ponto ', ponto, ' é a raiz da função!')
    
        else: 
            p = self.funcao(ponto)
            for i in range(max+1):
                p = self.funcao(p)
        
            print('Raiz encontrada com ',i,' iterações foi: ', p)
            return p

    def RungeKutta(self, x0, y0, intervalo, m):
        h = (intervalo[1] - intervalo[0])/m 
        y=y0
        x=x0
        print('0 ', x,'   ',y)

        for i in range(1,m+1):
        
            k1 = self.funcao(x,y) #Inclinação no início do intervalo
            k2 = self.funcao(x + h/2, y + k1 * h/2) #Inclinação no ponto médio do intervalo, usando k1 com o método de euler.
            k3 = self.funcao(x + h/2, y + k2*h/2) #Inclinação no ponto médio do intervalo, usando k2.
            k4 = self.funcao(x + h, y + h*k3) #Inclinação no final do intervalo
        
            #Metodo de RK4
            y = y + (k1 + 2*k2 + 2*k3 + k4) * h/6
            x = x + h
            print (i, round(x,5),round(y,5)) #Imprime os valores de x e y

funcao1 = MetodosComputacionais(f)
funcao2 = MetodosComputacionais(g)
funcao3 = MetodosComputacionais(edo)

print('Bisseção: \n')
funcao1.Bissecao(10, 12, 0.005, 16)
print('Ponto fixo: \n')
funcao2.PontoFixo(1.5, 10)
print('Runge Kutta: ')
funcao3.RungeKutta(0, 1, [0,1], 10)