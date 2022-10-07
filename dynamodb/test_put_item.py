import boto3
import app
from botocore.stub import Stubber


def test_put_item():
    app.client = boto3.client('dynamodb')    
    dynamo_stubber = Stubber(app.client) 
    
    ITEM = { 'Key': {'S': 'xxxx'}, 'Atributo': {'S': 'yyyy'}}

    parametro_put_item = {'TableName':'TABELA','Item':ITEM }
    resposta_put_item = {'ResponseMetadata': { 'HTTPStatusCode': 200 }}
    dynamo_stubber.add_response('put_item',resposta_put_item,parametro_put_item)
    dynamo_stubber.activate()
    assert dynamo_stubber .assert_no_pending_responses() is None
