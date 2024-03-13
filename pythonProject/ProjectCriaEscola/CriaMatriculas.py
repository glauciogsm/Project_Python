def GeraMatriculas(totMatricula):
    from random import randint
    from datetime import date
    import mysql.connector

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="dbescola"
    )

    cursor = banco.cursor()
    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela matriculas
    comandosql = "delete from matriculas"
    cursor.execute(comandosql)
    banco.commit()

    # ver o total de alunos
    comandosql = "Select * from alunos"
    cursor.execute(comandosql)
    dados_lidos = cursor.fetchall()
    totaluno = len(dados_lidos)
    # ver o total de turmas
    comandosql = "Select * from turmas"
    cursor.execute(comandosql)
    dados_lidos = cursor.fetchall()
    toturmas = len(dados_lidos)

    from_db = []

    # Retorna uma lista de tuplas
    for x in range(1, totMatricula):
        t = randint(1,toturmas)
        a = randint(1,totaluno)
        d = date.today()
        dados = (x,t,a,d)
        from_db.append(dados)

    #Trabalhando com os dados no Mysql
    #Update direto na tabela matriculas
    sql = '''
        INSERT INTO dbescola.matriculas (id, turmas_id, alunos_id, data_matricula) 
        VALUES (%s, %s, %s, %s)
        '''

    cursor.executemany(sql, from_db)
    banco.commit()
