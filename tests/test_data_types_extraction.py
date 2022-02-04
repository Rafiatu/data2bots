from src.util import Util
from unittest import TestCase


class TestUtils(TestCase):
    def setUp(self) -> None:
        self.extractor = Util

    def test_dictionary_schema_is_properly_extracted(self) -> None:
        object = {
            "id": 1015,
            "nickname": "Rafi",
            "title": "Python Developer",
            "accountType": "Basic",
            "countryCode": "NG",
            "orientation": False
        }
        self.assertEqual(self.extractor.read_dict(object),
                          {
                              "type": "OBJECT",
                              "tag": "",
                              "description": "",
                              "properties": dict(),
                              "required": ["id", "nickname", "title", "accountType", "countryCode", "orientation"]
                          }
                          )

    def test_dictionary_schema_reads_empty_dict_correctly(self) -> None:
        self.assertTrue(self.extractor.read_dict(dict()),
                        {
                            "type": "OBJECT",
                            "tag": "",
                            "description": "",
                            "properties": dict(),
                            "required": []
                        }
                        )

    def tearDown(self) -> None:
        del self.extractor
