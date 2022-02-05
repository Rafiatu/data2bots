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
                              "required": ["id", "nickname",
                                           "title", "accountType",
                                           "countryCode", "orientation"]
                          }
                          )

    def test_dictionary_schema_reads_empty_dict_correctly(self) -> None:
        self.assertEqual(self.extractor.read_dict(dict()),
                        {
                            "type": "OBJECT",
                            "tag": "",
                            "description": "",
                            "properties": dict(),
                            "required": []
                        }
                        )

    def test_read_array_function_does_not_return_wrong_output(self) -> None:
        self.assertNotEqual(self.extractor.read_array(),
                        {
                            "type": "ARRAY",
                            "tag": "",
                            "description": "",
                            "items": [],
                            "required": []
                        }
                        )

    def test_read_array_function_returns_expected_output(self) -> None:
        self.assertEqual(self.extractor.read_array(),
                        {
                            "type": "ARRAY",
                            "tag": "",
                            "description": "",
                            "items": dict(),
                            "required": set()
                        }
                        )

    def test_dict_reader_does_not_read_arrays(self) -> None:
        array_obj = ["id", "nickname",
                     "title", "accountType",
                     "countryCode", "orientation"]
        self.assertRaises(TypeError, self.extractor.read_dict, array_obj)

    def test_dict_reader_does_not_read_strings(self) -> None:
        self.assertRaises(TypeError, self.extractor.read_dict, "test_string")

    def tearDown(self) -> None:
        del self.extractor
