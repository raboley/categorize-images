import unittest
import json
from .context import categorize
from testfixtures import tempdir, compare

import os

client = categorize

class test_image_text_decider(unittest.TestCase):
    """
    Ensure if something is a stat screen, it takes the appropriate actions
    """
    def test_is_weapon_stat_screen(self):
        self.assertEqual(client.determine_picture_type(stat_screen_json),'stat_screen')

    # def test_weapon_name_gets_set(self):
    #     self.assertEqual(client.get_weapon_name(stat_screen_json),'Choora')

    def test_add_weapon_name_tag_combo_to_archive(self):
        pass


    @tempdir()
    def test_function(self, dir):
        dir.write('test.txt', b'some foo thing')
        foo2bar(dir.path, 'test.txt')
        compare(dir.read('test.txt'), b'some bar thing')

def foo2bar(dirpath, filename):
  path = os.path.join(dirpath, filename)
  with open(path, 'rb') as input:
      data = input.read()
  data = data.replace(b'foo', b'bar')
  with open(path, 'wb') as output:
      output.write(data)


stat_screen_json = [{'DetectedText': 'ATTACHMENT', 'Type': 'LINE', 'Id': 0, 'Confidence': 99.18334197998047, 'Geometry': {'BoundingBox': {'Width': 0.08702175319194794, 'Height': 0.04405874386429787, 'Left': 0.7036759257316589, 'Top': 0.10547396540641785}, 'Polygon': [{'X': 0.7036759257316589, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.14953270554542542}, {'X': 0.7036759257316589, 'Y': 0.14953270554542542}]}}, {'DetectedText': 'WEAPON', 'Type': 'LINE', 'Id': 1, 'Confidence': 99.72587585449219, 'Geometry': {'BoundingBox': {'Width': 0.09527381509542465, 'Height': 0.05073431134223938, 'Left': 0.29482370615005493, 'Top': 0.11481975764036179}, 'Polygon': [{'X': 0.29482370615005493, 'Y': 0.11481975764036179}, {'X': 0.3900975286960602, 'Y': 0.11481975764036179}, {'X': 0.39084771275520325, 'Y': 0.1642189621925354}, {'X': 0.29482370615005493, 'Y': 0.16555407643318176}]}}]