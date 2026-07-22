from time import sleep

lista_usuarios = []


def menu_principal():
    while True:
        print('=== MENU PRINCIPAL ===')
        print('1 - Login ')
        print('2 - Cadastro')
        print('3 - Sair')

        opcao = input('Escolha a opção: ')

        if opcao == '1':
            fluxo_login()
        elif opcao == '2':
            fluxo_cadastro()
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')


def fluxo_cadastro():
    nome = input('Nome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    confirmar_senha = input('Confirmar senha: ')

    if senha != confirmar_senha:
        print('Senhas não conferem!')
        sleep(1)
        return

    for usuario in lista_usuarios:
        if usuario['email'] == email:
            print('Email já cadastrado')
            return

    novo_usuario = {'nome': nome, 'email': email, 'senha': senha}
    lista_usuarios.append(novo_usuario)

    print('Cadastro realizado com sucesso!')


def fluxo_login():
    email_digitado = input('Email: ')
    senha_digitada = input('Senha: ')

    for usuario in lista_usuarios:
        if usuario['email'] == email_digitado and usuario['senha'] == senha_digitada:
            print(f"Bem-vindo, {usuario['nome']}!")
            area_logada(usuario)
            return

    print('Email ou senha inválidos')


def area_logada(usuario):
    while True:
        print(''' 1 - Ver dados
                  2 - Logout ''')

        opcao = input('Opção: ')

        if opcao == '1':
            print(f"Nome: {usuario['nome']}")
            print(f"Email: {usuario['email']}")
            print(f"Senha: {usuario['senha']}")
        elif opcao == '2':
            print('Logout realizado')
            return
        else:
            print('Opção inválida!')


menu_principal()
