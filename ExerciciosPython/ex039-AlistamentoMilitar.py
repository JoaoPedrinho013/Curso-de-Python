#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
#do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento:'))
sexo = input('Qual seu sexo?').lower().strip()
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if sexo == 'masculino':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda falta {saldo} anos para se alistar.')
        print(f'Seu alistamento será em {atual + saldo}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {atual-saldo}.')
elif sexo == 'feminino':
    print('Você não precisa se alistar!')
else:
    print('Tu é burro é pra escolhe entre masculino e feminino!!!')
