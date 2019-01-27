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

    def test_get_image_name(self):
        
        args = {
    "bucket_image_folder_path": "new_images/",
    "bucket_text_folder_path": "new_text/",
    "local_text_folder": self.d.path,
    "weapon_mapping_file": "mappings/all_weapons.json"
    }

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
                "key": "archive/2019-01-18_13-53-00/Dvndh6DUYAAF1rM.jpg",
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
        
        image_name = categorize.get_image_name(event, args)
        self.assertEqual(image_name, 'Ruby_Crystal_Ring_stat_screen.jpg')

if __name__ == '__main__':
    unittest.main()