pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 23, 'voto': 69}

print(pessoas)
print('=-' * 20)
print(pessoas['nome'], ['sexo'], ['idade'])  # ASSIM N FUNCIONA
print('=-' * 20)
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['sexo'])
print(pessoas['voto'])
print('=-' * 20)
######################################################
del pessoas['voto']  # AQUI DELETA UM INDICE OU CHAVE
pessoas['idade'] = 25  # DESSE JEITO EU TROCO QUALQUER VALOR DO DICIONARIO
pessoas['peso'] = 98.8  # AQUI ADCIONA UM INDICE NA [] E O VALOR DEPOIS DO = SE FOR NUMERO NAO PRECISA DE ""
######################################################
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade!')
print('=-' * 20)
print(pessoas.keys())  # puxa os indices, tipo a chave para eu acessar alguma informacao
print('=-' * 20)
print(pessoas.values())  # aqui puxa os valores que tem dentro das chaves por ex o nome da pessoa
print('=-' * 20)
print(pessoas.items())  # aqui ele puxa tanto o indice quanto o nome juntos em ()
print('=-' * 20)
