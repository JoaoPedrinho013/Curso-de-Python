teste = []
teste.append('Pedro')
teste.append(23)
galera = list()
galera.append(teste[:])
teste[0] = 'Caio'
teste[1] = 22
galera.append(teste[:])
print(galera)