import unittest
from .context import categorize

find = categorize.find_in_json
is_weapon_stat_screen = categorize.is_weapon_stat_screen

json_path = './picture_text/test.json'
main_screen_path = './picture_text/Ruby_Goddes_Ring-Main.json'
stat_screen_path = './picture_text/Ruby_Crystal_Ring_Stats.json'
toan_screen_path = './picture_text/Toan_Choora_Stats.json'

class test_image_is_weapon_stat_screen(unittest.TestCase):
    """
    Ensure that we can correctly identify if something is weapon stat screen or not
    """

    def test_weapon_stat_screen_image_is_stat_image(self):
        self.assertTrue(is_weapon_stat_screen.image_is_weapon_stat_screen(source_text=json))

    def test_NON_weapon_stat_screen_image_is_NOT_stat_image(self):
        fail_json = find.get_json(main_screen_path)
        self.assertFalse(is_weapon_stat_screen.image_is_weapon_stat_screen(source_text=fail_json))

class test_set_weapon_name(unittest.TestCase):
    """
    Ensure that if it is a weapon stat screen, we can determine the weapon name from it
    """
    def test_weapon_name_is_set(self):
        pass_json = find.get_json(stat_screen_path)
        self.assertEqual(is_weapon_stat_screen.set_weapon_name(source_text=pass_json, id=4),'Crystaring')

    def test_weapon_name_does_not_have_modifier(self):
        toan_json = find.get_json(toan_screen_path)
        self.assertEqual(is_weapon_stat_screen.set_weapon_name(source_text=toan_json, id=4),'Choora')

class test_determine_character_name(unittest.TestCase):
    """
    Ensure that if we have a weapon name we can determine who it belongs to
    """
    def test_choora_belongs_to_toan(self):
        self.assertEqual(is_weapon_stat_screen.determine_character(weapon_name='Choora'), 'Toan')


json = [{'DetectedText': 'ATTACHMENT', 'Type': 'LINE', 'Id': 0, 'Confidence': 99.18334197998047, 'Geometry': {'BoundingBox': {'Width': 0.08702175319194794, 'Height': 0.04405874386429787, 'Left': 0.7036759257316589, 'Top': 0.10547396540641785}, 'Polygon': [{'X': 0.7036759257316589, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.14953270554542542}, {'X': 0.7036759257316589, 'Y': 0.14953270554542542}]}}, {'DetectedText': 'WEAPON', 'Type': 'LINE', 'Id': 1, 'Confidence': 99.72587585449219, 'Geometry': {'BoundingBox': {'Width': 0.09527381509542465, 'Height': 0.05073431134223938, 'Left': 0.29482370615005493, 'Top': 0.11481975764036179}, 'Polygon': [{'X': 0.29482370615005493, 'Y': 0.11481975764036179}, {'X': 0.3900975286960602, 'Y': 0.11481975764036179}, {'X': 0.39084771275520325, 'Y': 0.1642189621925354}, {'X': 0.29482370615005493, 'Y': 0.16555407643318176}]}}]