def GeraCompras(totalreg):
    from datetime import datetime
    import mysql.connector
    from random import choice , randint

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="workdados"
    )

    cursor = banco.cursor()
    #ver o numero de registros da tabela cliente
    comandosql = "Select * from clientes"
    cursor.execute(comandosql)
    dados_lidos = cursor.fetchall()
    totcli = len(dados_lidos)

    #ver o numero de registros da tabela lojas
    comandosql = "Select * from lojas"
    cursor.execute(comandosql)
    dados_lidos = cursor.fetchall()
    totloja = len(dados_lidos)

    print(totcli)
    print(totloja)

    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela compras
    comandosql = "delete from compras"
    cursor.execute(comandosql)
    banco.commit()

    from_db = []

    # Retorna uma lista de tuplas
    for x in range(1,totalreg):
        c = randint(1,totcli)
        l = randint(1,totloja)
        v = randint(1,9999)
        m = randint(1,12) #gera o mes aleatoria
        if (m == 1 or m == 3 or m == 5 or  m == 7 or m == 8 or m == 10 or m == 12):
            d = randint(1,31)
        elif (m == 2):
            d = randint(1, 28)
        else:
            d = randint(1, 30)
        str_date = (2024, m, d)
        data_str = (f'2024-{m}-{d}')
        data_datetime = datetime.strptime(data_str, "%Y-%m-%d").date()
        data_atual = data_datetime
        if v>5:
            v = round(v/3,2)
        dados = (x,c,l,data_atual,v,'P')
        from_db.append(dados)

    print(from_db)

    #Trabalhando com os dados no Mysql
    #Update direto na tabela compras
    sql = '''
        INSERT INTO workdados.compras (compras_id, cliente_id, loja_id, data_compra, valor, flag_id) 
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

    cursor.executemany(sql, from_db)
    banco.commit()
