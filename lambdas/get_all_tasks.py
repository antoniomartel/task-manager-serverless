import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    task_id = str(uuid.uuid4())
    title = body.get('title', '')

    if not title:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Title is required'})
        }

    item = {
        'id': task_id,
        'title': title,
        'completed': False
    }

    table.put_item(Item=item)

    return {
        'statusCode': 201,
        'body': json.dumps(item)
    }
