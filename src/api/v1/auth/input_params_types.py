""" Types for Auth API handler """

from pydantic import BaseModel


class LoginRequestParams(BaseModel):
    """Type for Auth Request Payload"""

    username: str
    password: str
