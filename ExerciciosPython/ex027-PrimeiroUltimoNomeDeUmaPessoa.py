#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo:')).strip().split()
print(f"""É um prazer te conhecer!
Seu primeriro nome é {n[0]}.
Seu ultimo nome é {n[len(n)-1]}.""")
