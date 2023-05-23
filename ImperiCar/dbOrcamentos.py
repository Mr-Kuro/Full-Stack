import sqlite3

class Database:

    def __init__(self, bdOrcamento):
        self.con     = sqlite3.connect(bdOrcamento)
        self.cur     = self.con.cursor()
        orcamento  = """CREATE TABLE IF NOT EXISTS orcamento(
                        id INTEGER PRIMARY KEY,
                        cpfcliente TEXT,
                        cpfmecanico TEXT,
                        valor REAL, 
                        servicos TEXT)"""

        self.cur.execute(orcamento)
        self.con.commit()

        
    def insert(self, cpfcliente, cpfmecanico, valor, servicos):
        self.cur.execute("INSERT INTO orcamento VALUES (NULL, ?, ?, ?, ?)",
                         (cpfcliente, cpfmecanico, valor, servicos))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM orcamento")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM orcamento WHERE id = ?", (id,))
        self.con.commit()

    def update(self, id, cpfcliente, cpfmecanico, valor, servicos):
        self.cur.execute("UPDATE orcamento SET cpfcliente=?, cpfmecanico=?, valor=?, servicos=? WHERE id=?",
                         (cpfcliente, cpfmecanico, valor, servicos, id))
        self.con.commit()
