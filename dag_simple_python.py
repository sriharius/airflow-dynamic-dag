
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

def dummy_python_callable(**kwargs):
    print('File Path - ', kwargs['file_path'])


with DAG(
    dag_id="Simple_Python",
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=None,
    default_args={
        'depends_on_past': False,
        'email': "sample@airflow.com",
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 1,
        'retry_delay': timedelta(minutes=3)
    }
) as dag:
    t1 = PythonOperator(
        task_id = "task_1",
        python_callable=dummy_python_callable,
        op_kwargs={ 'file_path': "/tmp/check/dummy_file.txt" }
    )