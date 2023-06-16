# creation of db named "mydb"

import mysql.connector     
conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',host = 'localhost')
qur = 'create database mydb'
mycur = conn.cursor()
mycur.execute(qur)
mycur.close()
conn.close()
