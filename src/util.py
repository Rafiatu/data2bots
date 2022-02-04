from ordered_set import OrderedSet
from typing import List


class Util:
    """
        Handles all schema extraction of all data types.
    """
    @staticmethod
    def read_dict(data: dict) -> dict[str, str, str, dict, List]:
        """
            Extracts the schema for dictionaries / json objects.
                Parameters:
                    data (dict): dictionary containing schema objects to be decoded.
                Returns:
                    dictionary_schema (dict): schema for the json object or python dictionary.
        """
        return {
            "type": "OBJECT",
            "tag": "",
            "description": "",
            "properties": dict(),
            "required": list(data.keys())
        }

    @staticmethod
    def read_array() -> dict[str, str, str, dict, List]:
        """
            Extracts the schema for array of json objects.
                Returns:
                    array_schema (dict): schema for array of json objects returned as a python dictionary.
        """
        return {
            "type": "ARRAY",
            "tag": "",
            "description": "",
            "items": dict(),
            "required": OrderedSet()
        }

    @staticmethod
    def read_string() -> dict[str, str, str]:
        """
            Extracts the schema for strings.
                Returns:
                    string_schema (dict): schema for json strings returned as a python dictionary.
        """
        return {
            "type": "STRING",
            "tag": "",
            "description": ""
        }

    @staticmethod
    def read_integer() -> dict[str, str, str]:
        """
            Extracts the schema for integers.
                Returns:
                    integer_schema (dict): schema for json integers returned as a python dictionary.
        """
        return {
            "type": "INTEGER",
            "tag": "",
            "description": ""
        }

    @staticmethod
    def read_boolean() -> dict[str, str, str]:
        """
            Extracts the schema for boolean values.
                Returns:
                    bool_schema (dict): schema for boolean values returned as a python dictionary.
        """
        return {
            "type": "BOOLEAN",
            "tag": "",
            "description": ""
        }
    
    @staticmethod
    def read_float() -> dict[str, str, str]:
        """
            Extracts the schema for float numbers.
                Returns:
                    float_schema (dict): schema for floats returned as a python dictionary.
        """
        return {
            "type": "NUMBER",
            "tag": "",
            "description": ""
        }

    @staticmethod
    def read_enum() -> dict[str, str, str]:
        """
            Extracts the schema for array of strings.
                Returns:
                    enum_schema (dict): schema for array of strings returned as a python dictionary.
        """
        return {
            "type": "ENUM",
            "tag": "",
            "description": ""
        }
