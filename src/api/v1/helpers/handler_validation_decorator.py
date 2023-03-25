""" Validation and exception handling decorator code """

import logging
from functools import wraps
from http import HTTPStatus
from typing import Any, Callable, Dict

from aws_lambda_powertools.utilities.parser import ValidationError
from aws_lambda_powertools.utilities.typing import LambdaContext
from requests.structures import CaseInsensitiveDict
from src.api.v1.auth.auth import verify_token
from src.api.v1.constants import INTERNAL_SERVER_ERROR, MISSING_AUTH_HEADER, WRONG_CREDENTIALS
from src.api.v1.helpers.response_builder import build_response

from src.configuration import DEBUG


# def validate_handler(handler: Callable, authenticate: bool = True) -> Callable:
def validate_handler(authenticate: bool = True) -> Callable:
    """
    Lambda Functions Event handler decorator factory

    :param bool authenticate: Whether to validate the Auth Token, defaults to True
    :return Callable: Decorator.
    """
    def decorator(handler: Callable) -> Callable:
        """
        Decorator to validate AWS HTTP handler functions

        :param Callable handler: Function handler to wrap with validator
        :return Callable: Function wrapped with validator
        """
        @wraps(handler)
        def wrapper_func(event: Dict[str, Any], _context: LambdaContext) -> Dict[str, Any]:
            user_id = None
            # If authenticate is required check and parse the Authorization Header
            if authenticate:
                headers = CaseInsensitiveDict(event["headers"])

                if "authorization" not in headers:
                    return build_response(HTTPStatus.UNAUTHORIZED, False, MISSING_AUTH_HEADER)

                token = headers["authorization"].split()[1]
                user_id = verify_token(token)

                if user_id is None:
                    return build_response(HTTPStatus.UNAUTHORIZED, False, WRONG_CREDENTIALS)

            if DEBUG:
                return handler(event, _context, user_id)

            try:
                return handler(event, _context, user_id)
            except (ValidationError, ValueError) as err:
                # log error, return BAD_REQUEST
                logging.error('VALIDATION ERROR: %s', err)
                return build_response(HTTPStatus.BAD_REQUEST, False, str(err))
            except Exception as err:  # pylint: disable=broad-except
                # log error, return INTERNAL_SERVER_ERROR
                logging.error('UNHANDLED ERROR: %s', err)
                return build_response(HTTPStatus.INTERNAL_SERVER_ERROR, False, INTERNAL_SERVER_ERROR)

        return wrapper_func
    return decorator
