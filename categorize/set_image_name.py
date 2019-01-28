from .rekognize_image  import create_json_fullpath, rekognize_image_json, write_image_json_to_file
from .get_matching_s3_objects import get_matching_s3_keys
from .get_basename import path_basename
from .upload_images_to_s3 import uploadfile
from. find_in_json import get_json
from .image_text_decider import determine_picture_type
from .is_weapon_stat_screen import image_is_weapon_stat_screen, get_weapon_name, determine_character, write_weapon_map_to_file, get_weapon_list
from .read_file_s3 import read_file_s3
from .retry_wrapper import retry
import json
import os

def copy_image_to_folder_with_categorized_name(args, file_object, output_file_object):
    categorized_image_key = get_image_name(args, file_object, output_file_object)
    destination_path = os.path.join(args["output_folder_name"], categorized_image_key)
    image_key = args["image_key"]
    file_object.copy_file(source_path=image_key, dest_path=destination_path)

def get_image_name(args, file_object, output_file_object):
    # Create json text from image on s3
    bucket_name = args["bucket_name"]
    image_key = args["image_key"]
    local_text_folder = args['local_text_folder']
    
    if not file_object.check_existence(key=image_key):
        raise ValueError('Error ' + image_key + 'does not exist or we dont have permissions to view it')

    local_json_path = write_image_json_to_file(foldertosavein=local_text_folder, bucket=bucket_name, photo=image_key)
    
    # Upload json file to s3
    bucket_text_folder_path = args['bucket_text_folder_path']
    bucket_text_fullpath = bucket_text_folder_path + path_basename(image_key) + ".json"
    uploadfile(bucket=bucket_name, upload_file_full_path=bucket_text_fullpath, local_filepath=local_json_path)
    
    # get the parent folder of the image    
    key_folder = file_object.get_parent_folder_name(image_key)
    
    # Determine image type based on Json
    json_data = get_json(local_json_path)
    picture_type = determine_picture_type(json_data)



    if picture_type == 'Stat':
        # get the list of weapons

        ## Read the list
        weapon_list_json = file_object.read_json_file(key=args['weapon_mapping_file'])
        ## parse the weapons file
        weapons_list = get_weapon_list(weapon_list_json)
        # get the weapon name
        weapon_name = get_weapon_name(source_text=json_data, id=4, weapon_list=weapons_list)
        
        # get the character name
        character_name = determine_character(weapon_name, weapon_list_json)

        

        # Put folder path, weapon name, character name combo up in s3
        date_folder_mapping = {"key":key_folder, "weapon name": weapon_name, "character name": character_name}
        file_object.append_json_file(key=args['datefolder_character_weapon_mapping_file'], json_data=date_folder_mapping)

    this_folder_mappings = get_folder_mappings(key=args['datefolder_character_weapon_mapping_file'], file_object=file_object, key_folder=key_folder)
    if this_folder_mappings:
        
        if picture_type == 'Side':
            side_one_name = this_folder_mappings["character name"] + '_' + this_folder_mappings["weapon name"] + '_Side1.jpg'
            picture_type = determine_side_number(side_one_key=side_one_name,output_file_object=output_file_object)
        
        # create the raw file name
        raw_filename = this_folder_mappings["character name"] + '_' + this_folder_mappings["weapon name"] + '_' + picture_type + '.jpg'
        
        # replace all spaces with underscores
        final_filename = raw_filename.replace(" ", "_")
        return final_filename

@retry(retry_count=6, delay=5, allowed_exceptions=ValueError)
def get_folder_mappings(key, file_object, key_folder):
    # get the file name elements
    full_character_weapon_mapping_json = file_object.read_json_file(key=key)
    this_folder_mappings = next((item for item in full_character_weapon_mapping_json if item["key"] == key_folder), 'unknown')
    if this_folder_mappings == 'unknown':
        raise ValueError(key_folder + " does not have a matching weapon name, character yet")
    else:
        return this_folder_mappings

def determine_side_number(side_one_key,output_file_object):
    # check if Side1 exists
    if output_file_object.check_existence(key=side_one_key):
        return 'Side2'
    else:
        return 'Side1'

