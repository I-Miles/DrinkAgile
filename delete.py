import mysql.connector
import connectdrink


def deletarfunc(p_id):
    try:
        connect_database = connectdrink.connect_database()
        cursor = connect_database.cursor()
        cursor.execute("SELECT COUNT(*) FROM funcionarios WHERE id = %s", (p_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            print("Funcionário não encontrado!")
        else:
            cursor.callproc('procremovefuncionario', (p_id,))
            connect_database.commit()
            print("Funcionário deletado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao deletar funcionário: ", error)
    finally:
        if 'db_connection' in locals() and connect_database.is_connected():
            cursor.close()
            connect_database.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    id = int(input("Digite o id do funcionario que você deseja deletar: "))
    deletarfunc(id)

def deletarforn(p_id):
    try:
        connect_database = connectdrink.connect_database()
        cursor = connect_database.cursor()
        cursor.execute("SELECT COUNT(*) FROM fornecedores WHERE idforn = %s", (p_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            print("Fornecedor não encontrado!")
        else:
            cursor.callproc('procremovefornecedores', (p_id,))
            connect_database.commit()
            print("Fornecedor deletado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao deletar fornecedor: ", error)
    finally:
        if 'db_connection' in locals() and connect_database.is_connected():
            cursor.close()
            connect_database.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    idforn = int(input("Digite o id do fornecedor que você deseja deletar: "))
    deletarforn(idforn)

def deletarprod(p_id):
    try:
        connect_database = connectdrink.connect_database()
        cursor = connect_database.cursor()
        cursor.execute("SELECT COUNT(*) FROM produtos WHERE idprod = %s", (p_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            print("Produto não encontrado!")
        else:
            cursor.callproc('procremoveprodutos', (p_id,))
            connect_database.commit()
            print("Produto deletado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao deletar produto: ", error)
    finally:
        if 'db_connection' in locals() and connect_database.is_connected():
            cursor.close()
            connect_database.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    idprod = int(input("Digite o id do Produto que você deseja deletar: "))
    deletarprod(idprod)

def deletarcli(p_id):
    try:
        connect_database = connectdrink.connect_database()
        cursor = connect_database.cursor()
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE idcli = %s", (p_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            print("Cliente não encontrado!")
        else:
            cursor.callproc('procremoveclientes', (p_id,))
            connect_database.commit()
            print("Cliente deletado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao deletar cliente: ", error)
    finally:
        if 'db_connection' in locals() and connect_database.is_connected():
            cursor.close()
            connect_database.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    idcli = int(input("Digite o id do Cliente que você deseja deletar: "))
    deletarcli(idcli)