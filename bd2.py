""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
Desarrollar una clase llamada PaisMySQL que herede de MySQLConnect. Debe
agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
a. insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir
como parámetro las columnas de la tabla y debe retornar True si se inserta el
dato o False en caso contrario.
b. editar(nombre): Método para editar el nombre en la Tabla País. Validar que
nombre no exista en la tabla.
c. eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener
como parámetro la llave primaria, retorna True si logró eliminarse y False en
caso contrario.
d. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de
tuplas con los resultados del filtro de la Tabla País. Ejemplo: “id = 1” ,
“nombre like %A%”

"""

from mysql.connector import connect, Error

class MySQLConnect:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None
    @property
    def host(self):
        return self._host
    @property
    def user(self):
        return self._user
    @property
    def password(self):
        return self._password
    @property
    def database(self):
        return self._database


    @host.setter
    def host(self, value):
        self._host = value
    @user.setter
    def user(self, value):
        self._user = value
    @password.setter
    def password(self, value):
        self._password = value
    @database.setter
    def database(self, value):
        self._database = value

    def conectar(self):
        conexion = connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database)
        return conexion

    def desconectar(self, conexion):
        if conexion:
            conexion.close()
mysql1 = MySQLConnect(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="olimpiadas"
)
conexion = mysql1.conectar()

if conexion:
    print("conexion exitosa")
else:
    print("No conecto")


class PaisMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
    def insertar(self, id, nombre):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            query = "insert into pais (id, nombre) values (%s, %s)"
            cursor.execute(query, (id, nombre))
            conexion.commit()
            print("Se inserto el dato")
            return True
        except Error as x:
            print(f"Error al insertar en la tabla Pais: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)
    def editar(self, id, newname):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            query = "select count(*) from pais where nombre = %s and id != %s"
            cursor.execute(query, (newname, id))
            nombrea = cursor.fetchone()[0]
            if nombrea == 0:
                newquery = "update pais set nombre = %s where id = %s"
                cursor.execute(newquery, (newname, id))
                conexion.commit()
                print("Se edito el dato")
            else:
                print("El nombre ya existe")
        except Error as x:
            print(f"Hubo error al editar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)
    def eliminar(self, id):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            delquery = "delete from pais where id = %s"
            cursor.execute(delquery, (id,))
            conexion.commit()
            print("Se elimino el dato")
        except Error as x:
            print(f"Hubo error al editar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)
    def consultar(self, filter):
        conexion = self.conectar()
        res=[]
        try:
            cursor = conexion.cursor()
            query = f"select * from pais where {filter}"
            cursor.execute(query)
            res = cursor.fetchall()
        except Error as x:
            print(f"Hubo un error al buscar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)
        return res

#PRUEBA INCISO A
pmysql1 = PaisMySQL(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="olimpiadas")
#pmysql1.insertar(300, "Castelvania")
#PRUEBA INCISO B
#pmysql1.editar(300,"Reino Castlevania")
#PRUEBA INCISO C
#pmysql1.eliminar(300)
#PRUEBA INCISO D
#pmysql1.insertar(300, "Castelvania")
#res = pmysql1.consultar("id=300")
#print(res)
