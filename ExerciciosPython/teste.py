def menu():
    while True:
        print('-' * 50)
        print('MENU PRINCIPAL'.center(50))
        print('-' * 50)
        print('\033[93m1 - \033[94mVer pessoas cadastradas\033[m')
        print('\033[93m2 - \033[94mCadastrar nova pessoa\033[m')
        print('\033[93m3 - \033[94mSair do sistema\033[m')
        print('-' * 50)
        while True:
            try:
                opcao = int(input('\033[93mSua opção: \033[m'))
            except (ValueError, TypeError):
                print('\033[91mErro: Por favor, digite um numero inteiro valido\033[m')
            except KeyboardInterrupt:
                print('\033[91mO usuario nao quis escrever nada!')
            else:
                if opcao == 1:
                    print('-' * 50)
                    print('OPÇÃO 1'.center(50))
                    print('-' * 50)
                    break
                if opcao == 2:
                    print('-' * 50)
                    print('OPÇÃO 2'.center(50))
                    print('-' * 50)
                    break
                if opcao == 3:
                    print('-' * 50)
                    print('Saindo do sistema... Até logo'.center(50))
                    print('-' * 50)
                    return
                if opcao > 3:
                    print('\033[91mErro: Digite uma opção valida!\033[m')




menu()