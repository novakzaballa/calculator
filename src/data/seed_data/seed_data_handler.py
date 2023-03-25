"""A dummy docstring."""

import json
import os
import boto3

dynamodb = boto3.client('dynamodb')
CALCULATOR_TABLE = os.environ.get('CALCULATOR_TABLE')

def initialize_seed_data():
    """Initialize seed data"""

    with open('./src/data/seed_data/seed_data.json', encoding="utf-8") as file:
        file = file.read()

        seed_data = json.load(file)

    for item in seed_data:
        dynamodb.put_item(TableName=CALCULATOR_TABLE, Item=item)
        print('INFO: item', item)
