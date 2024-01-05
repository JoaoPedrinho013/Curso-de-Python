# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi
# o maior e o menor valores lidos. O programa deve perguntar ao usuário se
# ele quer ou não continuar a digitar valores.

resposta = 'S'

somador = media = contador = maior = menor = 0

while resposta == 'S':
    numero = int(input('Digite um numero: '))
    contador += 1
    somador += numero
    media = somador / contador
    if contador == 1:
        maior = menor = numero
    else:
        if maior < numero:
            maior = numero
        elif maior > numero:
            menor = numero

    resposta = str(input('Quer continuar? S ou N')).upper()
print(f'Voce digitou {contador} numeros e a media foi de {media:.2f}\n'
      f'O maior valor foi o {maior} e o menor {menor}')
