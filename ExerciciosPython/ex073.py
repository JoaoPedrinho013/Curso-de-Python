# Exercício Python 73: Crie uma tupla preenchida com os 20
# primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


escala = ('Santos', 'Gremio', 'Flamengo', 'Palmeiras', 'Atletico PR', 'Sao paulo', 'Botafogo', 'cuiaba',
          'Fluminense', 'Bragantino', 'Fortaleza', 'Internacional', 'Cruzeiro', 'Chapecoense', 'Atletico mg',
          'Goias', 'Bahia', 'Coritiba', 'america mg', 'vasco da gama')
print('=-' * 30)
print(f'Lista do brasileirão 2023: {escala}')
print('=-' * 30)
print(f'Os cinco primeiros colocados são: {escala[:5]}')
print('=-' * 30)
print(f'Os quatro últimos são: {escala[16:]}')
print('=-' * 30)
print(f'Times em ordem alfabetica: {sorted(escala)}')
print('=-' * 30)
print(f'O chapecoense está na posição {escala.index("Chapecoense") + 1}°')
print('=-' * 30)

