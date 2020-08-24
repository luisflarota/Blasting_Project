import sqlite3

class Dabase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db, check_same_thread= False)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS explosives (id INTEGER PRIMARY KEY, name FIXED, density FLOAT, VOD INTEGER, Deton_Pressure FLOAT, Energy FLOAT, Weigth_S FLOAT)")
    def insert(self, name, density, vod, detpre, energy, wes):
        self.c.execute("INSERT INTO explosives VALUES (NULL, ?, ?, ?, ?, ?, ?)", (name, density, vod, detpre, energy, wes))
        self.conn.commit()
    def view(self):
        self.c.execute("SELECT * from explosives")
        rows = self.c.fetchall()
        return rows   
    def update(self, id, name, density, vod, detpre, energy, wes):
        self.c.execute("UPDATE explosives SET name = ?, density = ?, VOD = ?, Deton_Pressure =?, Energy = ?, Weigth_S = ? WHERE id = ?", (name, density, vod, detpre, energy, wes, id))
        self.conn.commit()

    def delete(self, id):
        self.c.execute("DELETE FROM explosives WHERE id = ?", (id,))
        self.conn.commit()

    def names_columns(self):
        self.c.execute("SELECT name from explosives ORDER BY density ASC")
        rows = self.c.fetchall()
        return rows
    
    def show_density(self, tipoexplosive):
        self.c.execute("SELECT density from explosives WHERE name = ?", (tipoexplosive,))
        rows = self.c.fetchall()
        return rows
    
    def show_we(self, tipoexplosive):
        self.c.execute("SELECT Weigth_S from explosives WHERE name = ?", (tipoexplosive,))
        rows = self.c.fetchall()
        return rows
    def __del__(self):
        self.conn.close()

