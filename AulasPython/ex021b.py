# def fatorial(num=1):
#     f = 1
#     for cont in range(num, 0, -1):
#         f *= cont
#     return f
#
#
# # numero = int(input('Digite um numero: '))
# # print(f'O fatorial de {numero} é igual a {fatorial(numero)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os valores sao {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
print(par(num))
if par(num):
    print('É par')
else:
    print('Não é par')