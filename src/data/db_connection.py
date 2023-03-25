""" Database connection functions and variables """

import logging
import boto3
from mypy_boto3_dynamodb.service_resource import Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.configuration import (
    AURORA_DB_CLUSTER_ARN,
    AURORA_DB_NAME,
    AURORA_DB_SECRET_ARN,
    CALCULATOR_TABLE,
    DEBUG,
    SERVERLESS_SIMULATE,
)

# Set logging level
if DEBUG is True:
    logging.basicConfig()
    logging.getLogger("aurora_data_api").setLevel(logging.DEBUG)

# Set Relational Database URL
database_url = f"postgresql+auroradataapi://:@/{AURORA_DB_NAME}"


# Define SQLALchemy engine, Session, and Base
engine = create_engine(
    database_url,
    echo=True,
    connect_args={
        "aurora_cluster_arn": AURORA_DB_CLUSTER_ARN,
        "secret_arn": AURORA_DB_SECRET_ARN,
    },
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_session():
    """
    Returns the SQLALchemy session object.
    """
    return Session()


def create_db():
    """
    Creates database if it does not exist.
    """
    logging.info('Creating DB')

    rds_client = boto3.client("rds-data")
    db_exists = False

    # Check if DB database_exists
    sql = "SELECT datname FROM pg_database WHERE datistemplate = false"
    response = rds_client.execute_statement(
        resourceArn=AURORA_DB_CLUSTER_ARN,
        secretArn=AURORA_DB_SECRET_ARN,
        database="postgres",
        sql=sql,
    )

    for record in response["records"]:
        if record[0]["stringValue"] == AURORA_DB_NAME:
            db_exists = True
            logging.error('Database already exists.')

    # Create Database
    if not db_exists:
        logging.error('Database not found, creating it.')
        sql = "CREATE DATABASE " + AURORA_DB_NAME
        response = rds_client.execute_statement(
            resourceArn=AURORA_DB_CLUSTER_ARN,
            secretArn=AURORA_DB_SECRET_ARN,
            database="postgres",
            sql=sql,
        )


config = {}


def get_table() -> Table:
    """
    Returns a DynamoDB table object using the above configuration

    :return Table: DynamoDB table object
    """

    if SERVERLESS_SIMULATE:
        logging.info('SERVERLESS_SIMULATE:  %s', SERVERLESS_SIMULATE)

        config['endpoint_url'] = "http://host.docker.internal:8000"
        config['aws_access_key_id'] = ''
        config['aws_secret_access_key'] = ''

    logging.info(str(config))

    dynamodb = boto3.resource("dynamodb", **config)

    logging.info('dynamodb=%s', str(dynamodb))

    return dynamodb.Table(CALCULATOR_TABLE)
