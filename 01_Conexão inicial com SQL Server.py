"""
ETAPA 1 – Conexão básica com SQL Server usando Python

Este script demonstra como realizar uma conexão simples entre o Python
e um banco de dados SQL Server utilizando a biblioteca pyodbc e
autenticação do Windows (Trusted Connection).

Esta é a primeira etapa de qualquer processo de ETL, automação ou
análise de dados, pois sem conexão não é possível extrair informações.
"""

import pyodbc
import pandas as pd  # Será utilizado nas próximas etapas

# ===============================
# CONFIGURAÇÕES DE CONEXÃO
# ===============================

# Nome do servidor SQL Server (exemplo: NOMEPC\\INSTANCIA)
server = 'exemplo'

# Nome do banco de dados
database = 'exemplo'

# ===============================
# CRIAÇÃO DA CONEXÃO
# ===============================

# Cria a conexão com o banco de dados SQL Server
conexaoDB = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

# ===============================
# CURSOR
# ===============================

# O cursor é responsável por executar comandos SQL no banco
cursor = conexaoDB.cursor()

print("✅ Conexão com o SQL Server realizada com sucesso!")

# ===============================
# ENCERRAMENTO
# ===============================

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conexaoDB.close()
 Para que serve este código?

''' Este código serve para conectar um script Python a um banco de dados SQL Server.

Essa conexão é essencial para:

executar consultas SQL

extrair dados
inserir ou atualizar informações

automatizar processos

construir pipelines de ETL '''