try: # isso é um tente, ele vai tentar executar o que eu pedi
    # , e com seus metodos nao aparece erro de semantica, eu escrevo o erro para simplificar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'Infelizmente deu erro  =( \033[91m{erro}\033[m') # esse mostra qual erro é
    print(f'Problema encontrado --> \033[92m{erro.__class__}\033[m')
    print(f'Problema encontrado --> \033[93m{erro.__cause__}\033[m')
    print(f'Problema encontrado --> \033[94m{erro.args}\033[m')
    print(f'Problema encontrado --> \033[95m{erro.__context__}\033[m')
    print(f'Problema encontrado --> \033[96m{erro.__dict__}\033[m')
    print(f'Problema encontrado --> \033[92m{erro.__doc__}\033[m')
else:
    print(f'A divisao de {a} por {b} é igual a {r}') # aqui so printa se nao tiver nenhum erro,
    # nao causando aquele erro feio de semantica
finally:
    print(f'Volte sempre muito obrigado! =D') # esse msg sempre printa para encerrar o programa,
    # nao é tao necessario