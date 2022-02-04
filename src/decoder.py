import json
import re
from .util import Util


class Schema:
    """
    Handles schema extraction from JSON objects.
    """

    def __init__(self) -> None:
        self.__main_schema = dict()

    def extract_from_file(self, json_file_path: str) -> dict or None:
        """
            Reads content from json file and returns the schema of the message object if present in the json object.
                Parameters:
                    json_file_path (str): path to the json file that contains the message object to be decoded.

                Returns:
                    schema (dict): The schema of the message object presented in python dictionary.
        """
        try:
            with open(json_file_path, "r") as file:
                objects = json.load(file)
            if "message" not in objects:
                print("No message found in the json object. Process exited.")
                return None
            message = objects.get("message")
            schema = self.read_schema(message)
            self.save_schema(json_file_path, schema)
            return schema
        except (ValueError, FileNotFoundError, TypeError) as error:
            print(error,
                  f"""We encountered a problem when trying to read the schema from {json_file_path}. 
                  Either you entered an incorrect file path or the file is not a json file.""")

    def read_schema(self, message: dict) -> dict:
        """
            Extracts all schema from the message object present in the json / dictionary
                Parameters:
                    message (dict): dictionary containing the data whose schema should be extracted.

                Returns:
                    main_schema (dict): The schema decoded from the message dictionary presented in a python dictionary.
        """
        try:
            for key, value in message.items():
                if type(value) == str:
                    self.__main_schema[key] = Util.read_string()

                elif type(value) == int:
                    self.__main_schema[key] = Util.read_integer()

                elif type(value) == float:
                    self.__main_schema[key] = Util.read_float()

                elif type(value) == bool:
                    self.__main_schema[key] = Util.read_boolean()

                elif type(value) == dict:
                    self.__main_schema[key] = Util.read_dict(value)
                    # read the schema from the inner dictionary
                    self.__main_schema[key]["properties"] = Schema().read_schema(value)

                elif type(value) == list:
                    if all(isinstance(item, str) for item in value):
                        # if all the items in the list are of type string, return the type as `ENUM`
                        self.__main_schema[key] = Util.read_enum()

                    else:
                        self.__main_schema[key] = Util.read_array()
                        for inner_dict in value:
                            # for each dict in the list, add the keys of that dict to the set of `required` field.
                            self.__main_schema[key]["required"].update(inner_dict.keys())
                            # for each dict in the list, add the schema of that dict to the `items` field.
                            self.__main_schema[key]["items"].update(Schema().read_schema(inner_dict))
                        # convert `required` from an Ordered Set to a list
                        self.__main_schema[key]["required"] = list(self.__main_schema[key]["required"])

            return self.__main_schema
        except Exception as error:
            raise error

    def save_schema(self, file_path: str, schema: dict) -> None:
        """
            Saves the extracted schema into a json file.
                Parameters:
                    file_path (str): path to json file where the schema data was gotten from.
                    Determines the name of the file the schema would be saved into.
                    schema (dict): schema to be saved into json file.

                Returns:
                    None: Simply saves the schema into a relevant file in the schema folder.
        """
        output_path = re.sub(r"\w+[/]", "", file_path)  # remove the current folder name from file if present
        output_path = f"schema/{output_path}"  # specify `schema` as folder for the output file path.
        with open(output_path, "w") as file:
            json.dump(schema, file, indent=3)
        print(f"The json schema for {file_path} is now available in {output_path}")
