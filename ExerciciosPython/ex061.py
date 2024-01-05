#Refaça o DESAFIO 51, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('GERADOR DE PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
contador = 1
print(f'{termo} ➢ ', end='')
while contador < 10:
    pa = termo + contador * razao # ou da pra usar de vez a variavel isso 'termo += razao' ai no print devez usar pa usa termo
    contador += 1
    print(pa, end=' ➢ ')
print('FIM!')
