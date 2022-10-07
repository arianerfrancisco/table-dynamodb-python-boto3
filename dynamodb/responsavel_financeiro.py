import boto3
from moto import mock_s3


@mock_s3
def get_dados_responsavel_financeiro(bucket_name, cd):
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key= file_key)
    return response['Body'].read()
    
def test_put_item():
    app.client = boto3.client('dynamodb')

# @mock_s3   
# def test_get(bucket_name, file_key):
#     conn = boto3.resource('s3', region_name='us-east-1')
#     conn.create_bucket(Bucket=bucket_name)
#     conn.put_object(Bucket=bucket_name, Key=file_key, Body=value)
#     body = conn.Object('mybucket', 'steve').get()[
#         'Body'].read().decode("utf-8")

#     assert body == 'is awesome'

# def save(mybucket, name, value):
#         s3 = boto3.client('s3', region_name='us-east-1')
#         s3.put_object(Bucket=mybucket, Key=name, Body=value)

# ariane= save('ariane','ariane', 'ariane')