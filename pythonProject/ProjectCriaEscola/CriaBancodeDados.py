import mysql.connector

def cria_schema():
  banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
  )

  cursor = banco.cursor()
  comandosql = "Create Schema DBEscola"
  cursor.execute(comandosql)
  dados_lidos = cursor.fetchall()

def cria_table():
  banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="DBEscola"
  )

  cursor = banco.cursor()
  comandosql = '''Create table instrutores (id INT NOT NULL AUTO_INCREMENT,nome VARCHAR(50) NOT NULL,
      email VARCHAR(50) NOT NULL,    valor_hora INTEGER UNSIGNED NULL,
      certificados VARCHAR(255) NULL,    PRIMARY KEY(id)    );'''
  cursor.execute(comandosql)

  comandosql = '''CREATE TABLE cursos (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    requisito VARCHAR(255) NULL,
    carga_horaria SMALLINT UNSIGNED NULL,
    preco DOUBLE UNSIGNED NULL,
    PRIMARY KEY(id)
    ); '''
  cursor.execute(comandosql)

  comandosql = '''CREATE TABLE alunos (
    id INT NOT NULL AUTO_INCREMENT,
    cpf CHAR(11) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    fone CHAR(14) NOT NULL,
    data_nascimento DATE NULL,
    PRIMARY KEY(id)
    ); '''
  cursor.execute(comandosql)

  comandosql = '''CREATE TABLE turmas (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    instrutores_id INT NOT NULL,
    cursos_id INTEGER UNSIGNED NOT NULL,
    data_inicio DATE NULL,
    data_final DATE NULL,
    carga_horaria SMALLINT UNSIGNED NULL,
    PRIMARY KEY(id),
    INDEX turmas_FKIndex1(cursos_id),
    INDEX turmas_FKIndex2(instrutores_id),
    FOREIGN KEY(cursos_id)
    REFERENCES cursos(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY(instrutores_id)
    REFERENCES instrutores(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
     ); '''
  cursor.execute(comandosql)

  comandosql = '''CREATE TABLE matriculas (
     id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
      turmas_id INTEGER UNSIGNED NOT NULL,
      alunos_id INT NOT NULL,
      data_matricula DATE NULL,
      PRIMARY KEY(id),
      INDEX matriculas_FKIndex1(alunos_id),
      INDEX matriculas_FKIndex3(turmas_id),
      FOREIGN KEY(alunos_id)
      REFERENCES alunos(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
      FOREIGN KEY(turmas_id)
      REFERENCES turmas(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
    ); '''
  cursor.execute(comandosql)

def Deleta_schema():
  banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
  )

  cursor = banco.cursor()
  cursor.execute("SHOW DATABASES LIKE 'DBEscola'")
  resultado = cursor.fetchone()

  if resultado:
    print("O banco de dados já existe.")
    comandosql = "Drop database DBEscola"
    cursor.execute(comandosql)
  else:
    print("O banco de dados ainda não existe.")


#Deleta_schema()
#cria_schema()
#cria_table()