frase = str(input('Digite uma frase qualquer: ')).upper().strip()
resp = frase.count('A')
resp2 = frase.find('A')+1
resp3 = frase.rfind('A')+1
print('A letra "a" aparece na sua frase {} vezes.\nA primeira vez na posição {}, e a última vez\n'
      'na posição {}. '.format(resp, resp2, resp3))
