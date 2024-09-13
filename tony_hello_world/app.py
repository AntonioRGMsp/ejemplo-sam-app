import json

# import requests


def lambda_handler(event, context):
    print('Event received: ')
    print(event)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "status_message": "invoke success",
        })
    }
    print(json.dumps(response))
