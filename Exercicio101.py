from datetime import date
import time
nasc = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
age = ano_atual - nasc

def voto(age: int):
    '''Voto opcional - entre 16 e 17 anos
    dps a partir dos 65 é opcional
    entre 18 e 64 anos é obrigatório
    menos de 16 é negado '''
        
    if age >= 16 or age >= 65:
        if  age >= 18 and age <= 64:
            print(f'Com {age} anos o voto é obrigatório')
            return 'Obrigatório'
        else:
            print(f'Com {age} anos o voto é opcional')
            return 'Opcional'
    else:
        print(f'Com {age} ano(s) o voto é negado')
        return 'Negado'
    

if __name__ == '__main__':
    print('Exemplo: ')
    voto(age)
    print('Rodando testes...')
    time.sleep(0.5)
    assert voto(64) == 'Obrigatório'
    time.sleep(0.5)
    assert voto(18) == 'Obrigatório'
    time.sleep(0.5)
    assert voto(65) == 'Opcional'
    time.sleep(0.5)
    assert voto(16) == 'Opcional'
    time.sleep(0.5)
    assert voto(17) == 'Opcional'
    time.sleep(0.5)
    assert voto(200) == 'Opcional'
