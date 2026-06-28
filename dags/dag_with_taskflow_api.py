from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    "owner": "coder2j",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="python_operator_dag_v07",
    default_args=default_args,
    description="this is our first DAG with TaskFlow API",
    start_date=datetime(2021, 10, 6),
    schedule_interval="@daily",
    catchup=False,
)
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            "first_name": "mohamed",
            "last_name": "hany",
        }

    @task()
    def get_age():
        return 23

    @task()
    def greet(first_name, last_name, age):
        print(f"hello my name is {first_name} {last_name} and my age is {age}")

    name = get_name()
    age = get_age()

    greet(
        first_name=name["first_name"],
        last_name=name["last_name"],
        age=age,
    )

greet_dag = hello_world_etl()