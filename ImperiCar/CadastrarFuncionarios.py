from dbFuncionarios import Database 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tela11:

    def __init__(self):
        self.db = Database("bd.db")
        
        self.janela_principal = Tk()
        self.janela_principal.title("Sistema de gerenciamento de Funcionários")
        self.janela_principal.geometry("1920x1080+0+0")
        self.janela_principal.config(bg = "#2c3e50")
        self.janela_principal.state("zoomed")

        self.nome = StringVar()
        self.senha = StringVar()       
        self.cpf = StringVar()
        self.cargo = StringVar()

        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP, fill = X)
        self.titulo = Label(self.frame1, text="Sistema de Gerenciamento de Funcionários", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.grid(row = 0, columnspan=2, padx=10, pady=10, sticky="w")

        self.labelNome = Label(self.frame1, text="Nome do Funcionário", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelNome.grid(row = 1, column = 0, padx=10, pady=10, sticky="w")
        self.txtNome = Entry(self.frame1, textvariable=self.nome, font=("CENTURY GOTHIC", 16), width=30)
        self.txtNome.grid(row = 1, column = 1, padx=10, pady=10, sticky="w")

        self.labelSenha = Label(self.frame1, text="Senha", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelSenha.grid(row = 1, column = 2, padx=10, pady=10, sticky="w")
        self.txtSenha = Entry(self.frame1, textvariable=self.senha, font=("CENTURY GOTHIC", 16), width=30, show="*")
        self.txtSenha.grid(row = 1, column = 3, padx=10, pady=10, sticky="w")

        

        self.labelCPF = Label(self.frame1, text="CPF", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelCPF.grid(row = 2, column = 2, padx=10, pady=10, sticky="w")
        self.txtCPF = Entry(self.frame1, textvariable=self.cpf, font=("CENTURY GOTHIC", 16), width=30)
        self.txtCPF.grid(row = 2, column = 3, padx=10, pady=10, sticky="w")

        self.labelCargo = Label(self.frame1, text="Cargo do Funcionário", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelCargo.grid(row = 2, column = 0, padx=10, pady=10, sticky="w")
        self.txtCargo= Entry(self.frame1, textvariable=self.cargo, font=("CENTURY GOTHIC", 16), width=30)
        self.txtCargo.grid(row = 2, column = 1, padx=10, sticky="w")

        
        self.frame2 = Frame(self.frame1, bg="#535c68")
        self.frame2.grid(row = 4, column = 0, columnspan = 4, padx=10, pady=10, sticky="w")
    

        self.btnAdd = Button(self.frame2, text="Adicionar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085", command = self.inserir_funcionario)
        self.btnAdd.grid(row=0, column=0, padx=10)
    
        self.btnEdit = Button(self.frame2, text="Editar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#2980b9", command = self.editar_funcionario)
        self.btnEdit.grid(row=0, column=1, padx=10)

        self.btnDel = Button(self.frame2, text="Deletar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085", command = self.del_funcionario)
        self.btnDel.grid(row=0, column=2, padx=10)

        self.btnClear = Button(self.frame2,  text="Limpar Campos", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#f39c12", command = self.clearAll)
        self.btnClear.grid(row=0, column=3, padx=10)

        
        

        self.frame3 = Frame(self.janela_principal, bg="#ecf0f1")
        self.frame3.place(x=0, y=250, width=1980, height=520)


        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"), rowheight=50)
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"))
        self.tv = ttk.Treeview(self.frame3, columns =(1, 2, 3, 4, 5 ), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=40, stretch=NO)
        self.tv.heading("2", text="Nome")
        self.tv.column("2", width=300, stretch=NO)
        self.tv.heading("3", text="Senha")
        self.tv.column("3", width=60, stretch=NO)
        self.tv.heading("4", text="CPF")
        self.tv.column("4", width=165, stretch=NO)
        self.tv.heading("5", text="Cargo")
        self.tv.column("5", width=200, stretch=NO)        
        self.tv["show"] = "headings"

        self.tv.bind("<ButtonRelease-1>", self.getData)
        self.tv.pack(fill=X)
        self.displayAll()
        mainloop()


    def getData(self, event):
        
        selected_row = self.tv.focus()            
        data = self.tv.item(selected_row)
        global row
        row = data["values"]
        
        self.txtNome.delete(0, END)
        self.txtSenha.delete(0, END)
        self.txtCPF.delete(0, END)
        self.txtCargo.delete(0, END)
        
        
        self.txtNome.insert(END, row[1])
        self.txtSenha.insert(END, row[2])
        self.txtCPF.insert(END, row[3])
        self.txtCargo.insert(END, row[4])
        
        

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch():
            self.tv.insert("", END, values=row)
            
    def clearAll(self):
        self.txtNome.delete(0, END)
        self.txtSenha.delete(0, END)
        self.txtCPF.delete(0, END)
        self.txtCargo.delete(0, END)
        

    def inserir_funcionario(self):
        
        if (self.txtNome.get == "" or self.txtSenha.get() == 0 or self.txtCPF.get() == "" or self.txtCargo.get() == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
        else:
            self.db.insert(self.txtNome.get(), self.txtSenha.get(), self.txtCPF.get(), self.txtCargo.get())
            messagebox.showinfo("Sucesso", "Funcionário cadastrado")
            self.clearAll()
            self.displayAll()
                  

    def editar_funcionario(self):
        
        if (self.txtNome.get == "" or self.txtSenha.get() == 0 or self.txtCPF.get() == "" or self.txtCargo.get() == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
            
        else:
            self.db.update(row[0], self.txtNome.get(), self.txtSenha.get(), self.txtCPF.get(), self.txtCargo.get())
            messagebox.showinfo("Sucesso", "Funcionário Atualizado")
            self.clearAll()
            self.displayAll()

    def del_funcionario(self):
        self.db.remove(row[0])
        messagebox.showinfo("Sucesso", "Funcionário Excluído")
        self.clearAll()
        self.displayAll()
