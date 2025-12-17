# Airflow Study Project

This project contains a collection of Apache Airflow DAGs created to explore various features and best practices.

## DAGs Overview

The `dags/` directory contains the following examples:

- **`our_first_dag.py`**
  A generic introductory DAG demonstrating the basic structure of an Airflow pipeline and usage of the `BashOperator`.

- **`create_dag_wirh_python_operator.py`**
  Demonstrates how to use the `PythonOperator`. It covers:
  - Defining Python callables.
  - Using XComs to push and pull data between tasks.
  - passing arguments (and resolving issues with missing arguments).

- **`dag_with_taskflow_api.py`**
  Showcases the modern TaskFlow API introduced in Airflow 2.0.
  - Uses decorators like `@dag` and `@task`.
  - Simplifies data passing and dependencies.
  - Demonstrates `multiple_outputs=True` for returning dictionaries.

- **`dag_with_catchup_and_backfill.py`**
  Explores scheduling concepts:
  - `catchup=False` to prevent running past non-triggered DAG runs.
  - Backfilling historical data using the CLI (`airflow dags backfill`).

- **`dag_with_cron_expression.py`**
  Examples of using standard Cron expressions for defining custom schedules (e.g., specific days of the week or times).

- **`dag_with_postgres_operator.py`**
  Demonstrates interaction with a PostgreSQL database using the `PostgresOperator`.
  - Usage of `postgres_conn_id` to specify connection.
  - Creating tables (`CREATE TABLE`).
  - Running idempotent SQL commands (DELETE existing rows before INSERT) to ensure safe retries.

## Usage

This project is designed to run in a Dockerized Airflow environment.
Top-level commands are run via `docker exec`, for example:

```bash
docker exec -it <container_id> airflow dags list
```
