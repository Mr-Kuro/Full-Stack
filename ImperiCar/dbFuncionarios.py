import sqlite3

class Database:

    def __init__(self, bdFuncionarios):
        self.con     = sqlite3.connect(bdFuncionarios)
        self.cur     = self.con.cursor()
        funcionarios = """CREATE TABLE IF NOT EXISTS funcionarios(
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        senha TEXT,
                        cpf TEXT,
                        cargo TEXT)"""

        self.cur.execute(funcionarios)
        self.con.commit()

    def insert(self, nome, senha, cpf, cargo):
        self.cur.execute("INSERT INTO funcionarios VALUES (NULL, ?, ?, ?, ?)",
                         (nome, senha, cpf, cargo))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM funcionarios")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM funcionarios WHERE id = ?", (id,))
        self.con.commit()

    def update(self, id, nome, senha, cpf, cargo):
        self.cur.execute("UPDATE funcionarios SET nome=?, senha=?, cpf=?, cargo=? WHERE id=?",
                     (nome, senha, cpf, cargo, id))
        self.con.commit()

    def logar(self, username, password):
        self.cur.execute("SELECT * FROM funcionarios WHERE nome='%s' AND senha='%s'"%(username, password))
        rows = self.cur.fetchone()
        return rows

    def trocarSenha(self, id, novaSenha):
        try:
            self.cur.execute("UPDATE funcionarios SET senha=? WHERE id=?",
                         (novaSenha, id))
            self.con.commit()
            return True

        except:
            return False
    

     
