import logging
import azure.functions as func
import requests
import os
#importar a biblioteca do banco de dados
import pyodbc

app = func.FunctionApp()


@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger1(myTimer: func.TimerRequest) -> None:

   #pegando o valor das variáveis
    usuario = os.getenv("USER")
    senha = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    banco_de_dados = os.getenv("DATABASE")

    #printar as variáveis
    logging.info(f"Usuario: {usuario}")
    logging.info(f"Senha: {senha}")
    logging.info(f"Host: {host}")
    logging.info(f"Banco de dados: {banco_de_dados}")


    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado(myTimer: func.TimerRequest) -> None:
    
    #capturar as variáveis de ambiente
    host_sql = os.getenv("HOST")
    database_sql = os.getenv("DATABASE")
    user_sql = os.getenv("USER")
    password_sql = os.getenv("PASSWORD")

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={host};"
        f"DATABASE={banco_de_dados};"
        f"UID={usuario};"
        f"PWD={senha};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
    )

    try:
        conexao = pyodbc.connect(connection_string)
        cursor = conexao.cursor()
        
        query = "SELECT * FROM chamado"

        cursor.execute(query)

        retorno = cursor.fetchall()

        logging.info(retorno)
        
        cursor.close()
        conexao.close()
    except Exception as e:
        print(f"Erro ao conectar: {e}")