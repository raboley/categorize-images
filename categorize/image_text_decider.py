from .is_weapon_stat_screen import image_is_weapon_stat_screen

def determine_picture_type(source_text):
    if image_is_weapon_stat_screen(source_text):
        return 'stat_screen'

