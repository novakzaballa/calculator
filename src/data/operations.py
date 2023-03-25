""" Data layer code for handling Operation entity """
from decimal import Decimal
from boto3.dynamodb.conditions import Key
from pydantic import validate_arguments
from src.data.db_connection import get_table
from src.model.operations.operation import Operation


@validate_arguments
def get_operation_by_name(operation_name: str) -> Operation:
    """
    Returns operation by a given operation type (name)

    :param str operation_name: Operation type (name)
    :return Operation: Returns an Operation instance for the provided name
    """
    table = get_table()
    response = table.query(
        IndexName="OperationTypeIndex",
        KeyConditionExpression=Key("type").eq(operation_name),
    )
    items = response.get("Items")
    if items:
        # Parse response item and return an instance of the `Operation` class
        return Operation.parse_obj(items[0])
    else:
        return None


@validate_arguments
def get_operation_attribute(operation_name: str, attribute: str) -> Decimal:
    """
    Retrieves the value of a specific attribute for a determined operation type

    :param str operation_name: Operation type (name)
    :param str attribute: Operation attribute name
    :raises ValueError: If type (name) not found
    :return Decimal: Returns the corresponding attribute value
    """
    operation = get_operation_by_name(operation_name)
    if operation is not None:
        return operation.dict()[attribute]
    else:
        raise ValueError(f"Operation {operation_name} not found")
