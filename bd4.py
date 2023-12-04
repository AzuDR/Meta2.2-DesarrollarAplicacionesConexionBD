"""
Azucena Dominguez Romero 951
17 de Octubre de 2023
Desarrollar una clase llamada ResultadosMySQL que herede de MySQLConnect.
Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
a. insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para
insertar datos en la Tabla Resultados, debe recibir como parámetro las
columnas de la tabla y debe retornar True si se inserta el dato o False en
caso contrario.
b. editar(oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla
Resultados. Validar que sean valores enteros positivos.
c. eliminar(idOlimpiada, idPais, idGenero): Método para eliminar un elemento
de la Tabla Resultados. Debe tener como parámetro la llave primaria
compuesta, retorna True si logró eliminarse y False en caso contrario.
d. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de
tuplas con los resultados del filtro de la Tabla Resultados. Ejemplo: “idPais =
1” , “idPais = 1 and idOlimpiada=2

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


class ResultadosMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            query = "insert into resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) values (%s, %s,%s, %s,%s, %s)"
            cursor.execute(query, (idOlimpiada, idPais, idGenero, oro, plata, bronce))
            conexion.commit()
            print("Insercion correcta")
            return True
        except Error as x:
            print(f"Hubo un error al insertar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)

    def editar(self, idOlimpiada, idPais, idGenero, neworo, newplata, newbronce):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            if neworo > 0 and newplata > 0 and newbronce > 0:
                    newquery = "update resultados set oro = %s, plata = %s, bronce = %s where idOlimpiada = %s and idPais = %s and idGenero = %s"
                    cursor.execute(newquery, (neworo, newplata, newbronce, idOlimpiada, idPais, idGenero))
                    conexion.commit()
                    print("Edicion correcta")
            else:
                print("Ingresa los valores enteros positivos")
        except Error as x:
            print(f"Hubo un error al editar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)

    def eliminar(self, idOlimpiada, idPais, idGenero):
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            delquery = "delete from resultados where idOlimpiada = %s and idPais = %s and idGenero = %s"
            cursor.execute(delquery, (idOlimpiada, idPais, idGenero))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Eliminacion correcta")
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
            query = f"select * from resultados where {filter}"
            cursor.execute(query)
            res = cursor.fetchall()
        except Error as x:
            print(f"Hubo un error al buscar: {x}")
        finally:
            if cursor:
                cursor.close()
            self.desconectar(conexion)
        return res
pmysql1 = ResultadosMySQL(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="olimpiadas")
#PRUEBA INCISO A
#pmysql1.insertar(1,1,1,3,2,1)
#PRUEBA INCISO B
#pmysql1.editar(1,1,1,4,5,6)
#PRUEBA INCISO C
#pmysql1.eliminar(1,1,1)
#PRUEBA INCISO D
#pmysql1.insertar(1,1,1,3,2,1)
#res = pmysql1.consultar("idOlimpiada=1")
