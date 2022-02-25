import numpy as np

def pontofixo(ponto, funcao, max):
    if funcao(ponto) == 0:
        print('O ponto ', ponto, ' é a raiz da função!')
    
    else: 
        p = funcao(ponto)
        for i in range(max+1):
            p = funcao(p)
        
        print('Raiz encontrada com ',i,' iterações foi: ', p)
        return p

#Definindo a f(x)

def f(x):
    return x**3 + 4 * (x**2) - 10 

# Algumas maneiras de manipular a f(x) para utilizar o método de ponto fixo:

def f1(x):
    return x - (x**3) - 4*(x**2) + 10

def f2(x):
    return np.sqrt((10/x) - 4*x)

def f3(x):
    return 0.5 * np.sqrt(10 - (x**3))

# Chamando a função pontofixo com um erro de 0.05
# Com p0 = 1.5 e um maximo de 10 iterações
# Utilizando a função f1 encontramos uma função divergente
# Utilizando a função f2 encontramos uma raiz quadrada de um ponto negativo
# Por fim, a função f3 é a que única que consegue encontrar a raiz para a f(x)


print(pontofixo(2,f3,10))
