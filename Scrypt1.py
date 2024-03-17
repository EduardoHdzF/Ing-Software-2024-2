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
    connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)    
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO peliculas (nombre, genero) VALUES (%s, %s)", (a, b)
    )
    connection.commit()
    #connection.close()


def agregaRenta(a, b, c):


    cursor.execute(
        "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta) VALUES (%s, %s, %s)", (a, b, c)
    )

def filtraApellidos(cond):
    cursor.execute(
        "SELECT * FROM usuarios WHERE nombre LIKE '% "+cond+"'"
    )



#agregaUsuario("Yo Hernandeez","yo.com")
agregaPelicula("Conjuro","Terror")
#agregaRenta(13,"1",dt.date.today())

cond = input("Ingrese la cadena con la que desea que el apallido del cliente finalice\n")
filtraApellidos(cond)

connection.commit()
connection.close()

def cambiaGenero(nombre_pelicula, nuevo_genero):
    connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM peliculas WHERE nombre = %s", nombre_pelicula
    )
    pelicula = cursor.fetchone()
    print(pelicula)

    if pelicula:
        # La película existe, actualizar su género
        id_pelicula = (pelicula.get('idPelicula'))
        print(type(id_pelicula), id_pelicula)
        print(type(pelicula))
        actualizacion = "UPDATE peliculas SET genero= '"+ nuevo_genero + "' WHERE idPelicula= '" + str(id_pelicula) +"'"
        print(actualizacion)
        #cursor.execute(actualizacion, (str(nuevo_genero), str(id_pelicula)))
        cursor.execute(actualizacion)
        print(f"Se ha actualizado el género de la película '{nombre_pelicula}' a '{nuevo_genero}'.")
    else:
        print(f"No se encontró ninguna película con el nombre '{nombre_pelicula}'.")
    
    connection.commit()
    print(cursor.rowcount, "registros afectado/s")
    #connection.close()

def eliminaRegistros():
    connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    fechaActual = dt.date.today()
    cursor.execute(
        "SELECT * FROM rentar WHERE fecha_renta < '2024-03-%s'", fechaActual-3
    )
    connection.commit()
    connection.close()


cambiaGenero("verde","hombre")
cambiaGenero("Conjuro","hombre")
