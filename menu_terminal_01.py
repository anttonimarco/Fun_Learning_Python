import time # Importação da biblioteca para usar time.

on = True   # Declarando variáveis booleanas.
off = False

while on == True:   # Enquanto variável (on) for verdadeira faça isso.
    print('\033[1:31m       # Menu #\033[m')
    print('\033[1:31m[1]\033[m \033[34mCadastrar Clientes')    #\033[1:31m textocolorido \033[m
    print('\033[1:31m[2]\033[m \033[34mConsultar Clientes')         #Códigos de cores.
    print('\033[1:31m[3]\033[m \033[34mSair\033[m')

    # Se variável choice receber o número 1 faça isso.
    choice = int(input('\033[32mDigite sua escolha: \033[m'))
    if choice == 1:
        print('\n')
        print('\033[1:31m# Cadastro de Clientes #\033[m')
        print('\033[34mDigite o nome do cliente que deseja cadastrar\033[m')
        nome_1 = str(input('\033[32mNome do Cliente: \033[m'))
        data_nasc = int(input('Data de Nascimento: '))
        print('\n\033[1:31mCliente Cadastrado com Sucesso!\033[m')
        print('\033[34mRetornando ao Menu Principal em\033[m \033[32m3\033[m')
        time.sleep(1)
        print('\033[34mRetornando ao Menu Principal em\033[m \033[33m2\033[m')
        time.sleep(1)
        print('\033[34mRetornando ao Menu Principal em\033[m \033[31m1\033[m\n')
        time.sleep(1)

    # Se variável choice receber o número 2 faça isso.
    elif choice == 2:
        print('\n')
        print('\033[1:31m# Consulta de Clientes #\033[m')
        finder = str(input('\033[32mDigite o nome para buscar: \033[m\n'))
        if finder == nome_1:
            print('\033[1:32m#Nome do Cliente Encontrado #\033[m')
            print('Nome: {}'.format(nome_1))
        else:
            print('Nome não encontrado!')
        print('\n Retornando ao Menu Principal\n')
        time.sleep(2)

    # Se variável choice receber o número 3 faça isso.
    elif choice == 3:
        var = on == False
        print('\033[34mSaindo do programa em\033[m \033[32m3\033[m')
        time.sleep(1)
        print('\033[34mSaindo do programa em\033[m \033[33m2\033[m')
        time.sleep(1)
        print('\033[34mSaindo do programa em\033[m \033[31m1\033[m')
        time.sleep(1)
        break

