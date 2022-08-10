import json

def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from git Lambda demo during cloud class')
    }


