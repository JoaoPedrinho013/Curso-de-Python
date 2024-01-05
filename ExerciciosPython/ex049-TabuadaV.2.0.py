#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
from time import sleep
n = int(input('Digite um numero:'))
for c in range(1, 11):
    t = n * c
    print(f'{n} X {c:2} = {t}')
    sleep(0.5)
print('='*20)
for c in range(1, 10+1):
    print(f'{n} X {c:2} = {n * c}')
    sleep(0.5)
