from Ex115.Lib.interface import *


def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('\033[91mHouve um ERRO  na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('\033[91mERRO ao ler o arquivo\033[m')
    else:
        cabecalho('Pessoas cadastradas')
        # print(arq.read().replace(";", '\t' * 5).replace('\n', ' anos\n'))
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[96m{dado[0]:<30}\033[36m{dado[1]:>3} anos\033[m')
    finally:
        arq.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'\033[91mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[91mHouve um ERRO na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adcionado.')
            a.close()
