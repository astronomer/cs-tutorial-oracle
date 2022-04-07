from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.oracle.operators.oracle import OracleOperator,OracleStoredProcedureOperator
from airflow.version import version
from datetime import datetime, timedelta



# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG('oracle_dag',
         start_date=datetime(2019, 1, 1),
         max_active_runs=3,
         schedule_interval=None,
         default_args = default_args,
         catchup = False,
        template_searchpath='/usr/local/airflow/include/sql'

         ) as dag:

    t0 = OracleOperator(
        task_id='ddl',
        sql='ddl.sql',
        oracle_conn_id='my_oracle_conn'

    )

    t1 = OracleOperator(
        task_id='insert',
        sql='insert.sql',
        oracle_conn_id='my_oracle_conn'

    )

    t2 = OracleStoredProcedureOperator(task_id='call_procedure',
                                       oracle_conn_id='my_oracle_conn',
                                       procedure='remove_prod',
                                       parameters={'product_id':1})




    t0 >> t1  >> t2