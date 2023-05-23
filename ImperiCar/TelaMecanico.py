from tkinter import *
from tkinter import ttk
from TrocarSenha3 import *
from CadastrarOrcamentos import *
from VerOrdens2 import *

class Tela3:

    def __init__(self, id, cpf):
        self.id = id

        self.cpf = cpf
        self.janela_principal = Tk()
        self.janela_principal.title("Mecânico")
        self.janela_principal.geometry("600x540")
        self.janela_principal.config(bg = "#2c3e50")
        self.img = PhotoImage(file='logo2.png')
        self.labelImg = Label(self.janela_principal, image =self.img, bg="#2c3e50")
        self.labelImg.pack()


        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP, fill = X)
        self.titulo = Label(self.frame1, text="Mecânico", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.pack()

        self.frame2 = Frame(self.janela_principal, bg="#535c68")
        self.frame2.pack(fill = X)

        self.btnOrçamento = Button(self.frame2, command=self.add_orçamento, text="Cadastrar Orçamento", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085")
        self.btnOrçamento.pack(padx=10, pady=10)

        self.btnOrdem = Button(self.frame2, command=self.ver_ordem, text="Visualizar Ordem de serviço", width=25, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#2980b9")
        self.btnOrdem.pack(padx=10, pady=10)

        self.btnTrocarSenha = Button(self.frame2, command=self.trocar_senha, text="Redefinir Senha", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#40A966")
        self.btnTrocarSenha.pack( padx=10, pady=10)

        mainloop()


    def add_orçamento(self):
        tela = Tela31()

    def ver_ordem(self):
        tela = Tela32(self.cpf)

    def trocar_senha(self):
        tela = Tela33(self.id)

