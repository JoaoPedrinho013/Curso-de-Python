#Exercício Python 060: Faça um programa que leia um número qualquer e
# mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# contador = 0
# somador = 1
# numero = int(input('Digite um numero para eu calcular seu fatorial: '))
# print(f'Calculando {numero}! = {numero}', end='')
# while numero > contador:
#     contador += 1
#     contagem = numero - contador
#     somador *= (contagem+1)
#     if contagem != 0:
#         print(end=f' x {contagem}')
# print(' =', somador)

n = int(input('Digite um numero para eu calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

























# while numero > 1:
#     fatorial = math.factorial(numero)
# print(fatorial)