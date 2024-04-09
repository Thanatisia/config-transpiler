"""
Configuration File Library
"""
import os
import sys
import json
import tomllib
import toml

## External Libraries
from ruamel.yaml import YAML
from ruamel.yaml.main import round_trip_dump as yaml_dump

## Get system information
version_major = sys.version_info.major
version_minor = sys.version_info.minor

class Configuration:
    """
    Configuration class
    """
    def __init__(self, file_name, file_type, mode="r"):
        self.file_name = file_name
        self.file_type = file_type
        self.open_mode = mode
        self.cfg_file = None

    def open_file(self):
        """
        Open File for use
        """
        # Check if file exists
        file_Exists = self.verify_exists(self.file_name)

        # Check if file is opened
        file_Open = self.verify_open(self.file_name)

        if (file_Exists == True) and (file_Open == False):
            self.cfg_file = open(self.file_name, self.open_mode)

    def close_file(self):
        """
        Close file after usage
        """
        # Check if Configuration file is opened
        if self.cfg_file != None:
            # Configuration file is opened
            # Close file after usage
            self.cfg_file.close()

            # Set configuration file object to empty
            self.cfg_file = None

    def verify_open(self, target_fname):
        """
        Check if specified file is opened
        """
        is_open = False
        # Check if file name is set and if configuration file object is not empty
        if (self.file_name == target_fname) and (self.cfg_file != None):
            is_open = True
        return is_open

    def verify_exists(self, target_fname):
        """
        Check if specified file exists
        """
        file_exists = False
        if os.path.isfile(target_fname):
            file_exists = True
        return file_exists

class YAMLConfig(Configuration):
    """
    YAML Configuration File Handler
    inheriting the configuration file class
    """
    def __init__(self, file_name, mode="r"):
        """
        Class constructor
        """
        ## To keep the inheritance of the parent's __init__() function
        super(YAMLConfig, self).__init__(file_name, "yaml", mode)
        self.configuration = Configuration

        # Initialize Classes
        self.yaml = YAML()

        # Set properties
        self.set_filename(file_name)
        self.set_mode(mode)

        # Initialize Variables
        self.file = None

    def set_filename(self, file_name):
        """
        Explicitly set file name
        """
        self.file_name = file_name

    def set_mode(self, mode):
        """
        Explicitly specify mode to use
        """
        self.mode = mode

    def open_file(self):
        """
        Open file and import file
        """
        # Open file for use
        self.file = open(self.file_name, self.mode)

    def close_file(self):
        """
        Close file after usage and set empty file object
        """
        # Check if file is opened
        if self.file != None:
            # Close file after use
            self.file.close()
            self.file = None

    def convert_dict_to_yaml(self, data):
        """
        Convert a dictionary object to YAML file

        :: Params
        - data : The dictionary object you wish to convert
            Type: Dictionary
        """
        return self.yaml.dump(data)

    def write_config(self, data):
        """
        Dump and write dictionary object to YAML configuration file
        """
        print("Data: {}, Type: {}".format(data, type(data)))
        # Check if data is not empty and file is opened
        if (data != None) and (self.file != None):
            # Dump the data
            self.yaml.dump(data, self.file)

    def read_config(self):
        """
        Load and read YAML configuration file contents to dictionary
        """
        file = self.file

        # Check if file is opened
        if (file == None):
            # Open file if not opened
            file = open(self.file_name)

        return self.yaml.load(file)

    def parse_yaml_str_to_dict(self, yaml_str):
        """
        Parse YAML strings into dictionary object
        """
        if yaml_str != "":
            return self.yaml.load(yaml_str)


