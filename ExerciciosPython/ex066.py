n = s = c = 0
while True:
    n = int(input('Digite um valor (666 para parar): '))
    if n == 666:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores foi {s}')
