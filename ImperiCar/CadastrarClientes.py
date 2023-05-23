from dbClientes import Database 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tela21:

    def __init__(self):
        self.db = Database("bd.db")
        
        self.janela_principal = Tk()
        self.janela_principal.title("Cadastro de Clientes")
        self.janela_principal.geometry("1920x1080+0+0")
        self.janela_principal.config(bg = "#2c3e50")
        self.janela_principal.state("zoomed")

        self.nome = StringVar()
        self.placa = StringVar()
        self.email = StringVar()
        self.telefone = StringVar()
        self.cpf = StringVar()
        self.endereco = StringVar()

        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP, fill = X)
        self.titulo = Label(self.frame1, text="Cadastro de Clientes", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.grid(row = 0, columnspan=2, padx=10, pady=10, sticky="w")

        self.labelNome = Label(self.frame1, text="Nome", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelNome.grid(row = 1, column = 0, padx=10, pady=10, sticky="w")
        self.txtNome = Entry(self.frame1, textvariable=self.nome, font=("CENTURY GOTHIC", 16), width=30)
        self.txtNome.grid(row = 1, column = 1, padx=10, pady=10, sticky="w")

        self.labelPlaca = Label(self.frame1, text="Placa do veículo", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelPlaca.grid(row = 2, column = 0, padx=10, pady=10, sticky="w")
        self.txtPlaca = Entry(self.frame1, textvariable=self.placa, font=("CENTURY GOTHIC", 16), width=30)
        self.txtPlaca.grid(row = 2, column = 1, padx=10, pady=10, sticky="w")

        self.labelEmail = Label(self.frame1, text="Email", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelEmail.grid(row = 2, column = 2, padx=10, pady=10, sticky="w")
        self.txtEmail = Entry(self.frame1, textvariable=self.email, font=("CENTURY GOTHIC", 16), width=30)
        self.txtEmail.grid(row = 2, column = 3, padx=10, pady=10, sticky="w")

        self.labelCPF = Label(self.frame1, text="CPF", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelCPF.grid(row = 1, column = 2, padx=10, pady=10, sticky="w")
        self.txtCPF = Entry(self.frame1, textvariable=self.cpf, font=("CENTURY GOTHIC", 16), width=30)
        self.txtCPF.grid(row = 1, column = 3, padx=10, pady=10, sticky="w")

        self.labelTelefone = Label(self.frame1, text="Telefone", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelTelefone.grid(row = 3, column = 0, padx=10, pady=10, sticky="w")
        self.txtTelefone= Entry(self.frame1, textvariable=self.telefone, font=("CENTURY GOTHIC", 16), width=30)
        self.txtTelefone.grid(row = 3, column = 1, padx=10, sticky="w")

        self.labelEndereco = Label(self.frame1, text="Endereço", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelEndereco.grid(row = 3, column = 2, padx=10, pady=10, sticky="w")
        self.txtEndereco= Text(self.frame1, width=30, height=5, font=("CENTURY GOTHIC", 16))
        self.txtEndereco.grid(row = 3, column = 3, padx=10, sticky="w")

        self.frame2 = Frame(self.frame1, bg="#535c68")
        self.frame2.grid(row = 6, column = 0, columnspan = 4, padx=10, pady=10, sticky="w")
    

        self.btnAdd = Button(self.frame2, text="Adicionar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085", command = self.inserir_cliente)
        self.btnAdd.grid(row=0, column=0, padx=10)

    
        self.btnEdit = Button(self.frame2, text="Editar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#2980b9", command = self.editar_cliente)
        self.btnEdit.grid(row=0, column=1, padx=10)            


        self.btnClear = Button(self.frame2,  text="Limpar Campos", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#f39c12", command = self.clearAll)
        self.btnClear.grid(row=0, column=3, padx=10)
        

        self.frame3 = Frame(self.janela_principal, bg="#ecf0f1")
        self.frame3.place(x=0, y=350, width=1980, height=520)


        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"), rowheight=50)
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"))
        self.tv = ttk.Treeview(self.frame3, columns =(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=40, stretch=NO) #você tinha escrito strech ao invés de stretch
        self.tv.heading("2", text="Nome")
        self.tv.column("2", width=300, stretch=NO)
        self.tv.heading("3", text="Telefone")
        self.tv.column("3", width=60, stretch=NO)
        self.tv.heading("4", text="CPF")
        self.tv.column("4", width=165, stretch=NO)
        self.tv.heading("5", text="Email")
        self.tv.column("5", width=200, stretch=NO)
        self.tv.heading("6", text="Endereço")
        self.tv.column("6", width=150, stretch=NO)
        self.tv.heading("7", text="Placa")
        self.tv.column("7", width=300, stretch=NO)
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
        self.txtPlaca.delete(0, END)
        self.txtCPF.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEndereco.delete(1.0, END)
        
        self.txtNome.insert(END, row[1])
        self.txtTelefone.insert(END, row[2])
        self.txtCPF.insert(END, row[3])
        self.txtEmail.insert(END, row[4])
        self.txtEndereco.insert(END, row[5])
        self.txtPlaca.insert(END, row[6])
        

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch():
            self.tv.insert("", END, values=row)
            
    def clearAll(self):
        self.txtNome.delete(0, END)
        self.txtPlaca.delete(0, END)
        self.txtCPF.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEndereco.delete(1.0, END)

    def inserir_cliente(self):
        
        if (self.txtNome.get == "" or self.txtPlaca.get() == 0 or self.txtEmail.get() == "" or self.txtTelefone.get() == "" or self.txtCPF.get() == "" or self.txtEndereco.get(1.0, END) == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
        else:
            self.db.insert(self.txtNome.get(), self.txtTelefone.get(), self.txtCPF.get(), self.txtEmail.get(), self.txtEndereco.get(1.0, END), self.txtPlaca.get())
            messagebox.showinfo("Sucesso", "Cliente cadastrado")
            self.clearAll()
            self.displayAll()
                  

    def editar_cliente(self):
        
        if (self.txtNome.get == "" or self.txtPlaca.get() == 0 or self.txtEmail.get() == "" or self.txtTelefone.get() == "" or self.txtCPF.get() == "" or self.txtEndereco.get(1.0, END) == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
            
        else:
            self.db.update(row[0], self.txtNome.get(), self.txtTelefone.get(), self.txtCPF.get(), self.txtEmail.get(), self.txtEndereco.get(1.0, END), self.txtPlaca.get())
            messagebox.showinfo("Sucesso", "Cliente Atualizado")
            self.clearAll()
            self.displayAll()
