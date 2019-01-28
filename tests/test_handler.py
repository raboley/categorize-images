import unittest
from testfixtures import tempdir, compare, TempDirectory

from context import categorize

class test_set_image_name(unittest.TestCase):
    """
    Ensure that we can set the image name correctly with weapon, character name and type
    """
    def setUp(self):
        self.d = TempDirectory()
        
    def tearDown(self):
        self.d.cleanup

    def test_get_image_name_when_is_stat_screen(self):
        event = {
        "Records": [
            {
            "eventVersion": "2.0",
            "eventTime": "1970-01-01T00:00:00.000Z",
            "requestParameters": {
                "sourceIPAddress": "127.0.0.1"
            },
            "s3": {
                "configurationId": "testConfigRule",
                "object": {
                "eTag": "0123456789abcdef0123456789abcdef",
                "sequencer": "0A1B2C3D4E5F678901",
                "key": "archive/2019-01-27_18-20-31/DwJ6vY_VAAIexyj.jpg",
                "size": 1024
                },
                "bucket": {
                "arn": "TEST",
                "name": "dark-cloud-bucket",
                "ownerIdentity": {
                    "principalId": "EXAMPLE"
                }
                },
                "s3SchemaVersion": "1.0"
            },
            "responseElements": {
                "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH",
                "x-amz-request-id": "EXAMPLE123456789"
            },
            "awsRegion": "us-east-1",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
                "principalId": "EXAMPLE"
            },
            "eventSource": "aws:s3"
            }
        ]
        }

        args = {
            "bucket_name": event['Records'][0]['s3']['bucket']['name'],
            "image_key": event['Records'][0]['s3']['object']['key'],
            "bucket_image_folder_path": "new_images/",
            "bucket_text_folder_path": "new_text/",
            "local_text_folder": self.d.path,
            "weapon_mapping_file": "mappings/all_weapons.json",
            "datefolder_character_weapon_mapping_file": "__test/mappings/datefolder_character_weapon_mapping_file.json",
            "output_folder_name": "__test/weapons",
            "output_bucket_name": "dark-cloud-bucket"
        }

        file_object =  categorize.FileS3(event['Records'][0]['s3']['bucket']['name'])
        output_file_object = categorize.FileS3(args["output_bucket_name"])
        image_name = categorize.get_image_name(event, args, file_object, output_file_object)
        self.assertEqual(image_name, 'Toan_Choora_Stat.jpg')