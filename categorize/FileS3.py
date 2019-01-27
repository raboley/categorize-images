import boto3
import json
from .FileOs import FileOs
from botocore.exceptions import ClientError

class FileS3(FileOs):

    def read_json_file(self, key):
        body = self.read_file(key=key)
        return json.loads(body)

    def read_file(self, key):
        if self.check_existence(key=key):
            client = boto3.client('s3')
            s3_object = client.get_object(Bucket=self.bucket_name, Key=key)
            body = s3_object['Body']
            return body.read()

    def append_json_file(self, key, json_data):
        if self.check_existence(key=key):
            original_json = self.read_json_file(key=key)
            original_json.append(json_data)
        else:
            original_json = []
            original_json.append(json_data)
        self.put_json_file(key=key, json_data=original_json)

    def check_existence(self, key):
        try:
            self.client.head_object(Bucket=self.bucket_name, Key=key)
        except ClientError: #as e:
            return False
            #return int(e.response['Error']['Code']) != 404
        return True

    def put_json_file(self, key, json_data):
        binary_data = json.dumps(json_data).encode('utf-8')
        self.put_file(key=key, binary_data=binary_data)

    def put_file(self, key, binary_data):
        self.client.put_object(Body=binary_data, Bucket=self.bucket_name, Key=key)

    def __init__(self, bucket):
        self.client = boto3.client('s3')
        self.bucket_name = bucket

