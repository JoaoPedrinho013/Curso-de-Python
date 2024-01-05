# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante ‘a função input() do Python, só que fazendo a validação
# para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
# def leiaInt(valor):
#     while True:
#         num = str(input(valor).strip())
#         if num.isnumeric():
#             return num
#         else:
#             print("\033[1;91m" + f'ERRO! Digite um numero inteiro valido!' + "\033[0;0m")
# numero = leiaInt('Digite um numero: ')
# print(f'Voce acabou de digitar o {numero}')


## PROFESSOR

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[1;91mERRO! Digite um numero inteiro valido!\033[0;0m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o {n}')
