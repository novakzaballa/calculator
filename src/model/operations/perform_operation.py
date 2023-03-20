""" The code related with the execution a requested operation """
from decimal import Decimal
from src.data.operation_records import get_user_balance, save_operation_record
from src.data.operations import get_operation_by_name
from src.model.operations.operation import Operations, operate
from src.model.aggregates.user_operation_record import OperationRecord


def perform_operation(user_id: str, operation_name: Operations, **params) -> Decimal:
    """
    Performs the requested operation

    :param str user_id: The user ID requesting the operation
    :param Operations operation_name: Operation type (name)
    :return Decimal: The result of the operation performed
    """
    # Perform corresponding operation and store the result
    result = operate[operation_name](**params)

    # Get operation id and cost
    operation = get_operation_by_name(operation_name)

    # Get current user credit balance
    user_balance = get_user_balance(user_id)

    if user_balance - operation.cost < 0.0:
        print('Insufficient credit in balance to perform the requested operation.'
              f' Balance:{user_balance} Cost:{operation.cost}')
        raise ValueError('Insufficient credit in balance to perform the requested operation.')

    # Store the operation record in the DB
    save_operation_record(OperationRecord(
        operation_id=operation.id,
        user_id=user_id,
        amount=operation.cost,
        user_balance=user_balance - operation.cost,
        operation_response=str(result)
    ))

    return result
