try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'\033[91mTivemos um problema com os tipos de dados que voce digitou!\033[m')
except ZeroDivisionError:
    print(f'\033[91mNão é possivel dividir um numero por zero!\033[m')
except KeyboardInterrupt:
    print(f'\033[91mO usuario preferiu nao informar os dados!\033[m')
else:
    print(f'A divisao de {a} por {b} é igual a {r:.1f}')
finally:
    print(f'Volte sempre muito obrigado! =D')
