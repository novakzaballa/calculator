""" Domain model entity User """

from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class UserStatus(Enum):
    """Enum of the different user statuses allowed"""

    ACTIVE = "active"
    INACTIVE = "inactive"


class User(BaseModel):
    """User entity. Extends pydantic BaseModel for automatic validation"""

    id: str
    username: str
    password: str
    status: UserStatus
    balance: Decimal

    class Config:
        """Pydantic configuration to use enum values for validation"""

        use_enum_values = True

    def is_active(self):
        """
        Determine if user is active

        :return _type_: True if user is active false otherwise
        """
        if self.status == UserStatus.ACTIVE.value:
            return True

        return False
