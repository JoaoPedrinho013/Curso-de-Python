a = [2, 3, 4, 5]
c = a[:] # AQUI È UMA COPIA CORRETA ELA RECEBE TODOS OS ARGUMETOS DO A
b = a  # SE CASO EU TENTAR COPIAR A LISTA A DESSE JEITO E TENTAR MUDAR O VALOR DA B VAI MUDAR O A TBM
b[2] = 8  # PQ AS  DUAS ESTAO INTERLIGADAS
c[1] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
