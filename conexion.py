import mysql.connector

class Conexion:

 HOST = 'localhost'
 USER = 'root'
 PASSWORD = 'admin'
 DATABASE = 'logitrans'
 PORT = '3306'
 pool = None
 POOL_SIZE = 5
 POOL_NAME = 'zona_fit_pool'

 @classmethod
 def obtener_conexion(cls):
     mysql.connector.connect( host=cls.HOST,
                                          user=cls.USER,
                                          password=cls.PASSWORD,
                                          port=cls.PORT,
                                          database=cls.DATABASE)
     return cls.obtener_conexion().get_connection()

 @classmethod
 def liberar_conexion(cls, conexion):
   conexion.close()


if __name__ == "__main__":
 conexion1 = Conexion.obtener_conexion()
 Conexion.liberar_conexion(conexion1)
 conexion2 = Conexion.obtener_conexion()