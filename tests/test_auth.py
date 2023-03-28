from src.api.v1.auth.auth import generate_token
from src.api.v1.auth.auth_handler import login
#from aws_lambda_powertools.utilities.typing import LambdaContext

def test_generate_token():
     token = generate_token('USER#novak')
     assert token is not None
