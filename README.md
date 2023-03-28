# calculator
Coded by Novak Zaballa

The scope of this project is login and operations backend fro a payed calculator.

This project has been built with Serverless Framework and targeting AWS lambda with Python 3.8 + DynamoDB + Aurora PostgreSQL. You can deploy the project to AWS installing and configuring serverless, or you can run the services locally, using the serverless-offline plugin, which is included. The offline configuration also includes a local DynamoDB instance is provided by the serverless-dynamodb-local plugin.

### Setup and test locally
To test your service locally, without having to deploy it first, you will need node.js (tested with v13.7.0) and follow the steps below in the root directory of the project.

npm install
serverless dynamodb install
serverless dynamodb start --migrate
The --migrate option creates the schema. Ctl+C to stop the local DynamoDB. The DB schema and data will be lost since by default the local DB is stored in memory.

Run service offline
To test the project locally use:

serverless offline start
Alternatively you can debug the project with VS Code. This repository includes the launch.json file needed by VS Code to run and debug this serverless project locally. How ever dynamodb needs to be started.

Configure and Deploy service to AWS
You will need to configure authentication key in a .env file in the root folder containing:
"""JWT_SECRET_KEY=YOUR_SECRET_KEY_VALUE"""

To deploy the service you need an account in AWS. Use the following command:

serverless deploy -v

Authorization for testing
Every request must include an authorization header containing the OAuth Bearer token. For testing purposes currently an account is in seed in the DB. The request content type must be application/json as per the examples below. While in dev stage, I will provide valid access credentials for a test user through a secure channel.

### Live Demo
You can test locally following the former instructions, however there is also a live test with the following endpoints published in my AWS account for testing purposes:

Available endpoints:
  GET - https://68i17san2e.execute-api.us-east-1.amazonaws.com/dev/api/v1/operations
  POST - https://68i17san2e.execute-api.us-east-1.amazonaws.com/dev/api/v1/operations
  POST - https://68i17san2e.execute-api.us-east-1.amazonaws.com/dev/api/v1/auth
  PUT - https://68i17san2e.execute-api.us-east-1.amazonaws.com/dev/api/v1/operations/{operation_record_id}

### Live Testing with Swagger UI

[Click here to see API documentation and test iit n Swagger UI](https://app.swaggerhub.com/apis-docs/novak.zaballa/calculator-api/1#/)
