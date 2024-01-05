#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
s2 = 0
c1 = 0
c2 = 0
for c in range(1,7):
    n = int(input(f'Digite o {c} número inteiro:'))
    if n % 2 == 0:
        s += n
        c1 += 1
    elif n % 2 == 1:
        s2 += n
        c2 += 1
print(f'A soma de todos os {c1} números pares é {s}!')
print(f'A soma de todos os {c2} números impar é {s2}!')
