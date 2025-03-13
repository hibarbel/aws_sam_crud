def handler(event, context):
    id = event['pathParameters']['id']
    print("id: " + id)
    return {
                "statusCode": 200,
                "body": "Success! Your request was processed."
            }