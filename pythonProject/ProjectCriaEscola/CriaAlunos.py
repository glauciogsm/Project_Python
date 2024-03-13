def GeraAlunos(totalunos):
    from dados import escolha_dados
    from datetime import date, timedelta
    import mysql.connector
    from random import randint

    banco = mysql.connector.connect(
       host="localhost",
       user= "root",
       passwd="",
       database="DbEscola"
    )

    from_db = []
    current_date = date.today()

    for x in range(0, totalunos):
        f = randint(1,99999999999)
        o = str('849')+str(randint(1,99999999))
        h = 6000 + randint(1, 5000)
        d= current_date - timedelta(h)
        n = escolha_dados("nomealuno")
        s = escolha_dados("sobrenome")
        m = escolha_dados("email")
        e = n + s + m
        ee = e.lower()
        dados = (x+1,f,n+s,ee.replace(" ", ""),o,d)
        from_db.append(dados)

   # print(from_db)

    # Percorrer os resultados e inseri-los à lista
    # deletando os dados da tabela alunos
    cursor = banco.cursor()
    comandosql = "delete from alunos"
    cursor.execute(comandosql)
    banco.commit()

    # Trabalhando com os dados no Mysql
    # Update direto na tabela alunos
    sqll = '''
            INSERT INTO DbEscola.alunos (id, cpf, nome, email, fone, data_nascimento) 
            VALUES (%s, %s, %s, %s, %s, %s)    
            '''
    cursor.executemany(sqll, from_db)
    banco.commit()
