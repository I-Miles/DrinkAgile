import mysql.connector
import connectdrink
def cadastrar_produto(p_nomeprod, p_valorprod, p_estoqueprod):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('insere_produto', (p_nomeprod, p_valorprod, p_estoqueprod))
        db_connection.commit()
        print("Produto cadastrado com sucesso")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar Produto:",error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    nome = input("Digite o nome do produto: ")
    valor = int(input("Digite o valor do produto: "))
    estoque = int(input("Digite a quantidade do produto: "))
    cadastrar_produto(nome,valor,estoque)


def cadastrar_cliente(p_nome, p_email, p_telefone,p_estatus):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('insere_cli', (p_nome, p_email, p_telefone,p_estatus))
        db_connection.commit()
        print("Cliente cadastrado com sucesso")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar Cliente:",error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    estatus = input("digite se o cliente sera ativo ou inativo: ")
    cadastrar_cliente(nome,email,telefone,estatus)

def cadastrar_func( p_nome, p_cargo, p_salario):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('insere_func', ( p_nome,p_cargo,p_salario))
        db_connection.commit()
        print("Funcionario cadastrado com sucesso")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar Funcionario:",error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    nome = input("Digite o nome do funcionario: ")
    cargo = input("Digite o cargo do funcionario: ")
    salario = input("Digite o salario do funcionario: ")
    cadastrar_func(nome,cargo,salario)

def cadastrar_fornecedor( p_nomeforn,p_emailforn,p_telefoneforn,p_idprod):
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        cursor.callproc('insere_fornecedor', ( p_nomeforn,p_emailforn,p_telefoneforn,p_idprod))
        db_connection.commit()
        print("Fornecedor cadastrado com sucesso")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar Fornecedor:",error)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    nome = input("Digite o nome do fornecedor: ")
    email = input("Digite o email do fornecedor: ")
    telefone = input("Digite o telefone do fornecedor: ")
    produto = int(input("digite o id do produto: "))
    cadastrar_fornecedor(nome,email,telefone,produto)
