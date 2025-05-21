import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psg54321',
    database='bdyouutube',
)
cursor = conexao.cursor()

cursor.close()

#crud
comando = 'INSERT INTO vendas (nome_produto, valor)'
cursor.execute(comando)
conexao.commit()
resultado = cursor.fetchall()

conexao.close()
