num = (8, 2, 4, 5)
num2 = [8, 2, 4, 5, 8]
num3 = [8, 2, 4, 5]
#num[2] = 3
num2[2] = 3 # troca o num da lista

num2.append(7) # add final da lista

num2.sort() #cola em ordem

num3.sort(reverse=True) #Ordem Decrescente, ao contrario

num3.insert(2, 'ola') # insert serve para colocar algo na lista pode ser qualquer coisa
num3.insert(3, 0) # o  numero so pra provar

num2.pop() # REMOVE O ULTIMO DA LISTA

num3.pop(3) # REMOVE O QUARTO  DA LISTA

num2.remove(8) # ESSE REMOVER SE TIVER 2 NUMEROS OU ITENS IGUAIS ELE VAI REMOVER O PRIMEIRO QUE VER

# num2.remove(69) SE O NUMERO N TIVER NA LISTA ELE DA ERRO TEM QUE USAR IF

if 69 in num2:
    num2.remove(69)   # ASSIM JA FUNCIONA PQ ELE VAI PROCURAR SE TEM E SE TIVER ELE TIRA
else:
    print('O numero 69 nao ta na lista')

print(f'Essa lista tem {len(num3)} elementos') # LEN pra ver quantas coisas tem na lista comecando por 0

print(num)
print(num2)
print(num3)
