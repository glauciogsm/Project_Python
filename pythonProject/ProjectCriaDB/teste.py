import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
  )

cursor = banco.cursor()
cursor.execute("SHOW DATABASES LIKE 'workdados'")
resultado = cursor.fetchone()

if resultado:
    print("O banco de dados já existe.")
else:
    print("O banco de dados ainda não existe.")


