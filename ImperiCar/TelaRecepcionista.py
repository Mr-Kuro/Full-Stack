from CadastrarClientes import *
#from CadastrarPecas import *
from TrocarSenha2 import *
from VerOrcamentos import *
from tkinter import *
from tkinter import ttk

class Tela2:
    
    def __init__(self, id):
        self.id = id
           
        self.janela_principal = Tk()
        self.janela_principal.title("Recepção")
        self.janela_principal.geometry("600x540")
        self.janela_principal.config(bg = "#2c3e50")
        self.img = PhotoImage(file='logo2.png')
        self.labelImg = Label(self.janela_principal, image =self.img, bg="#2c3e50")
        self.labelImg.pack()


        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP, fill = X)
        self.titulo = Label(self.frame1, text="Recepcionista", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.pack()

        self.frame2 = Frame(self.janela_principal, bg="#535c68")
        self.frame2.pack(fill = X)

        self.btnCadastrar = Button(self.frame2, command=self.add_cliente, text="Cadastrar Cliente", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085")
        self.btnCadastrar.pack(padx=10, pady=10)

        #self.btnPecas = Button(self.frame2, command=self.add_pecas, text="Cadastrar Peças", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#2980b9")
        #self.btnPecas.pack(padx=10, pady=10)

        self.btnOrcamento = Button(self.frame2, command=self.ver_orcamento, text="Ver Orçamentos", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#c0392b")
        self.btnOrcamento.pack( padx=10, pady=10)

        self.btnTrocarSenha = Button(self.frame2, command=self.trocar_senha, text="Redefinir Senha", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#40A966")
        self.btnTrocarSenha.pack( padx=10, pady=10)

        mainloop()

    def add_cliente(self):
        tela = Tela21() 

    #def add_pecas(self):
        #tela = Tela22()

    def ver_orcamento(self):
        tela = Tela23()

    def trocar_senha(self):
        tela = Tela24(self.id)
        
