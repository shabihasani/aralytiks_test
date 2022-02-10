from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.email import EmailOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
import pandas as pd
from airflow.operators.python_operator import PythonOperator
import os
from sqlalchemy import types, create_engine
import pandas as pd


from datetime import datetime, timedelta
import csv
import requests
import json

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

def testMethod1(**context):
    for files in os.listdir('opt/airflow/dags/files/'):
         tabela = pd.read_csv('opt/airflow/dags/files/' + files, sep=None, engine="python")
    dtyp = {c: types.VARCHAR(tabela[c].str.len().max())
            for c in tabela.columns[tabela.dtypes == 'object'].tolist()}

    tabela = tabela.apply(lambda col: pd.to_datetime(col, errors="ignore")
    if col.dtypes == object
    else col,
    axis=0)

    print('Shabi')

def testMethod2(**context):
    print('Hasani')

with DAG("shabiPrint", start_date=datetime(2021, 1 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:


    task1 = PythonOperator(task_id = "Task1", python_callable=testMethod1)

    task2 = PythonOperator(task_id = "Task2", python_callable=testMethod2)

    task1 >> task2

   
    
