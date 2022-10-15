import pyodbc

create_connection = (
    "Driver={SQL Server};"
    "Server=localhost\SQLEXPRESS;"
    "Database=db_estudos_python;"
)

connect = pyodbc.connect(create_connection)
print('Conexão bem sucedida')

cursor = connect.cursor()

id = 4
nome = 'Stan Lee'
idade = 76
altura = 174
peso = 87
sexo = 'Masculino'

comand = f"""INSERT INTO Usuario( id_user , nome, idade, altura, peso, sexo) 
VALUES 
    ({id}, '{nome}', {idade} , {altura}, {peso}, '{sexo}')"""

cursor.execute(comand)
cursor.commit()
