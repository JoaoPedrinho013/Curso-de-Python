#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

p = int(input('Primeiro valor:'))
s = int(input('Segundo valor:'))
t = int(input('Terceiro valor:'))

#Como fiz
'''if p < s and p < t:
    print(f'O menor valor é {p}.')
if s < p and s < t:
    print(f'O menor valor é {s}.')
if t < p and t < s:
    print(f'O menor valor é {t}.')
if p > s and p > t:
    print(f'O maior valor é {p}.')
if s > p and s > t:
    print(f'O maior valor é {s}.')
if t > p and t > s:
    print(f'O maior valor é {t}.')'''

#Verificando qual o menor
menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
#verificando qual o maior
maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t

# menor = min(p, s, t)
# maior = max(p, s, t)

print(f'''O menor valor é {menor}.
O maior valor é {maior}.''')
