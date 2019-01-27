from .rekognize_image  import create_json_fullpath, rekognize_image_json, write_image_json_to_file
from .get_matching_s3_objects import get_matching_s3_keys
from .get_basename import path_basename
from .upload_images_to_s3 import uploadfile
from. find_in_json import get_json
from .image_text_decider import determine_picture_type
from .is_weapon_stat_screen import image_is_weapon_stat_screen, get_weapon_name, determine_character, write_weapon_map_to_file, get_weapon_list
from .read_file_s3 import read_file_s3
import json

event = {
    "bucket_name": "dark-cloud-bucket2",
    "bucket_image_folder_path": "new_images/",
    "bucket_text_folder_path": "new_text/",
    "photo_extension": ".jpg",
    "local_text_folder": "./picture_text",
    "image_key": ""
}

def get_image_name(event, args):
    # Create json text from image on s3
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    local_text_folder = args['local_text_folder']
    local_json_path = write_image_json_to_file(foldertosavein=local_text_folder, bucket=bucket_name, photo=file_key)
    
    # Upload json file to s3
    bucket_text_folder_path = args['bucket_text_folder_path']
    bucket_text_fullpath = bucket_text_folder_path + path_basename(file_key) + ".json"
    uploadfile(bucket=bucket_name, upload_file_full_path=bucket_text_fullpath, local_filepath=local_json_path)

    # Determine image type based on Json
    json_data = get_json(local_json_path)
    picture_type = determine_picture_type(json_data)

    if picture_type == 'stat_screen':
        # get the list of weapons

        ## Read the list
        weapon_mapping_file = args['weapon_mapping_file']
        raw_json = read_file_s3(bucket_name, weapon_mapping_file)
        weapon_list_json = json.loads(raw_json)
        ## Maybe abstract the reading

        ## parse the weapons file
        weapons_list = get_weapon_list(weapon_list_json)
        
        # get the weapon name
        weapon_name = get_weapon_name(source_text=json_data, id=4, weapon_list=weapons_list)
        
        # get the character name
        character_name = determine_character(weapon_name, weapon_list_json)

        # Put folder path, weapon name, character name combo up in s3
        #client = boto3.client('s3')
        #client.put_object(Body=more_binary_data, Bucket='my_bucket_name', Key='my/key/including/anotherfilename.txt')

        # create the raw file name
        raw_filename = character_name + '_' + weapon_name + '_' + picture_type + '.jpg'
        
        # replace all spaces with underscores
        final_filename = raw_filename.replace(" ", "_")
        return final_filename

