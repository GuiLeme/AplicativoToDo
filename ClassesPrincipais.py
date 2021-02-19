import tkinter as tk

def seleciona(botao, numero):
    if numero == 1:
        botao.select()



class CheckList:
    # Crio a instância do meu objeto checklist com as informações que eu prciso
    # armazenadas na memória RAM...
    def __init__(self, master, dados):
        self.master = master
        self.valor1 = tk.IntVar(self.master, value=1)
        # Aqui esse vai para o banco de dados, pelo fato do mesmo não suportar
        # objetos tk.IntVar()
        self.dados = dados

        # Esse cara armazena as informações nos objetos, pra depois ser compactado
        # no banco de dados a partir dos dados, a posteriori
        self.guardados = []

        # Esse cara armazena os objetos...
        self.checkBoxesDaRam = []
        for item in self.dados:
            # Fazendo dessa forma abaixo, consigo já um objeto que vai me
            # retornar o valor da checkbox em algum momento que eu pedir...
            self.guardados.append([item[0], self.criarIntTk(item[1])])

    # Aqui é só um método pra retornar o um objeto para colocar na lista...
    def criarIntTk(self, dado):
        if dado == 1:
            return tk.IntVar(self.master,value=1)
        else:
            return tk.IntVar(self.master, value=0)

    def montarCheck(self):
        for item in self.guardados:
            novo = tk.Checkbutton(self.master, variable = item[1])
            novo.config(text=item[0])
            self.checkBoxesDaRam.append(novo)

    # Aqui como padrão da nossa biblioteca, é interessante dar o pack em outro lugar, que não sendo
    # o de criação da lista...
    def grid(self):
        self.textoSuasTarefas = tk.Label(self.master.master, text = 'Suas tarefas:') # Aqui queremos o master do
        self.textoSuasTarefas.grid(row=0, column=0, sticky='nsw')                    # nosso atual master...
        self.textoSuasTarefas.grid(row = 0, column = 0, sticky = 'nsw')
        for indice, item in enumerate(self.checkBoxesDaRam):
            item.grid(row = indice + 1, column = 0, sticky = 'nsw')

    # Aqui vai um método para criar uma nova tarefa para o usuário
    def mostrarTarefaNova(self):
        mostrar = self.guardados[-1]
        novo = tk.Checkbutton(self.master, text = mostrar[0], variable = mostrar[1])
        self.checkBoxesDaRam.append(novo)
        novo.grid(sticky = 'nsw')
