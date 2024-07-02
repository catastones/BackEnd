from app.database import get_db

class Producto:
    #CONSTRUCTOR
    def __init__(self,id=None,nombre=None,descripcion=None,id_talle=None,id_color=None,id_genero=None,url_image=None,price=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_talle = id_talle
        self.id_color = id_color
        self.id_genero = id_genero
        self.url_image = url_image
        self.price = price
        
    @staticmethod
    def get_by_gen(id_genero):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""SELECT 
            p.id as id,
	        p.nombre as nombre, 
            p.descripcion as descripcion,
            t.talle as talle,
            c.color as color,
            g.genero as genero,
            p.url_image as url_image,
            p.price as price
            FROM productos as p
            left JOIN talles as t on t.id = p.id_talle
            left JOIN colores as c on c.id = p.id_color
            left JOIN generos as g on g.id = p.id_genero
            where g.id=%s """, (id_genero,))
        rows = cursor.fetchall()
        cursor.close()
        productos = [Producto(id=row[0], nombre=row[1], descripcion=row[2], id_talle=row[3], id_color=row[4], id_genero=row[5],url_image=row[6],price=row[7]) for row in rows]       
        return productos
    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(id=row[0], nombre=row[1], descripcion=row[2], id_talle=row[3], id_color=row[4], id_genero=row[5],url_image=row[6],price=row[7])
        return None
    
    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            """SELECT 
            p.id as id,
	        p.nombre as nombre, 
            p.descripcion as descripcion,
            t.talle as talle,
            c.color as color,
            g.genero as genero,
            p.url_image as url_image,
            p.price as price
            FROM productos as p
            left JOIN talles as t on t.id = p.id_talle
            left JOIN colores as c on c.id = p.id_color
            left JOIN generos as g on g.id = p.id_genero""")
        rows = cursor.fetchall()
        productos = [Producto(id=row[0], nombre=row[1], descripcion=row[2], id_talle=row[3], id_color=row[4], id_genero=row[5],url_image=row[6],price=row[7]) for row in rows]
        cursor.close()
        return productos

    def save(self):
        #logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        print(self.id)
        if self.id  :
            cursor.execute("""
                UPDATE productos SET nombre = %s, descripcion = %s, id_talle = %s, id_color = %s, id_genero = %s, url_image = %s,price = %s
                WHERE id = %s
            """, (self.nombre, self.descripcion, self.id_talle, self.id_color,self.id_genero,self.url_image, self.price, self.id))
        else:
            cursor.execute("""
                INSERT INTO productos (nombre, descripcion, id_talle, id_color,id_genero,url_image,price) VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.nombre, self.descripcion, self.id_talle, self.id_color,self.id_genero,self.url_image, self.price))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'talle':self.id_talle,
            'color':self.id_color,
            'genero':self.id_genero,
            'url_image':self.url_image,
            'price':self.price,           
        }
    
    