import numpy as np

def bissecao(a, b, funcao, erro, max):

    if (funcao(a) == 0):
        k = a
        # Retorna o ponto A caso seja a raiz
        print('A raiz é o próprio ponto A: ', a)

    elif (funcao(b) == 0):
        k = b
        # Retorna o ponto B caso seja a raiz
        print('A raiz é o próprio ponto B: ', b)

    elif (funcao(a)*funcao(b) < 0):
        t = 1
        while (np.absolute(funcao(b)-funcao(a))/2 > erro):  # Laço com sistema de erro
            k = (a+b)/2
            if funcao(k) == 0:
                print('A raiz é: ', k)
                break
            else:
                if (funcao(a) * funcao(k) < 0):
                    b = k
                else:
                    a = k
            t = t+1
            if t >= max:    # Sistema de parada caso exceda o número de iterações estipulada
                break

        print('numero de iterações foi: ', t)
        print('valor da raiz é: ', k)
        print('f(', k, '): ', f(k))

    else:
        print('nao há raiz no intervalo')

    return k  # Retorna a raiz para ser utilizada como objeto

# Exemplos:


def f(x):
    return 0.05*(x**3) - 0.4*(x**2) + 3*np.sin(x)*x


bissecao(10, 12, f, 0.005, 16)
