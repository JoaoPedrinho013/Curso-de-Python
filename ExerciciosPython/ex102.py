# Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique
# o número a calcular e outro chamado show, que será
# um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.
#
#
# def fatorial(num=1, show=False):
#     """
#     -> Calculo de um numero fatorial
#     :param num: vem o numero para ser calculado
#     :param show: o calculo se quiser use show=True
#     :return: o numero fatorial do valor num
#     feito por pedro
#     """
#     fato = 1
#     for cont in range(num, 0, -1):
#         fato *= cont
#         if show == True:
#             if cont > 1:
#                 print(f'{cont} ', end='X ')
#             if cont == 1:
#                 print(f'{cont} ', end='= ')
#     return fato
#
#
# num = int(input('Digite um numero para ser calculado o fatorial: '))
# print(fatorial(num, show=False))
# # help(fatorial)




def fatorial(num=1, show=False):
    """
    -> Calculo de um numero fatorial
    :param num: vem o numero para ser calculado
    :param show: o calculo se quiser use show=True
    :return: o numero fatorial do valor num
    feito por pedro
    """
    fato = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' X ', end='')
            if cont == 1:
                print(' = ', end='')
        fato *= cont
    return fato


num = int(input('Digite um numero para ser calculado o fatorial: '))
pergunta = str(input('Você quer ver os numeros do fatorial?').strip().title()[0])
if pergunta == 'S':
    show = True
else:
    show = False
print(fatorial(num, show))
