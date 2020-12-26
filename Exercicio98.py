from time import sleep
def separador():
    print('-=' * 30)

def contador(inicio, fim, passo=1):
    print(f'Contagem de {inicio} a {fim}, de {passo + 1 if passo == 0 else abs(passo)} em {passo + 1 if passo == 0 else abs(passo)}: ')
    sleep(1.5)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo *= -1
        fim -= 1
    else:
        fim += 1
    for num in range(inicio, fim, passo):
         
        print(num, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    
# Programa principal
separador()  
contador(1,10)
separador()
contador(10,0,2)
separador()
print('Agora é sua vez de personalizar a contagem!')

começo = int(input('Início: '))
final = int(input('Fim: '))
espaço = int(input('Passo: '))
separador()

contador(começo, final, espaço)
