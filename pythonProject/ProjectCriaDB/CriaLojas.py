def GeraLojas():
    from dados import escolha_dados
    import mysql.connector
    from random import choice

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="workdados"
    )

    dados_Lojas=escolha_dados("lojas")

    from_db = []

    for x in range(0, len(dados_Lojas)):
        l = dados_Lojas[x]
        dados = (x+1, l, 'P')
        from_db.append(dados)

    print(from_db)

    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela clientes
    cursor = banco.cursor()
    comandosql = "delete from Lojas"
    cursor.execute(comandosql)
    banco.commit()

    # Trabalhando com os dados no Mysql
    # Update direto na tabela clientes
    sqll = '''
            INSERT INTO workdados.lojas (lojas_id, lojas, flag_id) 
            VALUES (%s, %s, %s)    
            '''
    cursor.executemany(sqll, from_db)
    banco.commit()
