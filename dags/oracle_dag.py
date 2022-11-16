"""
### Stored Procedures with Oracle

Example that shows how to load data into Oracle and run stored procedures from it.
Uses the prebuilt Oracle Operator.

Relevant SQL can be found in the `include` folder. 
"""

from airflow import DAG
from airflow.providers.oracle.operators.oracle import (
    OracleOperator,
    OracleStoredProcedureOperator,
)
from pendulum import datetime


my_oracle_conn = "my_oracle_conn"
with DAG(
    "oracle_dag",
    start_date=datetime(2019, 1, 1),
    max_active_runs=3,
    schedule_interval=None,
    default_args={"oracle_conn_id": my_oracle_conn},
    catchup=False,
    doc_md=__doc__,
    template_searchpath="/usr/local/airflow/include/sql",
) as dag:

    ddl = OracleOperator(
        task_id="ddl",
        sql="ddl.sql",
    )

    insert = OracleOperator(
        task_id="insert",
        sql="insert.sql",
    )

    call_procedure = OracleStoredProcedureOperator(
        task_id="call_procedure",
        procedure="remove_prod",
        parameters={"product_id": 1},
    )

    ddl >> insert >> call_procedure
