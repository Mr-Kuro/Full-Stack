
from tkinter import *
from TelaGerente import *
from TelaRecepcionista import *
from TelaMecanico import *
from dbFuncionarios import Database

def login():
    db = Database("bd.db")
    # Criando variaveis para armazenar o que foi digitado pelo usuário
    uname = username.get()
    pwd = password.get()

    #Verificando se algum dos campos está vazio
    if uname == "" or pwd == "":
        #Se estiver, peço que o usuário preencha
        message.set("Preencha os campos que estão vazios!!!")
    #Se não estiver...
    else:
        # buscando um admin na tabela, que possua username e senha iguais aos que foram digitados pelo usuário
        # Verifica se a busca gerou algum resultado
        rows = db.logar(uname, pwd)
        print(rows)
        if rows:
            #Se gerou, o login é feito
            message.set("Login efetuado com sucesso!!!")

            #verificando qual a função do funcionário para chamar a tela correspondente
            funcao = rows[4]

            if funcao == "gerente" or funcao == 'Gerente' or funcao == 'GERENTE':
                janela_principal.destroy()
                telaGerente = Tela1(rows[0])

            elif funcao == "recepcionista" or funcao == 'Recepcionista' or funcao == 'RECEPCIONISTA':
                janela_principal.destroy()
                telaRecepcionista = Tela2(rows[0])

            elif funcao == "mecânico" or funcao == 'mecanico' or funcao == 'Mecânico' or funcao == 'Mecanico' or funcao == 'MECÂNICO' or funcao == 'MECANICO':
                janela_principal.destroy()
                telaMecanico = Tela3(rows[0], rows[3])



            #Caso contrário...
        else:
            # Aviso pro usuário que tem parada errada aí irmão
            message.set("Nome de usuário ou Senha incorreto!!!")

def Loginform():
    #Criando a janela    
    global janela_principal
    janela_principal = Tk()
    #Mudando o titulo da janela
    janela_principal.title("Login do Sistema")
    #Alterando o tamanho da janela
    janela_principal.geometry("350x520")
    #Alterando a cor de fundo da janela
    janela_principal["bg"] = "#C1C1CE"

    #Criando as variaveis globais
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    img = PhotoImage(file='logo.png')
    labelImg = Label(janela_principal, image =img, bg="#C1C1CE")
    labelImg.place(x=25, y=0)
    

    #Criando o label de titulo
    labelTitulo = Label(janela_principal, width=300, text="Login Mecânica ImperiCar",
                        bg="#0B95E3", fg="white", font=("Century Gothic", 12, "bold"))
    labelTitulo.place(x=0, y=300)

    #Criando o label do nome de usuario
    labelUsername = Label(janela_principal, text="Nome de usuário", bg="#C1C1CE",
                          fg="black", font=("Century Gothic", 12, "bold"))
    labelUsername.place(x=10, y=350)
    #Criando a caixa de texto onde será digitado o nome de usuário
    txtUsername = Entry(janela_principal, textvariable=username, bg="white",
                          fg="black", font=("Century Gothic", 12, "bold"))
    txtUsername.place(x=150, y=352)

    #Criando o label da senha
    labelPassword = Label(janela_principal, text="Senha", bg="#C1C1CE",
                          fg="black", font=("Century Gothic", 12, "bold"))
    labelPassword.place(x=10, y=390)
    #Criando a caixa de texto onde será digitada a senha
    txtPassword = Entry(janela_principal, textvariable=password, bg="white",
                          fg="black", font=("Century Gothic", 12, "bold"), show="*")
    txtPassword.place(x=150, y=392)

    #Criando o label para informar o usuário o resultado de sua tentativa de login
    labelSaida = Label(janela_principal, text="", textvariable=message, bg="#C1C1CE",
                          fg="black", font=("Century Gothic", 12, "bold"))
    labelSaida.place(x = 20, y = 420)
    
    #Criando o botão de login
    btnLogin = Button(janela_principal, text="Login", width=10, height=1, command=login,
                      bg="#0B95E3", fg="white", font=("Century Gothic", 12, "bold"))
    btnLogin.place(x=125, y=470)
    
    #Executando a janela
    janela_principal.mainloop()
    
#Chamando o método que executa a interface
Loginform()





                        
