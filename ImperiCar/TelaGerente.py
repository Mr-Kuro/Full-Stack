from CadastrarFuncionarios import *
from VerOrdens import *
from VerClientes import *
from TrocarSenha import *
#from VerPecas import *
from tkinter import *
from tkinter import ttk

class Tela1:

    def __init__(self, id):
        self.id = id
        
        self.janela_principal = Tk()
        self.janela_principal.title("Gerência")
        self.janela_principal.geometry("600x540")
        self.janela_principal.config(bg = "#2c3e50")
        self.img = PhotoImage(file='logo2.png')
        self.labelImg = Label(self.janela_principal, image = self.img, bg="#2c3e50")
        self.labelImg.pack()

        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP, fill = X)
        self.titulo = Label(self.frame1, text="Gerente", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.pack()

        self.frame2 = Frame(self.janela_principal, bg="#535c68")
        self.frame2.pack(fill = X)

        self.btnCadastrarFunc = Button(self.frame2, command=self.add_func, text="Gerenciar Funcionários", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#CA0000")
        self.btnCadastrarFunc.pack(padx=10, pady=10)

        self.btnVerOrdem = Button(self.frame2, command=self.ver_ordem, text="Ver ordem de serviço", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#5F00B2")
        self.btnVerOrdem.pack( padx=10, pady=10)

        self.btnVerClientes = Button(self.frame2, command=self.ver_clientes, text="Visualizar Clientes", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#0040B7")
        self.btnVerClientes.pack( padx=10, pady=10)

        self.btnTrocarSenha = Button(self.frame2, command=self.trocar_senha, text="Redefinir Senha", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#40A966")
        self.btnTrocarSenha.pack( padx=10, pady=10)

        #self.btnVerPecas = Button(self.frame2, command=self.ver_pecas, text="Visualizar Peças", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#CF2698")
        #self.btnVerPecas.pack( padx=10, pady=10)


        mainloop()

    def add_func(self):
        tela = Tela11()

    def ver_ordem(self):
        tela = Tela12()

    def ver_clientes(self):
        tela = Tela13()

    def trocar_senha(self):
        print(self.id)
        tela = Tela14(self.id)


    #def ver_pecas(self):
        #tela = Tela14()
