import json
import find_in_json

find = find_in_json
        
def image_is_weapon_stat_screen(source_text):
    if find.has_text(source_text=source_text, find_text='ATTACHMENT'):
        return True
    else:
        return False
        
def set_weapon_name(source_text, id=4):
    raw_weapon_name = find.find_value_by_id(source_text=source_text, id=id)
    final_weapon_name = raw_weapon_name.split('+')[0]
    return final_weapon_name

def determine_character(weapon_name='Choora'):
    weapon_owners = {
        'Choora': 'Toan',
        'Crystal Ring': 'Ruby'
    }
    return weapon_owners[weapon_name]


        #image_type = 'weapon_stat_screen'
        #character_name = 'toan'