from app.database import get_db

class Generos:
    #CONSTRUCTOR
    def __init__(self,id=None,genero=None):
        self.id = id
        self.genero = genero
     
      
  
    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM generos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Generos(id=row[0], genero=row[1])
        return None
    
    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM generos ")
        rows = cursor.fetchall()
        generos = [Generos(id=row[0], genero=row[1]) for row in rows]
        cursor.close()
        return generos

    def save(self):
        #logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute("""
                UPDATE generos SET color = %s
                WHERE id = %s
            """, (self.genero,  self.id))
        else:
            cursor.execute("""
                INSERT INTO generos (genero) VALUES (%s)
            """, (self.genero))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM generos WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()
    
    def serialize(self):
        return {
            'id': self.id,
            'genero': self.genero,             
        }
    
    