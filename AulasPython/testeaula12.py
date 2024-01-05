nome = str(input("Diga seu nome?")).lower()
if nome == 'caio':
    print("Que nome lindo Cara")
elif nome == 'pedro'or nome == 'carlos' or nome == 'richard':
    print("Tu é né!")
elif nome in 'maria carla juana':
    print("Tu é femea né!")
else:
    print("Um grande foda-se")
print(f"Olá Puta {nome.title()}!")
