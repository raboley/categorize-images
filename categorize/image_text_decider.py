import find_in_json
import is_weapon_stat_screen

stat = is_weapon_stat_screen

def determine_picture_type(source_text):
    if stat.image_is_weapon_stat_screen(source_text):
        return 'stat_screen'

