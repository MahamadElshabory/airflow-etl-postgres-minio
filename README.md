# Airflow ETL Pipeline: PostgreSQL ↔ MinIO/S3
## Overview

This project automates a common data engineering task: moving data out of an operational database and into object storage on a schedule, reliably and with visibility into failures. Rather than a one-off script, it's built as a proper Airflow DAG — meaning the pipeline has defined dependencies between steps, automatic retries if a step fails, and centralized logging so you can see exactly what happened and when.

The underlying pattern — extract, transform, load, with orchestration handling scheduling and failure recovery — is the same one used to automate things far beyond this specific pipeline: nightly data warehouse syncs, scheduled report generation, or even automated model retraining jobs. I built this specifically to understand DAG design, task dependencies, and Airflow's Hooks/Sensors for connecting to external systems (PostgreSQL and MinIO/S3) rather than just moving data with a plain script.

Everything runs in Docker Compose — Airflow, PostgreSQL, and MinIO — so the whole pipeline can be spun up identically on any machine.


## What it does
Extracts data from PostgreSQL on a schedule
Transforms/validates it in a Python task
Loads the result into MinIO/S3 as object storage
Uses Airflow Sensors to wait on upstream conditions before running downstream tasks
Fully Dockerized — Airflow, PostgreSQL, and MinIO all run via Docker Compose


## Tech Stack

Apache Airflow PostgreSQL MinIO/S3 Docker Compose Python TaskFlow API


## Architecture
PostgreSQL --[Extract Task]--> Transform Task --[Load Task]--> MinIO/S3
                     ↑
        Airflow DAG orchestrates scheduling, retries, and logging across all tasks

        
## Run locally
bash
docker-compose up --build

Airflow UI available at localhost:8080.


## Possible next steps
Add data quality checks as a dedicated Airflow task
Add alerting on task failure (e.g. Slack/email on DAG failure)
Parameterize the DAG for multiple source tables
