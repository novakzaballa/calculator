""" App level Configuration Variables """

import os

from dotenv import load_dotenv

# Disable validation for debugging
DEBUG = False

# Environment variables
SERVERLESS_SIMULATE = os.environ.get('SERVERLESS_SIMULATE')
CALCULATOR_TABLE = os.environ.get('CALCULATOR_TABLE')
AURORA_DB_NAME = os.environ.get('AURORA_DB_NAME')
if SERVERLESS_SIMULATE:
    if 'AURORA_DB_CLUSTER_ARN' in os.environ:
        del os.environ['AURORA_DB_CLUSTER_ARN']
    if 'AURORA_DB_ENDPOINT' in os.environ:
        del os.environ['AURORA_DB_ENDPOINT']
    if 'AURORA_DB_SECRET_ARN' in os.environ:
        del os.environ['AURORA_DB_SECRET_ARN']

# Load configuration env variables from .env file at root folder
load_dotenv()
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
AURORA_DB_CLUSTER_ARN = os.environ.get("AURORA_DB_CLUSTER_ARN")
AURORA_DB_ENDPOINT = os.environ.get("AURORA_DB_ENDPOINT")
AURORA_DB_SECRET_ARN = os.environ.get("AURORA_DB_SECRET_ARN")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
LOCAL_DB_USER=os.environ.get("LOCAL_DB_USER")
LOCAL_DB_PASSWORD=os.environ.get("LOCAL_DB_PASSWORD")
