""" Authentication business logic. """

from typing import Union
import jwt
import bcrypt
from pydantic import validate_arguments

from src.configuration import JWT_SECRET_KEY
from src.data.users import get_user_by_username
from src.model.user import User


@validate_arguments
def generate_token(user_id: str) -> str:
    """
    Generates a JWT token for containing user_id

    :param str user_id: User id
    :return str: Generated token
    """

    payload = {"user_id": user_id}
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token


@validate_arguments
def verify_token(token: str) -> Union[str, None]:
    """
    Verifies provided JWT token

    :param str token: JWT token to be verified
    :return Union[str, None]: If verification succeeded the user_id else None.
    """
    try:
        print(f'Token:{token}')
        print(f'JWT_SECRET_KEY:{JWT_SECRET_KEY}')
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.exceptions.InvalidTokenError:
        return None


@validate_arguments
def authenticate(username: str, password: str) -> Union[str, None]:
    """
    Authenticate user by username and password

    :param str username: User username
    :param str password: User password
    :return Union[str, None]: If authentication succeeded the JWT to be used in
                              future requests else None.
    """
    # Retrieve user from database by username
    user: User = get_user_by_username(username)

    # Generate and return token if user exists credentials match
    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return generate_token(user.id)

    return None
