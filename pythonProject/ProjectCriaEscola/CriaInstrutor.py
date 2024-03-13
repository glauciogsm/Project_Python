def GeraInstrutor():
    from dados import escolha_dados
    import mysql.connector

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="DbEscola"
    )
    from_db = []
    dados_instrutor = escolha_dados("nomeinstrutor")
    print(dados_instrutor)

    for x in range(0, len(dados_instrutor)):
        i = dados_instrutor[x]
        s = escolha_dados("sobrenome")
        e = i+s+escolha_dados("email")
        v = escolha_dados("horainstrutor")
        c = escolha_dados("certificados")
        ee = e.lower()
        dados = (x+1,i+s,ee.replace(" ", ""),v,c)
        from_db.append(dados)

    print(from_db)

    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela instrutor
    cursor = banco.cursor()
    comandosql = "delete from instrutores"
    cursor.execute(comandosql)
    banco.commit()

    # Trabalhando com os dados no Mysql
    # Update direto na tabela instrutores
    sqll = '''
            INSERT INTO DbEscola.instrutores (id, nome, email, valor_hora, certificados) 
            VALUES (%s, %s, %s, %s, %s)    
            '''
    cursor.executemany(sqll, from_db)
    banco.commit()
