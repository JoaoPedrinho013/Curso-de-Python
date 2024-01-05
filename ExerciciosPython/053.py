# pergunta = str(input('Digite uma frase: ')).strip().upper().replace(" ", "")
# invertida = pergunta[::-1]
# print(f'O inverso de {pergunta}, é {invertida}')
# if pergunta != invertida:
#     print('A frase digitada não é um PALÍNDROMO!')
# else:
#     print('A frase digitada é um PALÍNDROMO!')

##################################PROFESSOR
pergunta2 = str(input('Digite uma frase: ')).strip().upper().split()
junto = "".join(pergunta2)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um PALÍNDROMO!')
