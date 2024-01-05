pessoinhas = dict()
pessoinhas['nome'] = 'Pedro'
pessoinhas['idade'] = '23'
pessoinhas['sexo'] = 'Masculino'
print(pessoinhas)
print('=-' * 20)
for chave in pessoinhas.keys():
    print(f'{chave.title()}:')  # ESSE FOR MOSTRA OS INDICES AS CHAVES
print('=-' * 20)
for valores in pessoinhas.values():
    print(valores)          # ESSE FOR MOSTRA OS VALORES
print('=-' * 20)
for chave, valores in pessoinhas.items():
    print(f'{chave}: {valores} ')    # ESSE FOR MOSTRA OS DOIS ORGANIZADO
print('=-' * 20)
