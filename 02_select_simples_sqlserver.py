"""
ETAPA 2 – Executando uma query SELECT em uma tabela

Após realizar a conexão com o SQL Server, este script demonstra,
passo a passo, como executar uma consulta SELECT em uma tabela
e ler os dados retornados.
"""

import pyodbc

# ===============================
# CONEXÃO COM O BANCO
# ===============================

# Nome do servidor SQL Server
server = 'exemplo'

# Nome do banco de dados
database = 'exemplo'

# Cria a conexão com o banco de dados
conexaoDB = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

# O cursor é o objeto responsável por executar comandos SQL
cursor = conexaoDB.cursor()

# ===============================
# CONSULTA SQL
# ===============================

# Query SQL:
# SELECT * → retorna todas as colunas
# FROM vendas → busca os dados da tabela vendas
query = "SELECT * FROM vendas"

# Envia a query para o banco de dados
cursor.execute(query)

# ===============================
# LEITURA DOS RESULTADOS
# ===============================

# fetchall() retorna todas as linhas da consulta
resultados = cursor.fetchall()

# Cada linha representa um registro da tabela
for linha in resultados:
    print(linha)

# ===============================
# ENCERRAMENTO
# ===============================

# Fecha o cursor
cursor.close()

# Fecha a conexão com o banco
conexaoDB.close()

#O que essa etapa ensina?

'''Como executar uma consulta SQL usando Python

Como buscar dados de uma tabela do banco

Como ler os resultados retornados'''

# O que faz SELECT * FROM vendas?

'''SELECT * → seleciona todas as colunas

FROM vendas → indica a tabela de onde os dados serão buscados

Ou seja: traz todos os dados da tabela vendas.'''

 # O que faz cursor.execute()?

'''Envia a query SQL para o banco de dados executar.

Sem esse comando, a consulta não é executada.'''

# O que faz fetchall()?

'''Retorna todas as linhas da consulta.

Cada linha retornada é um registro da tabela.''''


# Por que usamos for linha in resultados?

'''Porque fetchall() devolve uma lista de registros.

O for permite percorrer cada registro individualmente.'''