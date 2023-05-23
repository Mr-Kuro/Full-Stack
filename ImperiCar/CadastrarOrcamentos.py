from dbOrcamentos import Database
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tela31:

    def __init__(self):

        self.db = Database("bd.db")

        self.janela_principal = Tk()
        self.janela_principal.title("Cadastro de Orçamentos")
        self.janela_principal.geometry("1920x1080+0+0")
        self.janela_principal.config(bg = "#2c3e50")
        self.janela_principal.state("zoomed")

        self.cpfcliente = StringVar()
        self.cpfmecanico = StringVar()
        #self.pecas = StringVar()
        self.valor = StringVar()
        self.servicos = StringVar()
       
        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP, fill = X)
        self.titulo = Label(self.frame1, text="Cadastro de Orçamentos", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.grid(row = 0, columnspan=2, padx=10, pady=10, sticky="w")

        self.labelCpfcliente= Label(self.frame1, text="CPF do Cliente", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelCpfcliente.grid(row = 1, column = 0, padx=10, pady=10, sticky="w")
        self.txtCpfcliente = Entry(self.frame1, textvariable=self.cpfcliente, font=("CENTURY GOTHIC", 16), width=30)
        self.txtCpfcliente.grid(row = 1, column = 1, padx=10, pady=10, sticky="w")

        self.labelCpfmecanico = Label(self.frame1, text="CPF do Mecânico", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelCpfmecanico.grid(row = 2, column = 0, padx=10, pady=10, sticky="w")
        self.txtCpfmecanico = Entry(self.frame1, textvariable=self.cpfmecanico, font=("CENTURY GOTHIC", 16), width=30)
        self.txtCpfmecanico.grid(row = 2, column = 1, padx=10, pady=10, sticky="w")

        #self.labelPecas = Label(self.frame1, text="Peças", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        #self.labelPecas.grid(row = 2, column = 2, padx=10, pady=10, sticky="w")
        #self.txtPecas = Entry(self.frame1, textvariable=self.pecas, font=("CENTURY GOTHIC", 16), width=30)
        #self.txtPecas.grid(row = 2, column = 3, padx=10, pady=10, sticky="w")

        self.labelValor = Label(self.frame1, text="Valor", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelValor.grid(row = 1, column = 2, padx=10, pady=10, sticky="w")
        self.txtValor = Entry(self.frame1, textvariable=self.valor, font=("CENTURY GOTHIC", 16), width=30)
        self.txtValor.grid(row = 1, column = 3, padx=10, pady=10, sticky="w")

        self.labelServicos = Label(self.frame1, text="Serviços", bg="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelServicos.grid(row = 2, column = 2, padx=10, pady=10, sticky="w")
        self.txtServicos = Entry(self.frame1, textvariable=self.servicos, font=("CENTURY GOTHIC", 16), width=30)
        self.txtServicos.grid(row = 2, column = 3, padx=10, sticky="w")

        self.frame2 = Frame(self.frame1, bg="#535c68")
        self.frame2.grid(row = 6, column = 0, columnspan = 4, padx=10, pady=10, sticky="w")
    

        self.btnAdd = Button(self.frame2, text="Adicionar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085", command = self.inserir_cliente)
        self.btnAdd.grid(row=0, column=0, padx=10)

    
        self.btnEdit = Button(self.frame2, text="Editar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#2980b9", command = self.editar_cliente)
        self.btnEdit.grid(row=0, column=1, padx=10)            


        self.btnClear = Button(self.frame2,  text="Limpar Campos", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#f39c12", command = self.clearAll)
        self.btnClear.grid(row=0, column=3, padx=10)
        

        self.frame3 = Frame(self.janela_principal, bg="#ecf0f1")
        self.frame3.place(x=0, y=225, width=1980, height=520)


        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"), rowheight=50)
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"))
        self.tv = ttk.Treeview(self.frame3, columns =(1, 2, 3, 4, 5), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=40, stretch=NO)
        self.tv.heading("2", text="CPF do Cliente")
        self.tv.column("2", width=300, stretch=NO)
        self.tv.heading("3", text="CPF do Mecânico")
        self.tv.column("3", width=300, stretch=NO)
        #self.tv.heading("4", text="Peças")
        #self.tv.column("4", width=165, stretch=NO)
        self.tv.heading("4", text="Valor")
        self.tv.column("4", width=200, stretch=NO)
        self.tv.heading("5", text="Serviços")
        self.tv.column("5", width=150, stretch=NO)
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
        
        self.txtCpfcliente.delete(0, END)
        self.txtCpfmecanico.delete(0, END)
        #self.txtPecas.delete(0, END)
        self.txtValor.delete(0, END)
        self.txtServicos.delete(0, END)
        
        self.txtCpfcliente.insert(END, row[1])
        self.txtCpfmecanico.insert(END, row[2])
        #self.txtPecas.insert(END, row[3])
        self.txtValor.insert(END, row[3])
        self.txtServicos.insert(END, row[4])

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch():
            self.tv.insert("", END, values=row)
            
    def clearAll(self):
        self.txtCpfcliente.delete(0, END)
        self.txtCpfmecanico.delete(0, END)
        #self.txtPecas.delete(0, END)
        self.txtValor.delete(0, END)
        self.txtServicos.delete(0, END)

    def inserir_cliente(self):
        
        if (self.txtCpfcliente.get() == "" or self.txtCpfmecanico.get() == 0 or self.txtValor.get() == "" or self.txtServicos.get() == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
        else:
            self.db.insert(self.txtCpfcliente.get(), self.txtCpfmecanico.get(), self.txtValor.get(), self.txtServicos.get())
            messagebox.showinfo("Sucesso", "Orçamento cadastrado")
            self.clearAll()
            self.displayAll()
                  

    def editar_cliente(self):
        
        if (self.txtCpfcliente.get() == "" or self.txtCpfmecanico.get() == 0 or self.txtValor.get() == "" or self.txtServicos.get() == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
            
        else:
            self.db.update(row[0], self.txtCpfcliente.get(), self.txtCpfmecanico.get(), self.txtValor.get(), self.txtServicos.get())
            messagebox.showinfo("Sucesso", "Orçamento Atualizado")
            self.clearAll()
            self.displayAll()
        

