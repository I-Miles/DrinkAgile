import mysql.connector
import connectdrink
from cadastro import cadastrar_func, cadastrar_cliente,cadastrar_produto,cadastrar_fornecedor
from pesquisa import consultarfunc,consultarforn,consultarprod,consultarcli
from delete import deletarcli,deletarforn,deletarfunc,deletarprod
from update import alterar_produto,alterar_clientes,alterar_funcionario,alterar_fornecedores

while True:
    print(25 * "-")
    print("bem-vindo ao drink.Agille")
    print(25 * "-")
    print("1. Menu funcionario")
    print("2. Menu cliente")
    print("3. Sair ")

    escolha = input("Qual menu deseja acessar: ")
    if escolha == "1":
        print("digite o login e senha para entrar como funcionario.")
        login = input("Login: ")
        senha = input("Senha: ")
        if login == "ADMDRINK" and senha == "drink123":
            print(25 * "-")
            print("bem vindo ao menu do funcionario")
            print("     O que deseja acessar ")
            print(25 * "-")
            print("1. Cadastro funcionario")
            print("2. Cadastro produto")
            print("3. Cadastro fornecedor")
            print("4. consultar")
            print("5. alterar dados")
            print("6. sair")

            escolhafunc = input("qual função deseja acessar: ")
            if escolhafunc == "1":
                p_nome = input("Digite o nome do funcionario: ")
                p_cargo = input("Digite o cargo do funcionario: ")
                p_salario = input("Digite o salario do funcionario: ")
                cadastrar_func(p_nome,p_cargo,p_salario)
            elif escolhafunc == "2":
                nome = input("Digite o nome do produto: ")
                valor = int(input("Digite o valor do produto: "))
                estoque = int(input("Digite a quantidade do produto: "))
                cadastrar_produto(nome, valor, estoque)
            elif escolhafunc == "3":
                nome = input("Digite o nome do fornecedor: ")
                email = input("Digite o email do fornecedor: ")
                telefone = input("Digite o telefone do fornecedor: ")
                produto = int(input("digite o id do produto: "))
                cadastrar_fornecedor(nome, email, telefone, produto)
            elif escolhafunc == "4":
                print("consultas")
                print("1. consultar funcionarios")
                print("2. consultar clientes")
                print("3. consultar fornecedores")
                print("4. consultar produtos")
                print("5. sair")
                escolha_consulta = input("Digite qual consulta deseja ver")
                if escolha_consulta == "1":
                    consultarfunc()
                elif escolha_consulta =="2":
                    consultarcli()
                elif escolha_consulta =="3":
                    consultarforn()
                elif escolha_consulta == "4":
                    consultarprod()
                elif escolha_consulta =="5":
                    print("saindo......")
                    pass
                else:
                    print("digite um valor coerente ao das opções")
            elif escolhafunc =="5":
                print("Alterar dados")
                print("1. update dados funcionarios")
                print("2. deletar funcionario")
                print("3. update dados cliente")
                print("4. deletar cliente")
                print("5. update dados fornecedor")
                print("6. deletar fornecedor")
                print("7. update dados produto")
                print("8. deletar produto")
                print("9. sair")
                escolha_consulta = input("Digite qual tabela deseja alterar")
                if escolha_consulta == "1":
                    id_funcionario = int(input("Digite o ID do funcionário que você deseja alterar: "))
                    novo_nome = input("Digite o novo nome: ")
                    novo_cargo = input("Digite o novo cargo: ")
                    novo_salario = float(input("Digite o novo salário: "))
                    alterar_funcionario(id_funcionario, novo_nome, novo_cargo, novo_salario)
                elif escolha_consulta == "2":
                    id = int(input("Digite o id do funcionario que você deseja deletar: "))
                    deletarfunc(id)
                elif escolha_consulta == "3":
                    id_clientes = int(input("Digite o ID do cliente que você deseja alterar: "))
                    novo_nome = input("Digite o novo nome: ")
                    novo_email = input("Digite o novo email: ")
                    novo_telefone = float(input("Digite o novo telefone: "))
                    alterar_clientes(id_clientes, novo_nome, novo_email, novo_telefone)
                elif escolha_consulta == "4":
                    idcli = int(input("Digite o id do Cliente que você deseja deletar: "))
                    deletarcli(idcli)
                elif escolha_consulta == "5":
                    id_fornecedores = int(input("Digite o ID do fornecedor que você deseja alterar: "))
                    novo_nome = input("Digite o nome: ")
                    novo_email = input("Digite o email: ")
                    novo_telefone = float(input("Digite o  telefone: "))
                    alterar_fornecedores(id_fornecedores, novo_nome, novo_email, novo_telefone)
                elif escolha_consulta == "6":
                    idforn = int(input("Digite o id do fornecedor que você deseja deletar: "))
                    deletarforn(idforn)
                elif escolha_consulta == "7":
                    id_produtos = int(input("Digite o ID do produto que você deseja alterar: "))
                    novo_nome = input("Digite o nome: ")
                    novo_preco = input("Digite o preço: ")
                    novo_estoque = float(input("Digite a quantidade disponivel pra estoque: "))
                    alterar_produto(id_produtos, novo_nome, novo_preco, novo_estoque)
                elif escolha_consulta == "8":
                    idprod = int(input("Digite o id do Produto que você deseja deletar: "))
                    deletarprod(idprod)
                elif escolha_consulta == "9":
                    print("saindo......")
                    pass
                else:
                    print("digite um valor coerente ao das opções")
            elif escolhafunc == "6":
                print("saindo......")
                pass
            else:
                print("opção invalida digite novamente")
    elif escolha == "2":
        print(25 * "-")
        print("bem vindo ao menu do cliente")
        print(25 * "-")
        print("1. se cadastre como cliente")
        print("2. consultar produtos da loja")
        print("3. sair")
        escolhacli = input("Digite o valor que deseja acessar.")
        if escolhacli == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            estatus = input("digite se o cliente sera ativo ou inativo: ")
            cadastrar_cliente(nome, email, telefone, estatus)
        elif escolhacli == "2":
            consultarprod()
        elif escolhacli == "3":
            print("saindo......")
            break
        else:
            print("Digite o um numero que seja coerente com o menu.")









