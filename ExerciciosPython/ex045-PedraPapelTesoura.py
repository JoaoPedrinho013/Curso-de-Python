#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
print(10*'='+ 'JOKENPÔ' + 10*'=')
print('''Sua opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')

#escolha do jogador
jogada = int(input("Qual é sua jogada?"))

if jogada == 0:
    jog = 'pedra'
elif jogada == 1:
    jog = 'papel'
elif jogada == 2:
    jog = 'tesoura'
else:
    print('Tu é burro cara é de 0 a 2!!!')
#sorteio do pc
sorteio = randint(0, 2)
if sorteio == 0:
    sor = 'pedra'
elif sorteio == 1:
    sor = 'papel'
elif sorteio == 2:
    sor = 'tesoura'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print(20*'=')
print(f'jogador jogou {jog.upper()}')
print(f'Pc jogou {sor.upper()}')
print(20*'=')

if jogada == sorteio:
    print('EMPATE')
elif jogada == 0 and sorteio == 1:
    print('PC VENCE')
elif jogada == 0 and sorteio == 2:
    print('JOGADOR VENCE')
elif jogada == 1 and sorteio == 0:
    print('JOGADOR VENCE')
elif jogada == 1 and sorteio == 2:
    print('PC VENCE')
elif jogada == 2 and sorteio == 0:
    print('PC VENCE')
elif jogada == 2 and sorteio == 1:
    print('JOGADOR VENCE')
else:
    print('Opção inválida. Escolha um número entre 0 e 2.')