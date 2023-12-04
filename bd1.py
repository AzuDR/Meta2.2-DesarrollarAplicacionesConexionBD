""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user,
password, database. Debe crear sus métodos set y get (property, setters).
Debe tener los siguientes métodos:
conectar() : Debe conectarse a la base de datos usando los atributos, debe
retornar el objeto de conexión.
desconectar(): Debe desconectar la base de datos. No debe retornar nada.
Investigar método close().

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