
# creation of TABLE in the database "mydb" 

import mysql.connector
conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',
                              host = 'localhost',database = 'mydb')
qur = 'create table Employee(Name VARCHAR(40),mob VARCHAR(40),dept VARCHAR(40),sal VARCHAR(40))'
mycur = conn.cursor()
mycur.execute(qur)
mycur.close()
conn.close()
