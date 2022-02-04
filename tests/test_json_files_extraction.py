import json
import os
from src.decoder import Schema
from unittest import TestCase


class TestUtils(TestCase):
    def setUp(self) -> None:
        self.schema = Schema()
        self.output_file = open("examples/example_output.json", "r")

    def test_json_schema_is_properly_extracted(self) -> None:
        objects = {
            "battleType": "ABCDEFGHIJKLMN",
            "wagerType": "ABCDEFGHIJKLMNOPQRSTUVW",
            "countdown": 60,
            "duration": 120,
            "users": [
                {
                    "id": 1015,
                    "nickname": "Rafi",
                    "title": "Python Developer",
                    "accountType": "Basic",
                    "countryCode": "NG",
                    "orientation": False
                },
                {
                    "id": "213456ujhgfvcxasgs76w87e9rtughvb221",
                    "nickname": "JSON",
                    "title": "Assessment",
                    "accountType": "Premium",
                    "countryCode": "LT",
                    "orientation": True
                }
            ]
        }
        expected_answer = {
            'battleType': {'description': '', 'tag': '', 'type': 'STRING'},
            'countdown': {'description': '', 'tag': '', 'type': 'INTEGER'},
            'duration': {'description': '', 'tag': '', 'type': 'INTEGER'},
            'users': {'description': '', 'tag': '', 'type': 'ARRAY',
                      'items': {'accountType': {'description': '',
                                                'tag': '',
                                                'type': 'STRING'},
                                'countryCode': {'description': '',
                                                'tag': '',
                                                'type': 'STRING'},
                                'id': {'description': '', 'tag': '', 'type': 'STRING'},
                                'nickname': {'description': '',
                                             'tag': '',
                                             'type': 'STRING'},
                                'orientation': {'description': '',
                                                'tag': '',
                                                'type': 'BOOLEAN'},
                                'title': {'description': '', 'tag': '', 'type': 'STRING'}},
                      'required': ['id',
                                   'nickname',
                                   'title',
                                   'accountType',
                                   'countryCode',
                                   'orientation'],
                      },
            'wagerType': {'description': '', 'tag': '', 'type': 'STRING'}}

        self.assertEqual(self.schema.read_schema(objects), expected_answer)

    def test_json_file_is_read_properly_and_returns_correct_schema(self) -> None:
        self.assertEqual(
            self.schema.extract_from_file("examples/example_input.json"),
            json.load(self.output_file)
        )
        self.assertTrue(os.path.exists("schema/example_input.json"))

    def test_wrong_file_path_raises_appropriate_error(self) -> None:
        self.assertIsNone(self.schema.extract_from_file("wrong_path/file.json"))

    def test_that_no_schema_is_extracted_if_there_is_no_message_in_the_object(self):
        self.assertIsNone(self.schema.extract_from_file("tests/data_for_test.json"))

    def test_that_schemas_are_properly_saved_into_files(self) -> None:
        schema = {
            "type": "OBJECT",
            "tag": "",
            "description": "",
            "properties": {
                "name": {
                    "type": "STRING",
                    "tag": "",
                    "description": ""
                },
                "iconId": {
                    "type": "STRING",
                    "tag": "",
                    "description": ""
                }
            },
            "required": [
                "name",
                "iconId"
            ]
        }
        self.schema.save_schema("output.json", schema)
        self.assertTrue(os.path.exists("schema/output.json"))

    def tearDown(self) -> None:
        if os.path.exists("schema/example_input.json"):
            os.remove("schema/example_input.json")
        if os.path.exists("schema/output.json"):
            os.remove("schema/output.json")
        del self.schema
        self.output_file.close()
