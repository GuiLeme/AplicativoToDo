from time import sleep
import tkinter as tk
import mysql.connector as mcon


# Aqui vou fazer a inserção de um novo usuário
def insereBanco(nomeNovo, emailNovo, senhaNova, window):
    nome = nomeNovo.get()
    email = emailNovo.get()
    senha = senhaNova.get()
    dados = [nome, email, senha]
    banco = mcon.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="bancoDadosToDo"
    )

    # Lembrando que a tabela e o banco de dados já estão online.
    # agora o que precisamos fazer é um script que será chamado sempre que
    # for para cadastro de um novo cliente

    cursor = banco.cursor()

    insereDados = 'INSERT INTO login (nome, email, senha) VALUES (%s, %s, %s)'

    cursor.execute(insereDados, dados)

    banco.commit()
    print('usuario cadastrado')

    cursor.execute(f"SELECT * FROM login WHERE email = '{email}'")
    dados = cursor.fetchall()

    # Aqui já aproveito para criar a tabela
    criaTabelaCliente(dados, cursor)


    window.destroy()

def pegarInfo(email):
    banco = mcon.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="bancoDadosToDo"
    )

    # Lembrando que a tabela e o banco de dados já estão online.
    # agora o que precisamos fazer é um script que será chamado sempre que
    # for para cadastro de um novo cliente

    cursor = banco.cursor()

    comando = f"SELECT * FROM login WHERE email = '{email}'"

    cursor.execute(comando)

    valores = cursor.fetchall()

    return valores

# Aqui vou criar uma função que cria uma tabela para o cliente...
def criaTabelaCliente(dados, cursor):

    idCliente = dados[0][0]
    nomeTabela = f'Cliente{idCliente}'
    comando = f'CREATE TABLE {nomeTabela} (Afazeres VARCHAR(200), Feito INT(1))'

    cursor.execute(comando)

# Essa função checa a existência de um usuário
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

    try:
        if valores[0][3] == senha:
            return True
    except:
        return False

def abrirOutraAba(nomeNovaAba, width, heith):
    novaAba = tk.Tk()
    novaAba.title(nomeNovaAba)
    novaAba.geometry(f'{width}x{heith}+500+500')
    return novaAba

# Agora, aqui vou entrar com a programação da tela inicial... até agora tinhamos o menu onde entramos
def iniciarTelaInicial():
    MenuInicial = tk.Tk()



    MenuInicial.mainloop()
