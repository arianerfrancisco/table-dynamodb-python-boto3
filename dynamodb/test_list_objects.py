import datetime
import botocore.session
from botocore.stub import Stubber, ANY

def test_app():
    s3 = botocore.session.get_session().create_client('s3')
    stubber = Stubber(s3)

    response = {
        'IsTruncated': False,
        'Name': 'test-bucket',
        'MaxKeys': 1000, 'Prefix': '',
        'Contents': [{
            'Key': 'test.txt',
            'ETag': '"abc123"',
            'StorageClass': 'STANDARD',
            'LastModified': datetime.datetime(2016, 1, 20, 22, 9),
            'Owner': {'ID': 'abc123', 'DisplayName': 'myname'},
            'Size': 14814
        }],
        'EncodingType': 'url',
        'ResponseMetadata': {
            'RequestId': 'abc123',
            'HTTPStatusCode': 200,
            'HostId': 'abc123'
        },
        'Marker': ''
    }

    expected_params = {'Bucket': ANY}
    stubber.add_response('list_objects', response, expected_params)

    with stubber:
        service_response = s3.list_objects(Bucket='test-bucket')

    assert service_response == response