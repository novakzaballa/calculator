""" Domain Model Entity OperationRecord """

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Union
# from uuid import uuid4

from pydantic import BaseModel


class OperationRecord(BaseModel):
    """Class that represents de model entity for the operation records"""

    id: Union[int, None]
    operation_id: Union[str, None]
    user_id: Union[str, None]
    amount: Decimal
    user_balance: Decimal
    operation_response: str
    date: datetime = datetime.now()

    class Config:
        """Pydantic configuration to use enum values for validation"""

        orm_mode = True
