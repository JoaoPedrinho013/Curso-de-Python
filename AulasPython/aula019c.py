brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Bahia', 'sigla': 'BA'}
estado3 = {'uf': 'Espirito Santo', 'sigla': 'ES'}
estado4 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
estado5 = {'uf': 'Tocantins', 'sigla': 'TO'}
estado6 = {'uf': 'Maranhão', 'sigla': 'MA'}
estado7 = {'uf': 'Acre', 'sigla': 'AC'}
estado8 = {'uf': 'Amazonas', 'sigla': 'AM'}
estado9 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado10 = {'uf': 'Pernambuco', 'sigla': 'PE'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
brasil.append(estado4)
brasil.append(estado5)
brasil.append(estado6)
brasil.append(estado7)
brasil.append(estado8)
brasil.append(estado9)
brasil.append(estado10)
print(brasil[0])
print(brasil[4]['uf'])
print(brasil[4]['sigla'])
for chave, valor in brasil:
    print(chave, valor)

