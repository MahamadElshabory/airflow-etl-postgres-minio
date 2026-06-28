from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "coder2j",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="our_first_dag_v0005",
    default_args=default_args,
    description="This is our first DAG",
    start_date=datetime(2021, 7, 29, 9),
    schedule_interval="0 3 * * Tue-Fri",
) as dag:

    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello",
    )
    
   
    
    task1 