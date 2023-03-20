""" API endpoint get_records handler """

import json
from http import HTTPStatus
from typing import Any, Dict

from aws_lambda_powertools.utilities.typing import LambdaContext
from src.api.v1.helpers.handler_validation_decorator import validate_handler
from src.api.v1.helpers.response_builder import build_response
from src.data.operation_records import get_user_operation_record_page


@validate_handler()
def get_user_operations(
    event: Dict[str, Any], _context: LambdaContext, user_id: str = None
) -> Dict[str, Any]:
    """
    Handles the request to the get_records API endpoint

    :param Dict[str, Any] event: AWS lambda event
    :param LambdaContext _context: AWS lambda context
    :return dict: AWS HTTP handler response.
    """
    # Extract and parse the Query String params
    params = event["queryStringParameters"]
    parsed_params = {
        "user_id": user_id,
        "page_number": int(params["page_number"]),
        "rows_per_page": int(params["rows_per_page"]),
    }

    if "sort_by" in params:
        parsed_params["sort_by"] = params["sort_by"]

    if "sort_type" in params:
        parsed_params["sort_type"] = params["sort_type"]

    if "operation_id" in params:
        parsed_params["operation_id"] = params["operation_id"]

    result, count = get_user_operation_record_page(**parsed_params)

    return build_response(
        HTTPStatus.OK,
        json.dumps(
            {
                "result": result,
                "count": count,
            },
            default=str,
        ),
    )
