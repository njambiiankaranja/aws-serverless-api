import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    
    http_method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')
    
    if http_method == 'POST':
        body = json.loads(event.get('body', '{}'))
        item_id = body.get('id', '1')
        item_name = body.get('name', 'Default Item')
        
        table.put_item(Item={'id': item_id, 'name': item_name})
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Item created successfully', 'id': item_id})
        }
    
    elif http_method == 'GET':
        response = table.scan()
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
        
    return {
        'statusCode': 400,
        'body': json.dumps({'error': 'Unsupported HTTP method'})
    }