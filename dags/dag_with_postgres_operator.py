from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    "owner": "coder2j",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="our_first_dag_v0077",
    default_args=default_args,
    description="This is our first DAG",
    start_date=datetime(2021, 7, 29, 9),
    schedule_interval="0 3 * * Tue-Fri",
) as dag:

    task1 = PostgresOperator(
        task_id="first_task",
        postgres_conn_id = "postgres_localhost",
        sql = """
            create table if not exists dag_run(
                dt date,
                dag_id character varying,
                primary key (dt,dag_id)
            )
        
        """
        
    )
    
   
    
    task1 