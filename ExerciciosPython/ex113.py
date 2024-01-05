def leiaInt(pergunta=''):
    while True:
        try:
            inteiro = int(input(pergunta))
        except:
            print(f'\033[91mErro. Por favor digite um número inteiro válido\033[m')
        else:
            return inteiro


def leiaFloat(pergunta=''):
    while True:
        try:
            real = float(input(pergunta))
        except:
            print(f'\033[91mErro. Por favor digite um número real válido\033[m')
        else:
            return real



# inteiro = leiaInt('Digite um numero inteiro: ')
# real = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi o {leiaInt("Digite um numero inteiro: ")} e o '
      f'real foi {leiaFloat("Digite um numero real: ")}')
