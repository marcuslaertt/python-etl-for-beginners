# Beginner-friendly-ETL-project-using-Python-and-relational-databases-SQL-Server-and-Oracle-.
Beginner-friendly ETL project using Python to connect, extract, transform, and load data from relational databases.


## Etapa 1 – Conexão com SQL Server

Nesta etapa é apresentada uma conexão básica entre Python e SQL Server
utilizando a biblioteca pyodbc e autenticação do Windows.

Essa etapa é a base de todo projeto de ETL ou automação de dados,
pois sem a conexão não é possível executar consultas ou manipular dados.


## Etapa 2 – Consulta SELECT em uma tabela

Após realizar a conexão com o SQL Server, nesta etapa é demonstrado
como executar uma consulta SELECT em uma tabela do banco de dados.

O objetivo é entender como o Python envia uma query para o banco,
como os dados são retornados e como podem ser lidos dentro do script.


## Etapa 3 – Mini ETL: Excel para SQL Server

Nesta etapa é demonstrado um exemplo simples de ETL, onde os dados são
lidos de um arquivo Excel, passam por um tratamento básico e são inseridos
em uma tabela do SQL Server.

O objetivo é entender o fluxo essencial do processo de ETL,
sem complexidade desnecessária.   ### Bibliotecas utilizadas

- **pandas**: utilizada para leitura e tratamento de dados em formato de tabela,
como arquivos Excel.
- **pyodbc**: utilizada para realizar a conexão entre o Python e o SQL Server,
permitindo executar consultas e inserir dados no banco.

