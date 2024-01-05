# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

cadastro = {
    'Nome': str(input('Nome: ')).title().strip(),
    'Idade': datetime.now().year - int(input('Ano de nascimento: ')),
    # 'Idade': 2023 - int(input('Ano de nascimento: ')),
    'CTPS': int(input('Carteira de trabalho (0 nao tem):')),
    }
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratacao: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = ((cadastro['Contratação'] - 2023) + 35) + cadastro['Idade']

print('-=-' * 25)
for indice, valor in cadastro.items():
    print(f'    -{indice} tem o valor {valor}')
