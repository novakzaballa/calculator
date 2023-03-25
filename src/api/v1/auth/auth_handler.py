""" API endpoint auth handler """

from http import HTTPStatus
from typing import Any, Dict

from aws_lambda_powertools.utilities.parser import parse
from aws_lambda_powertools.utilities.typing import LambdaContext

from src.api.v1.auth.auth import authenticate
from src.api.v1.auth.input_params_types import LoginRequestParams
from src.api.v1.helpers.handler_validation_decorator import validate_handler
from src.api.v1.helpers.response_builder import build_response
from src.api.v1.constants import WRONG_CREDENTIALS


@validate_handler(authenticate=False)
def login(event: Dict[str, Any], _context: LambdaContext, _user_id: str=None) -> dict:
    """
    Handles the request to the auth API endpoint

    :param Dict[str, Any] event: AWS lambda event
    :param LambdaContext _context: AWS lambda context
    :return dict: AWS HTTP handler response.
    """
    # Parse params from request body
    params: LoginRequestParams = parse(
        event=event["body"],
        model=LoginRequestParams,
    )
    username = params.username
    password = params.password
    token = authenticate(username, password)

    if token:
        return build_response(HTTPStatus.OK, True, {"token": token})

    else:
        return build_response(
            HTTPStatus.UNAUTHORIZED, False, {"message": WRONG_CREDENTIALS}
        )
