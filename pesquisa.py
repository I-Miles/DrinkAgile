import mysql.connector
import connectdrink

def consultarfunc():
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        sql = "SELECT * FROM funcionarios"
        cursor.execute(sql)
        print("Nome do ID\tNome\tCargo\tSalario")
        for row in cursor.fetchall():
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    except mysql.connector.Error as error:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    consultarfunc()

def consultarcli():
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        print("Nome do ID\tNome\tE-mail\tTelefone")
        for row in cursor.fetchall():
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    except mysql.connector.Error as error:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    consultarcli()

def consultarprod():
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        print("Nome do ID\tNome\tPreço\tEstoque")
        for row in cursor.fetchall():
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    except mysql.connector.Error as error:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    consultarprod()

def consultarforn():
    try:
        db_connection = connectdrink.connect_database()
        cursor = db_connection.cursor()
        sql = "SELECT * FROM fornecedores"
        cursor.execute(sql)
        print("Nome do ID\tNome\tE-mail\tTelefone\tID_Produtos")
        for row in cursor.fetchall():
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    except mysql.connector.Error as error:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")


if __name__ == "__main__":
    consultarforn()

