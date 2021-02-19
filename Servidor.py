import mysql.connector as mcon

def insereBanco(dados):
    banco = mcon.connect(
        host="localhost",
        user = "root",
        passwd = "1234",
        database = "bancoDadosToDo"
    )

    # Lembrando que a tabela e o banco de dados já estão online.
    # agora o que precisamos fazer é um script que será chamado sempre que
    # for para cadastro de um novo cliente

    cursor = banco.cursor()

    insereDados = 'INSERT INTO login (nome, email, senha) VALUES (%s, %s, %s)'


    cursor.execute(insereDados, dados)

    banco.commit()

def checarExistencia(email, senha):

    banco = mcon.connect(
            host="localhost",
            user = "root",
            passwd = "1234",
            database = "bancoDadosToDo"
        )

    # Lembrando que a tabela e o banco de dados já estão online.
    # agora o que precisamos fazer é um script que será chamado sempre que
    # for para cadastro de um novo cliente

    cursor = banco.cursor()

    comando = f"SELECT * FROM login WHERE email = '{email}'"


    cursor.execute(comando)

    valores = cursor.fetchall()

    if valores[0][2] == senha:
        return True

print(insereBanco(('a', 'a', 'a')))
