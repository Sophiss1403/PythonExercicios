def fatorial(n: int, show=False): 
    ''''
    ------------------------------
    Help on function fatorial in module __main__:
    
    fatorial(n, show=False)
    -> Calcula o Fatorial de um número.
    -> param. n: número a ser calculado
    -> param. show: (opcional) Mostrar ou não a conta
    -> return: O valor do fatorial de um número n.
    ''' 
    num = n
    f = 1
    if show == False:
        while num > 0:
            f *= num
            num -= 1
        return f
    else:
        print(f'{n}! = ', end = '')
        while num > 0:
            f *= num
            print(f'{num}', end='')
            print(f' x ' if num > 1 else ' = ', end = '')
            num -= 1
        return f
        
print(fatorial(5, True))
print(fatorial(10, True))

