import mysql.connector
import connectdrink

def alterar_funcionario(id_funcionario, novo_nome, novo_cargo, novo_salario):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('procalterarfuncionario', (id_funcionario, novo_nome, novo_cargo, novo_salario))
        db_connection.commit()
        for result in cursor.stored_results():
            print(result.fetchone()[0])
    except mysql.connector.Error as error:
        print("Erro ao alterar o funcionário:", error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    id_funcionario = int(input("Digite o ID do funcionário que você deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_cargo = input("Digite o novo cargo: ")
    novo_salario = float(input("Digite o novo salário: "))
    alterar_funcionario(id_funcionario, novo_nome, novo_cargo, novo_salario)

def alterar_clientes(id_clientes, novo_nome, novo_email, novo_telefone):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('procalterarclientes', (id_clientes, novo_nome, novo_email, novo_telefone))
        db_connection.commit()
        for result in cursor.stored_results():
            print(result.fetchone()[0])
    except mysql.connector.Error as error:
        print("Erro ao alterar o cliente:", error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    id_clientes = int(input("Digite o ID do cliente que você deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_email = input("Digite o novo email: ")
    novo_telefone = float(input("Digite o novo telefone: "))
    alterar_clientes(id_clientes, novo_nome, novo_email, novo_telefone)

def alterar_produto(id_produtos, novo_nome, novo_preco, novo_estoque):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('procalterarprodutos', (id_produtos, novo_nome, novo_preco, novo_estoque))
        db_connection.commit()
        for result in cursor.stored_results():
            print(result.fetchone()[0])
    except mysql.connector.Error as error:
        print("Erro ao alterar o cliente:", error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    id_produtos = int(input("Digite o ID do produto que você deseja alterar: "))
    novo_nome = input("Digite o nome: ")
    novo_preco = input("Digite o preço: ")
    novo_estoque = float(input("Digite a quantidade disponivel pra estoque: "))
    alterar_produto(id_produtos, novo_nome, novo_preco, novo_estoque)

def alterar_fornecedores(id_fornecedores, novo_nome, novo_email, novo_telefone):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('procalterarfornecedores', (id_fornecedores, novo_nome, novo_email, novo_telefone))
        db_connection.commit()
        for result in cursor.stored_results():
            print(result.fetchone()[0])
    except mysql.connector.Error as error:
        print("Erro ao alterar o cliente:", error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")


if __name__ == "__main__":
    id_fornecedores = int(input("Digite o ID do fornecedor que você deseja alterar: "))
    novo_nome = input("Digite o nome: ")
    novo_email = input("Digite o email: ")
    novo_telefone = float(input("Digite o  telefone: "))
    alterar_fornecedores(id_fornecedores, novo_nome, novo_email, novo_telefone)