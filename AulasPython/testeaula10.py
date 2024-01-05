#condição simples
n = str(input('Qual seu nome?'))
if n == 'Caio':
    print('Que legal é o meu nome!')
print(f'Olá, {n}!')
#condição composta
n = str(input('Qual seu nome?'))
if n == 'Caio':
    print('Que nome lindo!')
else:
    print('Que nome tão comum!')
print(f'Olá, {n}!')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print(f'A Sua media foi {m:.1f}')
if m >= 6.0:
    print('Você tirou uma nota boa! PARABÉNS!')
else:
    print('Você tirou uma nota ruim! ESTUDE MAIS!')
