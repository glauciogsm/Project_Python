def GeraClientes(totalreg,data_atual):
    from dados import escolha_dados
    import mysql.connector
    from random import choice

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="workdados"
    )
    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela clientes
    cursor = banco.cursor()
    comandosql = "delete from clientes"
    cursor.execute(comandosql)
    banco.commit()

    from_db = []

    # Retorna uma lista de tuplas
    for x in range(1,totalreg):
        n = escolha_dados("nome")
        s = escolha_dados("sobrenome")
        c = escolha_dados("ceps")
        p = escolha_dados("profissoes")
        dados = (x,n+s,c,p,data_atual,'P')
        from_db.append(dados)

    #Trabalhando com os dados no Mysql
    #Update direto na tabela clientes
    sql = '''
        INSERT INTO workdados.clientes (clientes_id, nome, cep, profissão, data, flag_id) 
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
    cursor.executemany(sql, from_db)
    banco.commit()
