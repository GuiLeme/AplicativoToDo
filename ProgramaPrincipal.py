import tkinter as tk
import ClassesPrincipais as cp
import FuncaoBackEndPP as fpp


def mainPP(dadosCliente):

    #Vamos recuperar os dados do cliente...
    nomeCliente = dadosCliente[0][1]
    afazeresCliente = fpp.abrirTabela(dadosCliente)

    # Definições da tela principal
    telaPrincipal = tk.Tk()
    telaPrincipal.title(f'Sua lista de afazeres {nomeCliente}')
    telaPrincipal.geometry('500x250+500+400')

    # Vou criar um frame
    framePrincipal = tk.Frame(telaPrincipal)
    frameCheckList = tk.Frame(framePrincipal) # Esse frame cuida dos afazeres.

    # Agora vou criar uma entry para escrever o que eu quero que seja mostrado...
    coletorInfo = tk.Entry(master=framePrincipal)

    # Labels
    bemVindo = tk.Label(framePrincipal, text = "Seja bem vindo a sua tela principal")

    # Os Checklists
    checkList = cp.CheckList(master=frameCheckList, dados = afazeresCliente)
    checkList.montarCheck()

    # Botões
    botaoAdicionar = tk.Button(master=framePrincipal, text='Adicionar Tarefa',command=lambda: fpp.novaAtividade(coletorInfo, checkList))
    botaoSalvar = tk.Button(master=framePrincipal, text='Salvar', command=lambda: fpp.salvar(checkList=checkList, dadosCliente=dadosCliente))

    # Fazendo o frame ficar colado e ajustar o tamanho:
    for i in range(0, 3):
        framePrincipal.grid_columnconfigure(i, weight=1)
        framePrincipal.grid_rowconfigure(i, weight=1)

    # Packing ou griding:
    bemVindo.grid(row = 0, column = 1, sticky = 'nsew')
    coletorInfo.grid(row = 1, column = 1, sticky = 'ns', pady = (10, 30))
    botaoAdicionar.grid(row = 2, column = 1, sticky = 'ns', padx = 100)
    checkList.grid() # esse cara foi o que eu criei, logo não tem os atributos
    botaoSalvar.grid(row = 1, column = 2, sticky = 'e')
    framePrincipal.pack(fill = 'both')
    frameCheckList.grid(row = 3, column = 0, sticky = 'wns')

    # MainLoop
    telaPrincipal.mainloop()


if __name__ == '__main__':
    mainPP([[2, 'Guilherme Pereira Leme', 'leme.guilherme.p@gmail.com', 'gui_2000']])