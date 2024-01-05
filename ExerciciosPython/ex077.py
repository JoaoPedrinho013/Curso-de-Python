listaPalavras = ('ola', 'maconha',
            'drogra', 'sexo',
            'minecraft', 'rock',
            'satanismo', 'viado',
            'caioGay', 'miaPika',
            'miaKhalifa', 'punheta',
            'vinicius13Porra')

for palavra in listaPalavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



