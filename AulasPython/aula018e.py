galera = []
dado = []
totmai = totmen = 0

for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print('=-' * 25)
for pessoas in galera:
    print(f'{pessoas[0].title().strip()} tem {pessoas[1]} anos de idade!', end=' ')


    if pessoas[1] >= 18:
        print(f'{pessoas[0].title().strip()}, é maior de idade')
        print('=-' * 25)
        totmai += 1
    else:
        print(f'{pessoas[0].title().strip()}, é menor de idade')
        print('=-' * 25)
        totmen += 1

print(f'Temos {totmai} pessoas maiores de idade e {totmen} menores!')
print('=-' * 25)

print(galera)
