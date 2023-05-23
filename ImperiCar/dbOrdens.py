import sqlite3


class DatabaseOrdem:

    def __init__(self, bdOrdem):
        self.con = sqlite3.connect(bdOrdem)
        self.cur = self.con.cursor()
        ordemDS = """CREATE TABLE IF NOT EXISTS ordemDS(
                        id INTEGER PRIMARY KEY,
                        cpfcliente TEXT,
                        cpfmecanico TEXT,
                        valor REAL, 
                        servicos TEXT,
                        finalizada INTEGER)"""

        self.cur.execute(ordemDS)
        self.con.commit()

    def insert(self, cpfcliente, cpfmecanico, valor, servicos):
        self.cur.execute("INSERT INTO ordemDS VALUES (NULL, ?, ?, ?, ?, 0)",
                         (cpfcliente, cpfmecanico, valor, servicos))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM ordemDS")
        rows = self.cur.fetchall()
        print(rows)
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM ordemDS WHERE id = ?", (id,))
        self.con.commit()

    def update(self, id, cpfcliente, cpfmecanico, valor, servicos):
        self.cur.execute("UPDATE ordemDS SET cpfcliente=?, cpfmecanico=?, valor=?, servicos=?, finalizada=1 WHERE id=?",
                         (cpfcliente, cpfmecanico, valor, servicos, id))
        self.con.commit()
