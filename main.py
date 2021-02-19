import tkinter as tk
from FuncaoBeckEnd import *
from ProgramaPrincipal import *

passagem = False
# Aqui, ao receber os dados do cliente,
# e conseguir fazer um menu principal
# dinâmico que depende do cliente logado
dadosCliente = []

def mainMenu():
    # Criando o menu inicial
    menuInicial = tk.Tk()
    menuInicial.geometry("500x250+500+200")# A parte do algoxalgo é a dimensão, as somas são a posição que eu quero
    menuInicial.title("To do List")        # Que a minha aplicação apareça
    menuInicial.minsize(200, 100)
    menuInicial['bg'] = '#AED0D9' #bg é background, seria a nossa cor de fundo, aqui no caso pode ser em hexa

    # Criando uma textbox que vai receber a info
    emailCliente = tk.Entry(menuInicial, textvariable = "digite seu email...")
    senhaCliente = tk.Entry(menuInicial, textvariable = "digite sua senha...")


    # associar um evento no meu botão
    # para eu controlar a entrada da pessoa, eu vou ter que modificar
    # tambem uma variável, e de acordo com isso, o programa vai deixar
    # ou não ser aberto o menu do cliente...
    # pra resolver isso, tive que criar uma variável global chamada
    # passagem
    usuErrado = tk.Label(menuInicial, text='Me desculpe, usuário errado', bg='#AED0D9')
    def funcBotaoCliente():
        email = emailCliente.get()
        senha = senhaCliente.get()
        valor = checarExistencia(email, senha)
        contador = 0
        global passagem
        global dadosCliente
        if valor:
            usuErrado.destroy()
            passagem = True
            # aqui pego as informações para entrar na tabela do cliente.
            dadosCliente = pegarInfo(email)
            menuInicial.destroy()
        else:
            if contador != 0:
                usuErrado.destroy()
                contador -= 0
            usuErrado.pack()


    # Aqui temos a função de cadastro de usuário
    def funcBotaoNovo():
        novaAba = abrirOutraAba("Criando nova conta", 500, 250)

        # Label
        bemVindo = tk.Label(novaAba, text = "Seja bem vindo, coloque seu nome e email!")
        msgEmail = tk.Label(novaAba, text = "Coloque seu email")
        msgSenha = tk.Label(novaAba, text = "Coloque sua senha")
        msgNome = tk.Label(novaAba, text = "Coloque seu nome")

        # Aqui vamos colocar o entry DB
        nomeNovo = tk.Entry(novaAba)
        emailNovo = tk.Entry(novaAba)
        senhaNova = tk.Entry(novaAba)

        # Botão
        botao = tk.Button(novaAba, text = "Criar usuário", command = lambda: insereBanco(nomeNovo, emailNovo, senhaNova, novaAba))

        # Fazendo o Pack
        bemVindo.pack()
        msgNome.pack()
        nomeNovo.pack()
        msgEmail.pack()
        emailNovo.pack()
        msgSenha.pack()
        senhaNova.pack()
        botao.pack()
        novaAba.mainloop()


    # Adicionando um botão
    botaoEntrar = tk.Button(menuInicial, text = 'Entrar', command = funcBotaoCliente, borderwidth = 0)
    botaoNovo = tk.Button(menuInicial, text = 'Sou novo aqui', command = funcBotaoNovo)


    #é só algo interessante mesmo, nada demais
    # Definir o label:
    emailLbl = tk.Label(menuInicial, text = "Digite seu email:")
    emailLbl['bg'] = '#AED0D9'
    senhaLbl = tk.Label(menuInicial, text = "Digite a sua senha:")
    senhaLbl['bg'] = '#AED0D9'


    # Fazendo o Packing
    emailLbl.pack()
    emailCliente.pack()
    senhaLbl.pack()
    senhaCliente.pack()
    botaoEntrar.pack()
    botaoNovo.pack()

    menuInicial.mainloop()
    return passagem
#Fim da Função do menu de entrada

# Rodando menu principal
valor = mainMenu()

# Agora vou rodar a aplicação principal, de fato
if valor:
    mainPP(dadosCliente)