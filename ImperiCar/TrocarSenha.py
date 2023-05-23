from dbFuncionarios import Database
from tkinter import *
from tkinter import messagebox

class Tela14:

    def __init__(self, id):
        self.id = int(id)
        self.db = Database("bd.db")
        
        self.janela_principal = Toplevel()
        self.janela_principal.title("Trocar senha do Gerente")
        self.janela_principal.geometry("600x540")
        self.janela_principal.config(bg = "#2c3e50")
        self.img = PhotoImage(file='logo2.png')
        self.labelImg = Label(self.janela_principal, image = self.img, bg="#2c3e50")
        self.labelImg.pack()
        
        self.senha = StringVar()

        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP, fill = X)
        self.titulo = Label(self.janela_principal, font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.pack(fill = X)
        
        self.labelSenhaNova = Label(self.frame1, text="Nova Senha", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelSenhaNova.grid(row = 2, column = 0, padx=10, pady=10, sticky="w")
        self.txtSenhaNova = Entry(self.frame1, textvariable=self.senha, font=("CENTURY GOTHIC", 16), width=30)
        self.txtSenhaNova.grid(row = 2, column = 1, padx=10, pady=10, sticky="w")

        self.frame2 = Frame(self.janela_principal, bg="#535c68")
        self.frame2.pack(fill = BOTH)

        self.btnRedefSenha = Button(self.frame2, command=self.redef_senha, text="Redefinir Senha", width=20, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#40A966")
        self.btnRedefSenha.pack( padx=10, pady=10)

        mainloop()

    def redef_senha(self):
        if self.txtSenhaNova.get() == "":
            messagebox.showerror("Erro!!", "Preencha os campos que estão vazios!!!")
        else:
            if self.db.trocarSenha(self.id, self.txtSenhaNova.get()):
                messagebox.showinfo('sucesso!', 'Senha atualizada!')
                self.janela_principal.destroy()

            else:
                messagebox.showerror('Erro!!', 'Houve um erro durante a atualização da senha!')
                self.janela_principal.destroy()
