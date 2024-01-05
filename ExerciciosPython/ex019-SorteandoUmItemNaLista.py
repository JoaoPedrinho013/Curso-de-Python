# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

a1 = str(input('Escreva o nome do primerio aluno:'))
a2 = str(input('Escreva o nome do segundo aluno:'))
a3 = str(input('Escreva o nome do terceiro aluno:'))
a4 = str(input('Escreva o nome do quarto aluno:'))
l = [a1, a2, a3, a4]
r = choice(l)
print(f'O aluno escolhido foi {r}!')
