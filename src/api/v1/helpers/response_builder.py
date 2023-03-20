""" Helper to generate HTTP responses for AWS HTTP handlers"""

from typing import Any, Dict, Union

from pydantic import validate_arguments


@validate_arguments
def build_response(status: int, body: Union[str, Dict[str, Any], object]) -> Dict:
    """
    Builds an HTTP response

    :param int status: Response status
    :param Union[str, Dict[str, Any], object] body: Response body
    :return Dict: HTTP Response
    """
    return {
        "statusCode": status,
        "body": body,
    }
