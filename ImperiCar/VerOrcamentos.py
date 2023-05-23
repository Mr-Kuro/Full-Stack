from dbOrcamentos import Database
from dbOrdens import DatabaseOrdem
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tela23:

    def __init__(self):

        self.db = Database("bd.db")

        self.janela_principal = Tk()
        self.janela_principal.title("Ver Orçamentos")
        self.janela_principal.geometry("1920x1080+0+0")
        self.janela_principal.config(bg = "#2c3e50")
        self.janela_principal.state("zoomed")
       
        self.frame1 = Frame(self.janela_principal, bg="#535c68")
        self.frame1.pack(side = TOP , fill = X)
        self.titulo = Label(self.frame1, text="Ver Orçamentos", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68", fg="white")
        self.titulo.grid(row = 0, columnspan=2, padx=10, pady=10, sticky="w")

        self.frame2 = Frame(self.frame1, bg="#535c68")
        self.frame2.grid(row = 6, column = 0, columnspan = 4, padx=10, pady=10, sticky="w")
    
        self.btnDel = Button(self.frame2, text="Deletar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085", command = self.del_orcamento)
        self.btnDel.grid(row=0, column=0, padx=10)

        self.btnOrdem = Button(self.frame2, text="Transformar em ordem de serviço", width=30, font=("CENTURY GOTHIC", 16, "bold"), fg="white", bg="#16a085", command = self.trans_ordem)
        self.btnOrdem.grid(row=0, column=1, padx=10)
        
        self.frame3 = Frame(self.janela_principal, bg="#ecf0f1")
        self.frame3.place(x=0, y=150, width=1980, height=520)


        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"), rowheight=50)
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"))
        self.tv = ttk.Treeview(self.frame3, columns =(1, 2, 3, 4, 5), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=40, stretch=NO) #você tinha escrito strech ao invés de stretch
        self.tv.heading("2", text="CPF do Cliente")
        self.tv.column("2", width=300, stretch=NO)
        self.tv.heading("3", text="CPF do Mecânico")
        self.tv.column("3", width=300, stretch=NO)
       # self.tv.heading("4", text="Peças")
       # self.tv.column("4", width=165, stretch=NO)
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

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch():
            self.tv.insert("", END, values=row)

    def del_orcamento(self):
        self.db.remove(row[0])
        messagebox.showinfo("Sucesso", "Orçamento Excluído")
        self.displayAll()

    def trans_ordem(self):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        global row
        row = data["values"]
        dO1 = DatabaseOrdem('bd.db')
        dO1.insert(row[1], row[2], row[3], row[4])
        
        bOr1 = Database('bd.db')
        bOr1.remove(int(row[0]))
        messagebox.showinfo("Sucesso", "Ordem de Serviço Criada")
        self.displayAll()
        

