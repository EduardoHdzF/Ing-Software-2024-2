import pymysql
import datetime as dt
connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

def agregaUsuario(a, b):
    cursor.execute(
        "INSERT INTO usuarios (nombre, password) VALUES (%s, %s)", (a, b)
    )


def agregaPelicula(a, b):

    cursor.execute(
        "INSERT INTO peliculas (nombre, genero) VALUES (%s, %s)", (a, b)
    )


def agregaRenta(a, b, c):


    cursor.execute(
        "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta) VALUES (%s, %s, %s)", (a, b, c)
    )

agregaUsuario("Yo Gomez","yo.com")
agregaPelicula("La toalla del mojado","Terror")
agregaRenta(13,"1",dt.date.today())

def filtraApellidos():
    cursor.execute(
        "SELECT * FROM usuarios WHERE nombre LIKE '%mez'"
    )

connection.commit()
connection.close()


