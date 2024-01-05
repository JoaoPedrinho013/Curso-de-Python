from ex109 import moeda

valor = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(valor, "US")} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'Aumentando 10% no valor fica {moeda.aumentar(valor,10, True)}')
print(f'Diminuindo 10% no valor fica {moeda.diminuir(valor,10, True)}')
