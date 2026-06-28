from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "coder2j",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="our_first_dag_v5",
    default_args=default_args,
    description="This is our first DAG",
    start_date=datetime(2021, 7, 29, 9),
    schedule_interval="@daily",
) as dag:

    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello",
    )
    
    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "second one yeah"
    )
    
    
    task3 = BashOperator(
        task_id = "third_task",
        bash_command = "the third one hereee"
    )
    
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
   
    # task1 >> task2
    # task1 >> task3   
    
    task1 >> [task2,task3]