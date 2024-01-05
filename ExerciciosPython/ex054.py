#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
cMaior = 0
cMenor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu?'))
    idade = atual - ano
    if idade >= 18:
        cMaior += 1
    elif idade < 18:
        cMenor += 1

print(f'Ao todo temos {cMaior} pessoas maiores de idade!\n'
      f'E também {cMenor} pessoas menores de idade!')
