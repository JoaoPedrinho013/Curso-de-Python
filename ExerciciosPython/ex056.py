# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idadeTotal = 0
mulheres = 0
maiorIdade = 0
for pessoas in range(1, 5):
    print(10 * '-', f'{pessoas}ª PESSOA', 10 * '-')
    nome = str(input('Qual seu nome:')).title().strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo (F/M)? ')).upper().strip()
    #MEDIA DE IDADE DE TODOS
    idadeTotal += idade
    mediaIdade = idadeTotal / 4
    #MENINAS ABAIXO DE 20
    if sexo == 'F' and idade < 20:
        mulheres += 1
    #NOME DO HOMEM MAIS VELHO
    if sexo == 'M' and idade > maiorIdade:
        idadeM = idade
        nomeM = nome
        maiorIdade = idadeM

print(f'A media da idade do grupo é de {mediaIdade} anos!')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {nomeM}')
print(f'Ao todo sao {mulheres} mulheres  com menos de 20 anos')
