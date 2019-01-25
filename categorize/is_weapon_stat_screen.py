import json
from .find_in_json import find_value_by_id, has_text, get_json


def image_is_weapon_stat_screen(source_text):
    if has_text(source_text=source_text, find_text='ATTACHMENT'):
        return True
    else:
        return False
        
def get_weapon_name(source_text, id=4):
    raw_weapon_name = find_value_by_id(source_text=source_text, id=id)
    final_weapon_name = raw_weapon_name.split('+')[0]
    return final_weapon_name

def determine_character(weapon_name, filepath):
    weapon_owners = get_json(filepath)
    return weapon_owners[weapon_name]

def write_weapon_map_to_file(parent_folder, weapon_name, pair):
    pair.set_pair(parent_folder, weapon_name)
    
        #image_type = 'weapon_stat_screen'
        #character_name = 'toan'