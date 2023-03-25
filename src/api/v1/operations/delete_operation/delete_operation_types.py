""" Types for new_operation API handler """

from pydantic import BaseModel


class DeleteOperationRequestParams(BaseModel):
    """Type of new_operation request payload"""

    operation_record_id: str
