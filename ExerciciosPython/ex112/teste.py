from ex112.ultilidadesCeV import moeda
from ex112.ultilidadesCeV import dados


valor = dados.leiaDinheiro('Digite o preço: R$')

moeda.resumo(valor, 20, 12)
