""" Data layer code for handling User entity  """

from decimal import Decimal
from typing import Union
from boto3.dynamodb.conditions import Key
from pydantic import validate_arguments
from src.data.db_connection import get_table
from src.model.user import User


@validate_arguments
def get_user_by_username(username: str) -> Union[User, None]:
    """
    Retrieves the corresponding User instance given a username

    :param str username: User username
    :return Union[User, None]: User instance corresponding to the given username
    """
    table = get_table()
    response = table.query(
        IndexName="UsernameIndex",
        KeyConditionExpression=Key("username").eq(username),
    )
    items = response.get('Items')
    if items:
        # Parse response item and return an instance of the `User` class
        return User.parse_obj(items[0])

    return None


@validate_arguments
def get_user_by_id(user_id: str) -> Union[User, None]:
    """
    Retrieves a User instance for a given user ID.

    :param str user_id: User ID
    :return Union[User, None]: User instance corresponding to the given user ID
    """
    table = get_table()

    # Get user from DB ensuring data consistency for user balance and status
    item = table.get_item(
        Key={'id': f"{user_id}"},
        ConsistentRead=True
        ).get('Item')
    if item and User.parse_obj(item).is_active():
        # Parse response item and return an instance of the `User` class
        return User.parse_obj(item)

    return None


@validate_arguments
def get_user_initial_balance(user_id: str) -> Decimal:
    """
    Retrieves the user credit balance

    :param str user_id: User ID
    :raises ValueError: When user not found in the DB
    :return Decimal: User's credit balance
    """
    user = get_user_by_id(user_id)
    if user is None:
        raise ValueError("User not found.")

    return user.balance
