import responsavel_financeiro
import boto3
from moto import mock_s3

@mock_s3   
def test_put():
    conn = boto3.resource('s3', region_name='us-east-1')
    conn.create_bucket(Bucket='mybucket')
    body = conn.Object('mybucket', 'steve').get()['Body'].read().decode("utf-8")


    responsavel_financeiro.get_dados_responsavel_financeiro('mybucket', {'file_key':'file_key'})
    
    assert body == 'file_key'


@mock_s3
def test_empty_key_set_on_existing_key():
    s3 = boto3.resource("s3")
    client = boto3.client("s3")
    s3.create_bucket(Bucket="foobar")

    key = s3.Object("foobar", "the-key")
    key.put(Body=b"some content")

    resp = responsavel_financeiro.get_dados_responsavel_financeiro(Bucket="foobar", Key="the-key")
    resp["Body"].read().should.equal(b"some content")

    key.put(Body=b"")

    resp = client.get_object(Bucket="foobar", Key="the-key")
    resp.should.have.key("ContentLength").equal(0)
    resp["Body"].read().should.equal(b"")

