from src.api.v1.auth.auth import generate_token
from src.api.v1.auth.auth_handler import login
#from aws_lambda_powertools.utilities.typing import LambdaContext

def test_generate_token():
     token = generate_token('USER#novak')
     assert token is not None

# def test_login():
#      output = login(
#           {'path': '/auth',
#             'headers': {
#                     'host': 
#                     'localhost:3000', 
#                     'connection': 'keep-alive', 
#                     'content-length': '44', 
#                     'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"', 
#                     'accept': 'application/json, text/plain, */*', 
#                     'content-type': 'application/json', 
#                     'sec-ch-ua-mobile': '?0', 
#                     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 
#                     'sec-ch-ua-platform': '"macOS"', 'origin': 'http://localhost:3001', 
#                     'sec-fetch-site': 'same-site', 
#                     'sec-fetch-mode': 'cors', 
#                     'sec-fetch-dest': 'empty', 
#                     'referer': 'http://localhost:3001/', 
#                     'accept-encoding': 'gzip, deflate, br', 
#                     'accept-language': 'en-US,en;q=0.9,es;q=0.8,pt-BR;q=0.7,pt;q=0.6'
#                     }, 
#                     'pathParameters': {}, 
#                     'requestContext': {
#                          'accountId': 'localContext_accountId', 
#                          'resourceId': 'localContext_resourceId', 
#                          'stage': 'dev', 
#                          'requestId': 'localContext_requestId_94060701695167', 
#                          'identity': {
#                               'cognitoIdentityPoolId': 'localContext_cognitoIdentityPoolId', 
#                               'accountId': 'localContext_accountId', 
#                               'cognitoIdentityId': 'localContext_cognitoIdentityId',
#                               'caller': 'localContext_caller', 
#                               'apiKey': 'localContext_apiKey', 
#                               'sourceIp': '::1', 
#                               'cognitoAuthenticationType': 'localContext_cognitoAuthenticationType', 
#                               'cognitoAuthenticationProvider': 'localContext_cognitoAuthenticationProvider', 
#                               'userArn': 'localContext_userArn', 
#                               'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 
#                               'user': 'localContext_user'}
#                          }, 
#                     'resource': 'localContext_resource', 
#                     'httpMethod': 'POST', 
#                     'queryStringParameters': {}, 
#                     'body': '{"username":"novak","password":"passwor123"}', 
#                     'stageVariables': {}
#           }, 
#           _context = LambdaContext
#      )
#      assert output != None

