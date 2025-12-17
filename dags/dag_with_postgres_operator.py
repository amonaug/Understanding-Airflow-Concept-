from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'pedro',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_postgres_operator_v3',
    default_args=default_args,
    start_date=datetime(2025, 12, 17),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql='''
        CREATE TABLE if not exists dag_runs (
            dt date,
            dag_id character varying,
            primary key (dt, dag_id)    
        )
        '''
    )

    task2 = PostgresOperator(
        task_id='insert_dag_run',
        postgres_conn_id='postgres_localhost',
        sql='''
        DELETE FROM dag_runs WHERE dt = '{{ ds }}' and dag_id = '{{ dag.dag_id }}';
        INSERT INTO dag_runs (dt, dag_id)
        VALUES ('{{ ds }}', '{{ dag.dag_id }}');
        '''
    )

    task1 >> task2
