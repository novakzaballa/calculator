""" Domain model entity Operation and related assets """

import math
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, validate_arguments

from src.external.random_org import get_random_string


class Operations(Enum):
    """Enum of the different operations supported"""

    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"
    DIVISION = "division"
    SQUARE_ROOT = "square_root"
    RANDOM_STRING = "random_string"


class Operation(BaseModel):
    """Class that represents de model entity operation"""

    id: str
    type: Operations
    cost: Decimal

    class Config:
        """Pydantic configuration to use enum values for validation"""

        use_enum_values = True


@validate_arguments
def add(operand1: Decimal, operand2: Decimal) -> Decimal:
    """
    Adds operand1 to operand2 and returns the result

    :param Decimal operand1: First operand of the addition operation
    :param Decimal operand2: Second operand of the addition operation
    :return Decimal: Result of the addition operation
    """
    return operand1 + operand2


@validate_arguments
def subtract(operand1: Decimal, operand2: Decimal) -> Decimal:
    """
    Subtract operand2 from operand1 and returns the result

    :param Decimal operand1: First operand of the subtraction operation
    :param Decimal operand2: Second operand of the subtraction operation
    :return Decimal: Result of the subtraction operation"""
    return operand1 - operand2


@validate_arguments
def multiply(operand1: Decimal, operand2: Decimal) -> Decimal:
    """
    Multiplies operand1 by operand2 and returns the result

    :param Decimal operand1: First factor
    :param Decimal operand2: Second factor
    :return Decimal: Result of the multiplication
    """
    return operand1 * operand2


@validate_arguments
def divide(operand1: Decimal, operand2: Decimal) -> Decimal:
    """
    Divides operand1 by operand2 and returns the result

    :param Decimal operand1: First operand of the division
    :param Decimal operand2: Second operand of the division
    :raises ValueError: When operand2, the divisor, is 0.
    :return Decimal: Result of the division
    """
    if operand2 == 0:
        raise ValueError("Operand 2 (divisor) can not be 0.")
    return operand1 / operand2


@validate_arguments
def sqrt(operand1: Decimal) -> Decimal:
    """
    Calculates and returns the square root of a given number.

    :param Decimal operand1: The number for which the square root is calculated
    :raises ValueError: When the number is negative.
    :return Decimal: The square root of the number provided.
    """
    if operand1 < 0:
        raise ValueError("Operand must be greater than 0.")
    return math.sqrt(operand1)


# Mapping of the different operation types and their corresponding function
operate = {
    Operations.ADDITION.value: add,
    Operations.SUBTRACTION.value: subtract,
    Operations.MULTIPLICATION.value: multiply,
    Operations.DIVISION.value: divide,
    Operations.SQUARE_ROOT.value: sqrt,
    Operations.RANDOM_STRING.value: get_random_string,
}
