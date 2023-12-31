from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def helloWorld():
    print("sa from github")

with DAG(dag_id="hello from airflowtest2 new commit auto",
         start_date=datetime(2021, 1, 1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    task2 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld)


task2