class TOMLConfig(Configuration):
    """
    TOML Configuration File 
    inheriting the configuration file class
    """
    def __init__(self, file_name, mode="r"):
        """
        Constructor
        """
        ## To keep the inheritance of the parent's __init__() function
        super(TOMLConfig, self).__init__(file_name, "toml", mode)

        # Initialize Variables
        self.configuration = Configuration

        # Initialize Classes

        # Set properties
        self.set_filename(file_name)
        self.set_mode(mode)

        # Initialize Variables
        self.file = None

    def set_filename(self, file_name):
        """
        Explicitly set file name
        """
        self.file_name = file_name

    def set_mode(self, mode):
        """
        Explicitly specify mode to use
        """
        self.mode = mode

    def open_file(self):
        """
        Open file and import file
        """
        # Open file for use
        self.file = open(self.file_name, self.mode)

    def close_file(self):
        """
        Close file after usage and set empty file object
        """
        # Check if file is opened
        if self.file != None:
            # Close file after use
            self.file.close()
            self.file = None

    def convert_dict_to_toml(self, data):
        """
        Convert a dictionary object to TOML file

        :: Params
        - data : The dictionary object you wish to convert
            Type: Dictionary
        """
        return toml.dumps(data)

    def write_config(self, data):
        """
        Dump and write dictionary object to TOML configuration file
        """
        print("Data: {}, Type: {}".format(data, type(data)))
        # Check if data is not empty and file is opened
        if (data != None) and (self.file != None):
            # Dump the data
            toml.dump(data, self.file)

    def read_config(self):
        """
        Load and read TOML configuration file contents to dictionary
        """
        # Initialize Variables
        results = {}
        file = self.file

        # Check if file is opened
        if (file == None):
            # Open file if not opened
            file = open(self.file_name)

        # Read contents
        file_contents = file.read()

        # Load the TOML file contents into dictionary
        results = tomllib.loads(file_contents)

        # Return
        return results

    def parse_toml_str_to_dict(self, toml_str):
        """
        Parse TOML strings into dictionary object
        """
        if toml_str != "":
            return tomllib.loads(toml_str)

class JSONConfig(Configuration):
    """
    JSON Configuration File 
    inheriting the configuration file class
    """
    def __init__(self, file_name, mode="r"):
        """
        Constructor
        """
        ## To keep the inheritance of the parent's __init__() function
        super(JSONConfig, self).__init__(file_name, "json", mode)

        # Initialize Variables
        self.configuration = Configuration
        self.set_filename(file_name)
        self.set_mode(mode)
        self.file = None

    def set_filename(self, file_name):
        """
        Explicitly set file name
        """
        self.file_name = file_name

    def set_mode(self, mode):
        """
        Explicitly specify mode to use
        """
        self.mode = mode

    def open_file(self):
        """
        Open file and import file
        """
        # Open file for use
        self.file = open(self.file_name, self.mode)

    def close_file(self):
        """
        Close file after usage and set empty file object
        """
        # Check if file is opened
        if self.file != None:
            # Close file after use
            self.file.close()
            self.file = None

    def write_config(self, data):
        """
        Dump and write dictionary object to JSON configuration file
        """
        # Check if data is not empty and file is opened
        if (data != None) and (self.file != None):
            # Dump the data
            json.dump(data, self.file, indent=4)

    def read_config(self):
        """
        Load and read JSON configuration file contents to dictionary
        """
        file = self.file

        # Check if file is opened
        if (file == None):
            # Open file if not opened
            file = open(self.file_name)

        return json.load(file)

    def parse_json_str_to_dict(self, json_str):
        """
        Parse JSON strings into dictionary object
        """
        if json_str != "":
            return json.load(json_str)

class Dictionary():
    """
    Configuration file dictionary
    """
    def get_Value(self, config_dict, keys=None):
        """
        Dive into the dictionary according to a specified key and obtain the value

        :: Parameters
        config_dict : Dictionary from the imported configuration contents
            Type: Dictionary

        keys : List of all nested keys; Note keys must be placed in consecutive index as per the nested structure
            Type: List
        """
        retrieved_Value = None

        if keys != None:
            for i in range(len(keys)):
                # Get current key
                curr_Key = keys[i]
                print("Current Key : {}".format(curr_Key))

                # Get current value
                retrieved_Value = config_dict[curr_Key]
            
        # Check if value is returned
        if retrieved_Value == None:
            retrieved_Value = config_dict

        return retrieved_Value

