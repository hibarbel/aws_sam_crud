import boto3
import json
import os

# Récupérer le nom de la table depuis les variables d'environnement
table_name = os.environ.get('DYNAMODB_TABLE', 'Produits')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        print("Event received:", event)

        # Récupérer l'ID depuis API Gateway
        if 'pathParameters' in event and event['pathParameters'] is not None:
            user_id = event['pathParameters'].get('id')
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "Missing 'id' in path parameters"}),
                'headers': {'Content-Type': 'application/json'}
            }

        if not user_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "User ID is required"}),
                'headers': {'Content-Type': 'application/json'}
            }

        # Récupérer l'élément depuis DynamoDB
        response = table.get_item(Key={'UserId': user_id})

        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': "Item not found"}),
                'headers': {'Content-Type': 'application/json'}
            }

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item']),
            'headers': {'Content-Type': 'application/json'}
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
