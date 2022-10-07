from hashlib import algorithms_guaranteed
from msilib import Table
from winreg import REG_NOTIFY_CHANGE_LAST_SET
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb',
                                  aws_access_key_id="anything",
                                  aws_secret_access_key="anything",
                                  region_name = 'us-east-2', endpoint_url="http://localhost:8000")

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='taabedslaa1a2s',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 105,
        'WriteCapacityUnits': 105
    }
)

# # Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)
username='tommy'
sobrenome='rocha'

def inserir():
    table.put_item(
        Item={
        'username': username,
        'first_name': sobrenome,
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)


response = table.scan(FilterExpression=Attr('username').eq(username) & Attr('first_name').eq(sobrenome)).get('Items',[])
if len(response) == 0:
    print ('No items found')
    inserir()
[

response = table.scan(FilterExpression=Attr('username').eq(username) & Attr('first_name').eq(sobrenome)).get('Items',[])
if len(response) == 0:
    print ('No items found')

if len(response) > 0 :
    print ('itens encontrados')]

dados = table.scan()

dados['Items']
