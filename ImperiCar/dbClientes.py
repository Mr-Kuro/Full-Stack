import sqlite3

class Database:

    def __init__(self, db):
        self.con     = sqlite3.connect(db)
        self.cur     = self.con.cursor()
        clientes = """CREATE TABLE IF NOT EXISTS clientes(
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        telefone TEXT,
                        cpf TEXT,
                        email TEXT,
                        endereco TEXT,
                        placa TEXT)"""

        self.cur.execute(clientes)
        self.con.commit()

    def insert(self, nome, telefone, cpf, email, endereco, placa):
        self.cur.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (nome, telefone, cpf, email, endereco, placa))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM clientes")
        rows =  self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM clientes WHERE id = ?", (id, ))
        self.con.commit()

    def update(self, id, nome, telefone, cpf, email, endereco, placa):
        self.cur.execute("UPDATE clientes SET nome=?, telefone=?, cpf=?, email=?, endereco=?, placa=? WHERE id=?",
                     (nome, telefone, cpf, email, endereco, placa, id))
        self.con.commit()

                     
