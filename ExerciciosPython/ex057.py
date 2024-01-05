# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

# sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
# while sexo != 'M' and sexo != 'F':
#     sexo = str(input('Dados invalidos. Fale seu sexo [M/F]: ')).upper().strip()[0]
# print(f'Seu sexo {sexo} foi confirmado com sucesso')


sexo1 = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo1 not in 'MmFf': 
    sexo1 = str(input('Dados invalidos. Fale seu sexo [M/F]: ')).upper().strip()[0]
print(f'Seu sexo {sexo1} foi confirmado com sucesso')