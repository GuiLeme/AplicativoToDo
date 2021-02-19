# Aqui vou colocar as funções do back-end do programa principal
import mysql.connector as mcon
import tkinter as tk

# vamos definir então a função que abre a tabela do cliente
# para tornar dinâmico o front-end.

def abrirTabela(dadosCliente):
    idCliente = dadosCliente[0][0]
    nomeTabela = f'Cliente{idCliente}'
    banco = mcon.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="bancoDadosToDo"
    )

    cursor = banco.cursor()

    cursor.execute(f'SELECT * FROM {nomeTabela}')

    dados = cursor.fetchall()
    return dados


# Vamos agora montar a função do botão que recupera a atividade que o usuário
# quiser cadastrar, e assim printa na tela colocando junto com o widget CheckList...
def novaAtividade(Entry, CheckList):
    dadoString = Entry.get()
    if len(dadoString)>0:
        verdade = tk.IntVar(CheckList.master, value=0)
        CheckList.guardados.append([dadoString, verdade])
        CheckList.mostrarTarefaNova()
        Entry.delete(0, len(dadoString))

# Aqui vou criar uma função auxiliar, que verifica se tem um alguma string numa
# matriz de duas dimensões
def estaAqui(string, lista):
    valor = False
    for i in lista:
        if string in i:
            valor = True
    return valor

# Aqui vamos colocar o comando salvar para o botão.
def salvar(checkList, dadosCliente):

    idCliente = dadosCliente[0][0]
    nomeTabela = f'Cliente{idCliente}'
    banco = mcon.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="bancoDadosToDo"
    )

    cursor = banco.cursor()

    for i in range(len(checkList.guardados)):
        if not estaAqui(checkList.guardados[i][0], checkList.dados):
            print(checkList.guardados[i][0], checkList.dados)

            # Aqui a única coisa que precisa ser feita é adicionar o que não estiver no dados
            checkList.dados.append([checkList.guardados[i][0], int(checkList.guardados[i][1].get())])

            comando = f'INSERT INTO {nomeTabela} (Afazeres, Feito) VALUES ("{checkList.guardados[i][0]}", {int(checkList.guardados[i][1].get())})'

            cursor.execute(comando)

    banco.commit()




