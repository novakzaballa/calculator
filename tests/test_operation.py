from src.data.operation_records import get_user_balance
from src.model.operations.operation import add, subtract, multiply, divide, sqrt
from src.model.operations.perform_operation import perform_operation

def test_add():
     output = add(1,3)
     assert output == 4

def test_subtract():
     output = subtract(5,5)
     assert output == 0

def test_multiply():
     output = multiply(3,4)
     assert output == 12

def test_divide():
     output = divide(40,4)
     assert output == 10

def test_sqrt():
     output = sqrt(9)
     assert output == 3
