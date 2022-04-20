# bitcoin_price
Terraform (1.x) code to build an API GW and a Lambda function in AWS

Resources deployed:
- Lambda function in Python 3.8 with attached layer "requests" to retrieve the BTC value in USD.
- API Gateway and its required resource
- An S3 bucket to store the Lambda file

