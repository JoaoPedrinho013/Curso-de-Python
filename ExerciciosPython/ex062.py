#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('GERADOR DE PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} ➢ ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos voce quer mostrar a mais? '))
print(f'Progressao finalizada com {total} termos mostrados!')
