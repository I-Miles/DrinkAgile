import mysql.connector

def connect_database():
    try:
        db_connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='devmysql',
            database='drinkAgile'
        )

        print("Conexão Realiada com Sucesso!")
        return db_connection

    except mysql.connector.Error as error:
        if error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("O Banco de dados não existe")
        elif error.errno == mysql.connector.errorcode.ER_ACESS_DENIED_ERROR:
            print("O User name ou o password está errado!")

        else:
            print(error)
connect_database()