""" Types for new_operation API handler """

from typing import Dict

from pydantic import BaseModel

from src.model.operations.operation import Operations


class NewOperationRequestParams(BaseModel):
    """Type of new_operation request payload"""

    operation: Operations
    arguments: Dict

    class Config:
        """Pydantic configuration to use enum values for validation"""

        use_enum_values = True
