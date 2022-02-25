import numpy


# RK4
# intervalo precisa ser uma lista.
# m é a quantidade de iterações a serem feitas, os passos são calculados dentro da função.

def RK4(x0,y0, intervalo, m):

    h = (intervalo[1] - intervalo[0])/m 
    y=y0
    x=x0
    print('0 ', x,'   ',y)

    for i in range(1,m+1):
        
        k1 = edo(x,y) #Inclinação no início do intervalo
        k2 = edo(x + h/2, y + k1 * h/2) #Inclinação no ponto médio do intervalo, usando k1 com o método de euler.
        k3 = edo(x + h/2, y + k2*h/2) #Inclinação no ponto médio do intervalo, usando k2.
        k4 = edo(x + h, y + h*k3) #Inclinação no final do intervalo
        
        #Metodo de RK4
        y = y + (k1 + 2*k2 + 2*k3 + k4) * h/6
        x = x + h
        print (i, round(x,5),round(y,5)) #Imprime os valores de x e y
        
def edo(x,y):
    return x - 2*y + 1


#Solução do PVI da EDO acima:
RK4(0,1,[0,1],10) 