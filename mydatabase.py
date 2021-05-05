import mysql.connector

class RedSocialDb:
    def open_conecction():
        connection=mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="",
                                           database="db_red_social")
        return connection

    def insert_db(self,email,pwd,age):
        my_connection=self.open_connection()
        cursor=my_connection.cursor()
        query="INSERT INTO tbl_usuario(CORREO,PWD,EDAD) VALUES (%s,%s,%s)"
        data=(email,pwd,age)
        cursor.execute(query,data)
        my_connection.commit()
        my_connection.close()
