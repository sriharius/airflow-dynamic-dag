
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="Simple_Bash",
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
    t1 = BashOperator(
        task_id = "task_1",
        bash_command="echo at task 1"
    )

    t2 = BashOperator(
        task_id = "task_2",
        bash_command="echo at task 2"
    )

t1 >> t2