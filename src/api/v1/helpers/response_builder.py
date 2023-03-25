""" Helper to generate HTTP responses for AWS HTTP handlers"""

import json
from typing import Any, Dict, Union

from pydantic import validate_arguments


@validate_arguments
def build_response(
    status: int,
    success: Union[bool, None] = None,
    payload: Union[str, Dict[str, Any], object, None] = None,
) -> Dict:
    """
    Builds an HTTP response

    :param int status: Response status
    :param Union[str, Dict[str, Any], object] body: Response body
    :return Dict: HTTP Response
    """
    body = {}
    if success is not None:
        body["success"] = success
    if payload is not None:
        body["payload"] = payload

    response = {
        "statusCode": status,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE'
        }
    }

    if len(body) > 0:
        response["body"] = json.dumps(body , default=str)

    return response
