#Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se  a expressão
# passada está com os parênteses abertos e fechados na ordem correta.

# expressao = (str(input('Digite uma expressão: ')))
# parenteses = expressao.count('(') + expressao.count(')')
# if parenteses % 2 == 0:
#     print('VALIDO')
# else:
#     print('INVALIDO')


#### PROFESSOR #####
expr = (str(input('Digite uma expressão: ')))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('VALIDO')
else:
    print('INVALIDO')
