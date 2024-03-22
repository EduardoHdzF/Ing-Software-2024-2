from alchemyClasses import db

class pelicula(db.Model):

    __tablename__ = 'pelicula'
    idPelicula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    genero = db.Column(db.String)
    duracion = db.Column(db.Integer)
    inventario = db.Column(db.Integer)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'Nombre:{self.nombre}\nGenero:{self.genero}\nDuracion:{self.duracion}\Inventario: {self.inventario}'