#importa a biblioteca que serve para conectar o banco de dados em phyton
import mysql.connector
#executa uma funçao da lib que realiza a conexao
conexao = mysql.connector.connect(
    #parametro de conexao o banco de dados
    host ="localhost",
    user="root",
    password="",
    database = "oficina"
)


print ("conectado")
#funçao cursor da lib
#serve para manipular os dados de envio para o banco 
cursor = conexao.cursor()
#comandos  e valores para envio de dados em sql
sql ="insert into"
sql= "insert into servico(descricao,id_carro)" \
"values(%s,%s)"

values = ("troca de oleo",1)



cursor.execute(sql,values)
conexao.commit()
cursor.execute("select*from funcionarios")
resultado = cursor.fetchall()

for i in resultado:
    print(i)




