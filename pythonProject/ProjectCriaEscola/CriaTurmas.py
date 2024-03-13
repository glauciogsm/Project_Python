def GeraTurmas(data_hj):
    from dados import escolha_dados
    from datetime import date, timedelta
    import mysql.connector

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="dbescola"
    )

    cursor = banco.cursor()
    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela turmas
    comandosql = "delete from turmas"
    cursor.execute(comandosql)
    banco.commit()

    from_db = []

    dados_curso = escolha_dados("cursos")
    dh = date.today()
    td = timedelta(7)
    di=(dh + td)
    df=(di + td)

    from_db = []
    print(di)
    print(df)
    # Retorna uma lista de tuplas
    for x in range(1, len(dados_curso)):
        i = x
        c = x
        dados = (x,i,c,di,df,'30')
        from_db.append(dados)

    #print(from_db)

    #Trabalhando com os dados no Mysql
    #Update direto na tabela turmas
    sql = '''
        INSERT INTO dbescola.turmas (id, instrutores_id, cursos_id, data_inicio, data_final, carga_horaria) 
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

    cursor.executemany(sql, from_db)
    banco.commit()
