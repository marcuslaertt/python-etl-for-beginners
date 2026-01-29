✅ Antes da Etapa 3: o que você precisa preparar no SQL Server

'''Para o script do Mini ETL (Excel → SQL Server) funcionar, o SQL Server precisa ter um lugar para receber os dados. Isso significa:

Ter o SQL Server instalado e rodando

Criar um banco de dados (ex: Python)

Criar uma tabela (ex: vendas) com as colunas corretas

Preparar o arquivo Excel com o mesmo padrão de colunas''''

📌 Onde fazer isso?

#Você pode fazer pelo SSMS (SQL Server Management Studio) ou por qualquer ferramenta que rode SQL.

✅ Comando para criar o banco:
CREATE DATABASE Python;


'''Depois disso, seu banco Python vai existir e você poderá conectar nele.'''

#2) Criar a tabela que vai receber os dados do Excel

Seu Excel precisa ter colunas (exemplo):

'''data_venda
produto
quantidade
valor

Então sua tabela no SQL Server deve ter as mesmas colunas (mesmo nome, e tipo compatível).'''


#Exemplo de criação da tabela:
USE Python;

CREATE TABLE vendas (
    data_venda DATE,
    produto VARCHAR(100),
    quantidade INT,
    valor DECIMAL(10,2)
);
#Por que isso é importante?

Porque o script pega os nomes das colunas do Excel e monta o INSERT assim:

INSERT INTO vendas (data_venda, produto, quantidade, valor)
VALUES (?, ?, ?, ?)
        
        ✅ O Excel deve ter:

Primeira linha = cabeçalho

Colunas com nomes iguais aos da tabela

Dados válidos (ex: números em quantidade, valor em decimal)

Exemplo de colunas no Excel:

data_venda	produto	quantidade	valor
2026-01-01	Arroz	2	15.90
2026-01-02	Feijão	1	8.50

"""
ETAPA 3 – Mini ETL simples: Excel para SQL Server

Objetivo:
Ler um arquivo Excel e inserir os dados em uma tabela do SQL Server.
"""

import pandas as pd '''pandas é uma biblioteca do Python usada para trabalhar com dados em formato de tabela, como:
Excel (.xlsx)
CSV
tabelas de banco de dados'''
import pyodbc '''pyodbc é uma biblioteca do Python que permite conectar o Python a bancos de dados usando ODBC.'''

# -------------------------------
# 1) LER O ARQUIVO EXCEL
# -------------------------------

caminho_excel = "dados/vendas.xlsx"

df = pd.read_excel(caminho_excel)

print("Excel lido com sucesso!")
print(df.head())

# -------------------------------
# 2) TRATAR OS DADOS
# -------------------------------

# Remove linhas vazias
df = df.dropna()

# -------------------------------
# 3) CONECTAR NO SQL SERVER
# -------------------------------

server = "exemplo"
database = "exemplo"

conexao = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

cursor = conexao.cursor()

print("Conectado ao SQL Server!")

# -------------------------------
# 4) INSERIR OS DADOS
# -------------------------------

query = """
INSERT INTO vendas (data_venda, produto, quantidade, valor)
VALUES (?, ?, ?, ?)
"""

for linha in df.itertuples(index=False, name=None):
    cursor.execute(query, linha)

conexao.commit()

print("Dados inseridos com sucesso!")

# -------------------------------
# 5) FECHAR CONEXÕES
# -------------------------------

cursor.close()
conexao.close()
