pessoas = list()
informacoes = []
maior = menor = 0

while True:
    informacoes.append(str(input('Nome: ')).title())
    informacoes.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = informacoes[1]
    else:
        if informacoes[1] > maior:
            maior = informacoes[1]
        if informacoes[1] < menor:
            menor = informacoes[1]
    pessoas.append(informacoes[:])
    informacoes.clear()
    continuar = str(input('Quer continuar?')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}kg. Peso de ', end="")
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end="")
print()
print(f'O menor peso foi {menor}kg. Peso de ', end="")
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end="")
