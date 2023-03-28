"""A dummy docstring."""

import json
import os
import boto3

dynamodb = boto3.client('dynamodb')
CALCULATOR_TABLE = os.environ.get('CALCULATOR_TABLE')

def initialize_seed_data():
    """Initialize seed data"""

    with open('./src/data/seed_data/seed_data.json', encoding="utf-8") as file:

        seed_data = json.load(file)

    for row in seed_data:
        item = {}
        for attribute, value in row.items():
            if attribute in ['balance', 'cost']:
                item[attribute] = {'N' : str(value)}
            else:
                item[attribute] = {'S' : value}

        dynamodb.put_item(TableName=CALCULATOR_TABLE, Item=item)
