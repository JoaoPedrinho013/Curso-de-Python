from ex108 import moeda

valor = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'Aumentando 10% no valor fica {moeda.moeda(moeda.aumentar(valor,10))}')
print(f'Diminuindo 10% no valor fica {moeda.moeda(moeda.diminuir(valor,10))}')
