def GeraCursos():
    from dados import escolha_dados
    import mysql.connector

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="DbEscola"
    )

    dados_curso=escolha_dados("cursos")

    from_db = []

    for x in range(0, len(dados_curso)):
        c = dados_curso[x]
        p = escolha_dados("precocurso")
        dados = (x+1, c, 'curso medio','25',p)
        from_db.append(dados)

    print(from_db)

    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela cursos
    cursor = banco.cursor()
    comandosql = "delete from cursos"
    cursor.execute(comandosql)
    banco.commit()

    # Trabalhando com os dados no Mysql
    # Update direto na tabela cursos
    sqll = '''
            INSERT INTO dbescola.cursos (id, nome, requisito, carga_horaria, preco) 
            VALUES (%s, %s, %s, %s, %s)    
            '''
    cursor.executemany(sqll, from_db)
    banco.commit()
