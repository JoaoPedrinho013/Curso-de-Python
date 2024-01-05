#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
n = str(input('Em qual cidade você nasceu?')).strip()
print(n[:5].upper() == 'SANTO')
