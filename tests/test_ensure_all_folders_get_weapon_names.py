from context import categorize
import unittest
import boto3
# from testfixtures import tempdir, compare, TempDirectory
# import os
# import json

FileS3 = categorize.FileS3

class test_ensure_all_folders_get_weapon_names(unittest.TestCase):
    """
    All archve/id folders should get a matching entry in the weapon mapping file
    and if they don't there should be an alert
    """

    def setUp(self):
        self.bucket = 'dark-cloud-bucket-dev'
        self.File_object = FileS3(bucket=self.bucket)
        self.output_folder = "__testing/"
    
    def test_get_all_folder_names(self):
        self.File_object