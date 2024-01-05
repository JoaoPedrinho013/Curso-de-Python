# print(help()) # esse comando e uma ajuda que mostra a porra toda, da pra ser usado no console tbm

print(print.__doc__)
# print(input.__doc__) # esse doc passa para que serve e todos os parametros que da pra usar
# print(len.__doc__)

# def contador(inicio, fim, passo):
#     """
#     -> Faz uma contatem e mostra na tela.
#     :parametro inicio: inicio da contagem
#     :parametro fim: fim da contagem
#     :parametro passo: passo da contagem
#     :return: sem retorno
#     feito por pedrinho
#     """
#     # isso que eu fiz usando """ """ é uma docstring mostrando a quem for
#     # ve como funciona o def, usando help(nome da funcao)
#     cont = 0
#     while cont <= fim:
#         print(f'{cont}', end='...')
#         cont += passo
#     print('PRONTO')
#
#
# contador(0, 100, 10)
# help(contador)

# def somar(a=0, b=0, c=0): # fazer uma funcao desse jeito os parametros sao opcionais, se nao por nao da erro
#     """
#     -> Faz a soma de 3 valores  e mostra o resultado na tela
#     :parametro a: o primeiro valor
#     :parametro b: o segundo valor
#     :parametro c: o terceiro valor
#     Feito por azien, isso é uma forma de parametro opcional
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
#
# somar(2, 3, 4)
# somar(8, 4)
# somar()
# help(somar)
#
# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}') # VARIAVEL GLOBAL # se eu por a a aqui dentro a de fora nao pega
#     print(f'A dentro vale {a}')  # VARIAVEL LOCAL # mas se eu mudar a variavel transformando ela em global, ele usa a de fora
#     print(f'B dentro vale {b}') # VARIAVEL LOCAL
#     print(f'c dentro vale {c}') # VARIAVEL LOCAL
#
# a = 5
# teste(a)
# print(f'A fora vale {a}') # VARIAVEL GLOBAL
# # print(f'B fora vale {b}') # VARIAVEL LOCAL
# # print(f'c fora vale {c}') # VARIAVEL LOCAL


# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(3, 7, 3)
# r3 = somar(2, 4, 6)
#
# print(f'Os resultados foram {r1}, {r2}, {r3}')
