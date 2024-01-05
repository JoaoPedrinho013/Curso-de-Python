#função do py
#input significa Escreva ex: ex = input('digite algo')
#print significa Leia ex:print('Algo',ex)

#Tipos primitivos
#int significa Numero Inteiro ex:6,-6
#float significa Numero Real ou Numero de Ponto Flutuante ex:4.20,-4,20
#bool signifaca Valor Logico ou Booliano ex:True(verdadeiro),False(falso)
#str significa Valor caracteris ou str ex:'Olá','7.5',''
#Uma nova forma de fazer print Antiga:print('soma vale',s) Nova:print(f'soma vale{s}')


#tipe é para descobrir o tipo primitvo se não for definido antes sempre sera str

#is é para verificar as informaçoes que forem escrita
#is ex:.isspace() para identificar espaço
#is ex:.isnumeric() para identificar numero
#is ex:.isalpha() para identificar letra do alfabeto
#is ex:.isalnum() para identificar se é alfanumerico
#is ex:.isupper() para identificar se é maiúsculo
#is ex:.islower() para identificar se é minúscula
#is ex:.istitle() para identificar se é capitalizada

#Operadores Aritimeticos

#Adição:+ ex:5+2==7
#Subtração:- ex:5-2==3
#Multiplicação:* ex:5*2==10
#Divisão:/ ex:5/2==2.5
#Divisão Inteira:// ex:5//2==2
#Resto da Divisão:% ex:5%2==5
#Potência:** ex:5**2==25
#Ordem de precedência
#1 ()
#2 **
#3 * / // %
#4 + -

#Como quebrar linha no print sem ter q escrever denovo usando apenas o \n ex:print(f'Algo aqui{} /n Algo aqui{}')
#Como escolher quantos numeros vão aparecer depois do ponto flutuante :.f ex:print('Um valor {:.2f}')
n = 30  # Número de elementos da sequência de Fibonacci que queremos calcular

f = [0, 1]  # Inicializamos a sequência com os dois primeiros números

while len(f) < n:
    n1= f[-1] + f[-2]  # Calcula o próximo número somando os dois últimos
    f.append(n1)  # Adiciona o próximo número à sequência

print(f)