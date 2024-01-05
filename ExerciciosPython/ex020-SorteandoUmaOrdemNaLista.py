#O professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Escreva o nome do primerio aluno:'))
a2 = str(input('Escreva o nome do segundo aluno:'))
a3 = str(input('Escreva o nome do terceiro aluno:'))
a4 = str(input('Escreva o nome do quarto aluno:'))
l = [a1, a2, a3, a4]
shuffle(l)
print(f'A ordem dos alunos para apresentar é:{l}')
