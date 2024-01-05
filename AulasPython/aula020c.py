def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2, 3, 4, 5, 6, 2, 1, 2]
print(valores)
dobra(valores)
print(valores)
