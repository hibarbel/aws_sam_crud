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

        # Vérifier si le corps de la requête contient des données
        if 'body' not in event or not event['body']:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "Missing request body"}),
                'headers': {'Content-Type': 'application/json'}
            }

        body = json.loads(event['body'])
        new_name = body.get('name')

        if not new_name:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "Missing 'name' in request body"}),
                'headers': {'Content-Type': 'application/json'}
            }

        # Mettre à jour l'élément dans DynamoDB
        response = table.update_item(
            Key={'UserId': user_id},
            UpdateExpression="SET #n = :name",
            ExpressionAttributeNames={'#n': 'Name'},
            ExpressionAttributeValues={':name': new_name},
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'msg': f'Item {user_id} updated successfully'}),
            'headers': {'Content-Type': 'application/json'}
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
