""" API endpoint delete_operation handler """

from http import HTTPStatus
from typing import Any, Dict

from aws_lambda_powertools.utilities.typing import LambdaContext

from src.api.v1.helpers.handler_validation_decorator import validate_handler
from src.api.v1.helpers.response_builder import build_response
from src.data.operation_records import soft_delete_operation_record


@validate_handler()
def delete_operation(
    event: Dict[str, Any], _context: LambdaContext, _user_id: str = None
) -> Dict[str, Any]:
    """
    Handles the request to the delete_operation API endpoint

    :param Dict[str, Any] event: AWS lambda event
    :param LambdaContext _context: AWS lambda context
    :return dict: AWS HTTP handler response.
    """
    # Extract and parse request path params
    if 'pathParameters' in event:
        path_params = event['pathParameters']
        operation_id = path_params['operation_id']
    else:
        raise ValueError("pathParameters not found.")


    # params: DeleteOperationRequestParams = parse(
    #     event=event["body"],
    #     model=DeleteOperationRequestParams,
    # )

    soft_delete_operation_record(int(operation_id))
    return build_response(
        HTTPStatus.OK,
        True,
        {"message": f"Record {operation_id} deleted"}
    )
