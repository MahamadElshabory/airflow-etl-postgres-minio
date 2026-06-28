from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "coder2j",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

def greet(ti):
    first_name = ti.xcom_pull( task_ids="second_task",key = "first_name")
    last_name = ti.xcom_pull(task_ids="second_task",key="last_name")
    age = ti.xcom_pull(task_ids="third_task" , key="age")
    print(f"hello {first_name}, {last_name} and my age is {age}")

def get_name(ti):
    ti.xcom_push(key="first_name" , value="mahamad")
    ti.xcom_push(key="last_name" , value = "elshabory")
    
def get_age(ti) :
    ti.xcom_push(key="age" ,value="23")
    

with DAG(
    dag_id="python_operator_dag_v06",
    default_args=default_args,
    description="this is our first dag with python operator",
    start_date=datetime(2021, 10, 6),
    schedule_interval="@daily",
) as dag:

    task2 = PythonOperator(
        task_id="second_task",
        python_callable=get_name,
    )

    task1 = PythonOperator(
        task_id="first_task",
        python_callable=greet,
        #op_kwargs={"age": 23},
    )
    
    task3 = PythonOperator(
        task_id = "third_task",
        python_callable = get_age
    )

    [task2,task3] >> task1