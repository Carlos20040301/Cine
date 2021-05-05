
import mysql.connector
class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_cine")
        return connection
    def insert_db(self, sala, butakas, boletos, precio):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_taquilla(SALA, BUTAKAS, BOLETOS, PRECIO) VALUES (%s,%s,%s,%s)"
        data = (sala, butakas, boletos, precio)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()
