from app.database import get_db

class Talles:
    #CONSTRUCTOR
    def __init__(self,id=None,talle=None):
        self.id = id
        self.talle = talle
     
      
  
    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM talles WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Talles(id=row[0], talle=row[1])
        return None
    
    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM talles ")
        rows = cursor.fetchall()
        talles = [Talles(id=row[0], talle=row[1]) for row in rows]
        cursor.close()
        return talles

    def save(self):
        #logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute("""
                UPDATE talles SET talle = %s
                WHERE id = %s
            """, (self.talle,  self.id))
        else:
            cursor.execute("""
                INSERT INTO talles (talle) VALUES (%s)
            """, (self.talle))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM talles WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()
    
    def serialize(self):
        return {
            'id': self.id,
            'talle': self.talle,             
        }
    
    