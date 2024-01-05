#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras tem sem considerar os espaços.
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo:'))
sem = nome.split()
com = ''.join(sem)
print(f"""Analizando seu nome...
Seu nome em letras maiusculas é {nome.upper()}.
Seu nome em letras minusculas é {nome.lower()}.
Seu nome tem {len(com)} letras!
seu nome tem {(len(nome))-nome.count(' ')} letras!
Seu primeiro nome é {sem[0]} tem {len(sem[0])} letras!""")
