# funciona em python 3.5 e 3.6

# tempo()
# início do programa: 
# > T = tempo()
# fim do programa: printa na tela a diferenca de tempo
# > tempo(T) 

import time

def tempo(t=0, verbose=True):
    if t == 0:
        if verbose:
            print('LOG: inicio do cronometro')
        return time.time()
    else:
        x = time.time() - t
        if verbose:
            print('LOG: tempo decorrido', x)
        return x


# funcao multiprocessor(): retorna um map 

import multiprocessing as mp

def multiprocessor(funcao, iteravel):
    print('iniciando threads...')
    pool = mp.Pool()
    saida = pool.map(funcao, iteravel)
    pool.close()
    pool.join()
    return saida
    

# Usar multiprocessor definindo a funcao a ser usada fora do __main__, 
# e chamando o multiprocessor no __main__

def funcao(x):    
    return x*x

if __name__ == "__main__":
    saidamap = multiprocessor(funcao, list(range(1000)))
    
    
    
# Caso sua funcao a ser multiprocessada receba argumentos não-iteraveis, use o partial:
    
from functools import partial

def funcao2(x, fixo):    
    return x*x*fixo

if __name__ == "__main__":
    novafuncao = partial(funcao2, fixo=100)
    saidamap = multiprocessor(novafuncao, list(range(1000)))
