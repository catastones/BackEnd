from app.database import get_db

class Colores:
    #CONSTRUCTOR
    def __init__(self,id=None,color=None):
        self.id = id
        self.color = color
     
      
  
    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM colores WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Colores(id=row[0], color=row[1])
        return None
    
    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM colores ")
        rows = cursor.fetchall()
        talles = [Colores(id=row[0], color=row[1]) for row in rows]
        cursor.close()
        return talles

    def save(self):
        #logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute("""
                UPDATE colores SET color = %s
                WHERE id = %s
            """, (self.color,  self.id))
        else:
            cursor.execute("""
                INSERT INTO colores (color) VALUES (%s)
            """, (self.color))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM colores WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()
    
    def serialize(self):
        return {
            'id': self.id,
            'color': self.color,             
        }
    
    