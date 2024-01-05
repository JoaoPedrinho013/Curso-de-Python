# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

# def notas(*n, sit=False):
#     """
#     -> Funcao para analisar notas e situacoes de varios alunos.
#     :param n: uma ou mais notas dos alunos - aceita varias
#     :param sit: valor opcional, indicando se deve ou nao adcionar a situacao
#     :return:   dicionario com  varias informacoes da turma.
#     feito por azien
#     """
#     print('-=' * len(n) * 11)
#     dados = {'total': len(n), 'maior': 0, 'menor': 0, 'media': '0'}
#
#     somador = 0
#     for chave, valor in enumerate(n):
#         somador += valor
#         if chave == 0:
#             maior = 0
#             menor = valor
#         if valor > maior:
#             maior = valor
#         if valor < menor:
#             menor = valor
#
#
#
#     media = somador / len(n)
#     dados['media'] = media
#     dados['maior'] = maior
#     dados['menor'] = menor
#     if sit:
#         if media > 7:
#             dados['situacao'] = 'BOA'
#         if media >= 5 and media <= 7:
#             dados['situacao'] = 'RAZOAVEL'
#         if media < 5:
#             dados['situacao'] = 'RUIM'
#
#     return dados
#
#
# ### PRINCIPAL
# resp = notas(5.5, 9.5, 10, 3.4, sit=True)
# print(resp)
# help(notas)


#### PROFESSOR
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 9.5, 10, 3.4, sit=True)
print(resp)
