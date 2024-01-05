from ex107 import moeda

valor = float(input('Digite um valor: R$'))

print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'Aumentando 10% no valor fica {moeda.aumentar(valor,10)}')
print(f'Diminuindo 10% no valor fica {moeda.diminuir(valor,10)}')
