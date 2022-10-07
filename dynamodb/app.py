import boto3

client = boto3.client('dynamodb')

ITEM = {
    'Key': {'S': 'xxxx'},
    'Atributo': {'S': 'yyyy'}
}

response = client.put_item(TableName='TABELA',Item=ITEM)