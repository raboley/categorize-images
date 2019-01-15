import rekognize_image 
import json
import boto3
import get_matching_s3_objects
import upload_images_to_s3
import get_basename
s3 = boto3.resource('s3')

bucket_name = 'dark-cloud-bucket2'
bucket_image_folder_path = 'new_images/'
bucket_text_folder_path = 'new_text/'
photo_extension = '.jpg'
local_text_folder = './picture_text'


files = get_matching_s3_objects.get_matching_s3_keys(bucket=bucket_name, prefix=bucket_image_folder_path, suffix=photo_extension)

for photo in files: 
    print(photo)
    rekognize_image.write_image_json_to_file(foldertosavein=local_text_folder, bucket=bucket_name, photo=photo)

    local_text_fullpath = rekognize_image.create_json_fullpath(foldertosavein=local_text_folder, photo=photo)
    bucket_text_fullpath = bucket_text_folder_path + get_basename.path_basename(photo) + '.json'
    upload_images_to_s3.uploadfile(bucket=bucket_name, upload_file_full_path=bucket_text_fullpath, local_filepath=local_text_fullpath)
