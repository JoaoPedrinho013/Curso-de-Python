# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores[:]:
        valores.append(valor)
        print(f'Valor de {valor} adcionado com sucesso!')
    else:
        print(f'Esse valor de {valor} ja esta na lista e nao foi adcionado!')
    pergunta = str(input('Quer continuar? ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('É sim ou não porra! ')).strip().upper()[0]
    if pergunta == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores} em ordem crescente!')
valores.sort(reverse=True)
print(f'E esses sao os valores em ordem decrescente {valores} !')
