#  Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
# pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: Não Vota'
    if idade >= 16 and idade < 18 or idade > 70:
        return f'Com {idade} anos: Voto Opcional'
    if idade >= 18 and idade <= 70:
        return f'Com {idade} anos: Voto Obrigatorio'


print(voto(int(input('Em que ano voce nasceu? '))))

