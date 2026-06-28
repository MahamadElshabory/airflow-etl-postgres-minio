# Dockerized Apache Airflow ETL Pipeline

This project demonstrates a local data engineering pipeline using Apache Airflow, PostgreSQL, MinIO/S3, and Docker.

## Project Overview

The pipeline extracts daily order data from PostgreSQL, writes the result into a temporary CSV/text file, and uploads it to a MinIO bucket using Airflow hooks. The project also includes examples of Airflow scheduling, PythonOperator, BashOperator, XCom, TaskFlow API, PostgreSQL Operator, S3 Sensor, retries, and dependency management.

## Tech Stack

- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- MinIO/S3
- Python
- Airflow Hooks, Operators, and Sensors

## Main Features

- Dockerized Airflow environment
- PostgreSQL integration using PostgresHook
- MinIO/S3 integration using S3Hook
- S3KeySensor to wait for files
- Daily DAG scheduling
- Retry handling and logging
- XCom example using PythonOperator
- TaskFlow API example
- Custom Airflow image with Python dependencies

## Main Pipeline

1. Airflow connects to PostgreSQL.
2. It extracts orders for a specific execution date.
3. The data is written to a temporary file.
4. The file is uploaded to MinIO/S3 under the `orders/` folder.
5. The output can be checked from the MinIO console.

## How to Run

```bash
docker compose up -d --build


## Required Airflow Connections

Create these connections from:

Airflow UI → Admin → Connections

### 1. PostgreSQL Connection

| Field | Value |
|---|---|
| Conn Id | postgres_localhost |
| Conn Type | Postgres |
| Host | postgres |
| Schema | airflow |
| Login | airflow |
| Password | airflow |
| Port | 5432 |

Note: DBeaver connects from the host machine using `localhost:5433`, but Airflow containers connect using `postgres:5432`.

### 2. MinIO / S3 Connection

| Field | Value |
|---|---|
| Conn Id | minio_conn |
| Conn Type | Amazon Web Services |

Extra:

```json
{
  "aws_access_key_id": "AKIAIOSFODNN7EXAMPLE",
  "aws_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "host": "http://host.docker.internal:9000"
}