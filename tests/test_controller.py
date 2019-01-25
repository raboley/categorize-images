from .context import categorize
import os
import unittest

class controller(unittest.TestCase):
    """
    ensure that this will recognize images
    Post the json in a folder
    determine the image type (stat, main, side 1 and 2)
    extract the weapon name from the stat page
    post the weapon name and image group folder date stamp to an archive file
    move and rename the image to staging location for image cropping
    """

    def setUp(self):
        self.source_json_path = './tests/_testArtifacts/test_controller/Ruby_Crystal_Ring_Stats.json'
        self.json = categorize.find_in_json.get_json(self.source_json_path)
        self.weapon_name = categorize.get_weapon_name(self.json)
        self.character_map = './tests/_testArtifacts/test_controller/weapon_character_pairs.json'
        self.weapon_map = './tests/_testArtifacts/test_controller/__temp/folder_weapon_pairs.json'

    # Json can be gotten
    def test_can_get_json(self):
        self.json = categorize.find_in_json.get_json(self.source_json_path)
        self.assertIsNotNone(self.json)
    # Determine image type based on json
    def test_can_tell_it_is_stats_image(self):
        picture_type = categorize.determine_picture_type(self.json)
        self.assertEqual(picture_type, 'stat_screen')
    # If it is a stat screen

        # get the weapon name
    def test_can_get_weapon_name(self):
        weapon_name = categorize.get_weapon_name(self.json)
        self.assertEqual(weapon_name, 'Crystaring')

        # figure out the character name based on the weapon name
    def test_get_character_name_from_weapon_name(self):
        character_name = categorize.determine_character(self.weapon_name, self.character_map)
        self.assertEqual(character_name, 'Ruby')
        # write the weapon name to the pair file
    def test_can_write_image_weapon_pair_to_file(self):
        pair = categorize.ArchivePair(self.weapon_map)
        categorize.write_weapon_map_to_file('test_controller', self.weapon_name, pair)

        data = [{"key":'test_controller',"value":self.weapon_name}]
        self.assertEqual(data, pair.read_pair_file())
        # copy the file to the staging folder with the correct name

    def test_reads_weapon_name_from_file(self):
        pass

    def test_moves_the_file_to_staging_with_correct_name(self):
        pass

##TODO: setup a finally that always deletes the temp file created for file map thing