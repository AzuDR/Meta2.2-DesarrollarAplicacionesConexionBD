""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
Desarrollar una clase llamada OlimpiadaMySQL que herede de MySQLConnect.
Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
a. insertar(id, year): Método para insertar datos en la Tabla Olimpiada, debe
recibir como parámetro las columnas de la tabla y debe retornar True si se
inserta el dato o False en caso contrario.
b. editar(year): Método para editar el año en la Tabla Olimpiada. Validar que el
año no exista en la tabla.
c. eliminar(id): Método para eliminar un elemento de la Tabla Olimpiada. Debe
tener como parámetro la llave primaria, retorna True si logró eliminarse y
False en caso contrario.
d. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de
tuplas con los resultados del filtro de la Tabla Olimpiada. Ejemplo: “id = 1” ,
“year > 1990”

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


class OlimpiadaMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            query = "insert into olimpiada (id, year_olimpiada) values (%s, %s)"
            cursor.execute(query, (id, year))
            conexion.commit()
            print("Operacion exitosa")
            return True
        except Error as x:
            print(f"Hubo un error al insertar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)

    def editar(self, id, newyear):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            veriquery = "select count(*) from olimpiada where year_olimpiada = %s and id != %s"
            cursor.execute(veriquery, (newyear, id))
            yeara = cursor.fetchone()[0]
            if yeara == 0:
                newquery = "update olimpiada set year_olimpiada = %s where id = %s"
                cursor.execute(newquery, (newyear, id))
                conexion.commit()
                print("Operacion exitosa")
            else:
                print("Ya existe el año")
        except Error as x:
            print(f"Hubo un error al editar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)

    def eliminar(self, id):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            delquery = "delete from olimpiada where id = %s"
            cursor.execute(delquery, (id,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Operacion exitosa")
                return True
            else:
                print("Elemento no encontrado")
        except Error as x:
            print(f"Hubo un error al eliminar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)

    def consultar(self, filter):
        conexion = self.conectar()
        res=[]
        try:
            cursor = conexion.cursor()
            query = f"select * from olimpiada where {filter}"
            cursor.execute(query)
            res = cursor.fetchall()
        except Error as x:
            print(f"Hubo un error al buscar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)
        return res
pmysql1 = OlimpiadaMySQL(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="olimpiadas")
#pmysql1.insertar(4000, 2018)
#PRUEBA INCISO B
#pmysql1.editar(4000,2020)
#PRUEBA INCISO C
#pmysql1.eliminar(4000)
#PRUEBA INCISO D
#pmysql1.insertar(4000, 2018)
#res = pmysql1.consultar("id=4000")
#print(res)
