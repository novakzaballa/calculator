""" API endpoint new_operation handler """

import json
from http import HTTPStatus
from typing import Any, Dict

from aws_lambda_powertools.utilities.parser import parse
from aws_lambda_powertools.utilities.typing import LambdaContext
from src.api.v1.helpers.handler_validation_decorator import validate_handler
from src.api.v1.helpers.response_builder import build_response
from src.api.v1.operations.new_operation.input_params_types import (
    NewOperationRequestParams,
)
from src.model.operations.perform_operation import perform_operation


@validate_handler()
def new_operation(
    event: Dict[str, Any], _context: LambdaContext, user_id: str = None
) -> Dict[str, Any]:
    """
    Handles the request to the new_operation API endpoint

    :param Dict[str, Any] event: AWS lambda event
    :param LambdaContext _context: AWS lambda context
    :return dict: AWS HTTP handler response.
    """

    # Extract and parse the HTTP body
    params: NewOperationRequestParams = parse(
        event=event["body"],
        model=NewOperationRequestParams,
    )

    result = perform_operation(user_id, params.operation, **params.arguments)

    return build_response(HTTPStatus.OK, json.dumps({"result": result}, default=str))
