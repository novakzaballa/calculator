""" API endpoint get_records handler """

from http import HTTPStatus
from typing import Any, Dict

from aws_lambda_powertools.utilities.typing import LambdaContext
from src.api.v1.helpers.handler_validation_decorator import validate_handler
from src.api.v1.helpers.response_builder import build_response
from src.data.operation_records import get_user_balance


@validate_handler()
def get_user_balance_handler(
    _event: Dict[str, Any], _context: LambdaContext, user_id: str = None
) -> Dict[str, Any]:
    """
    Handles the request to the get_records API endpoint

    :param Dict[str, Any] event: AWS lambda event
    :param LambdaContext _context: AWS lambda context
    :return dict: AWS HTTP handler response.
    """

    balance: float = get_user_balance(user_id)

    return build_response(
        HTTPStatus.OK,
        True,
        {"result": balance},
    )
