"""
Multi-configuration file type transpiler

[File Type Support]
- yaml
- toml
- json
"""
## Built-in Libraries
import os
import sys

## External Libraries
import lib.configs as configs
from lib.configs import TOMLConfig, YAMLConfig, JSONConfig, Dictionary

def setup():
    """
    Perform initialization setup
    """
    global toml_cfg_filename, yaml_cfg_filename, json_cfg_filename, cs_Toml, cs_Yaml, cs_JSON, cs_Dict
    # Initialize Variables
    yaml_cfg_filename = "data.yaml"
    json_cfg_filename = "data.json"
    toml_cfg_filename = "data.toml"

    # Initialize Classes
    cs_Toml = TOMLConfig(toml_cfg_filename)
    cs_Yaml = YAMLConfig(yaml_cfg_filename)
    cs_JSON = JSONConfig(json_cfg_filename)
    cs_Dict = Dictionary()

def print_toml(toml_Contents):
    # Binary Tree Dictionary
    if toml_Contents != None:
        for k,v in toml_Contents.items():
            print("{} => {}".format(k,v))
            key_Type = type(k)
            value_Type = type(v)
            if value_Type == list:
                for i in range(len(v)):
                    # Get current item
                    v_Item = v[i]

                    print("\t{}. {}".format(i, v_Item))
            elif value_Type == dict:
                for k,v in v.items():
                    print("\t{}".format(v))

def print_yaml(yaml_Contents):
    # Binary Tree Dictionary
    if yaml_Contents != None:
        for k,v in yaml_Contents.items():
            print("{} => {}".format(k,v))
            key_Type = type(k)
            value_Type = type(v)
            if value_Type == list:
                for i in range(len(v)):
                    # Get current item
                    v_Item = v[i]

                    print("\t{}. {}".format(i, v_Item))
            elif value_Type == dict:
                for k,v in v.items():
                    print("\t{}".format(v))

"""
TOML
"""
def convert_toml_to_json():
    """
    Open, read, print and close TOML configuration file
    """
    print("===================================")
    print(" Converting TOML file [{}] => [{}] ".format(toml_cfg_filename, json_cfg_filename))
    print("===================================")

    print("")

    print("Reading TOML Configuration file...")
    cs_Toml.open_file()
    toml_Contents = cs_Toml.read_config()
    cs_Toml.close_file()

    # Print YAML contents
    print_toml(toml_Contents)

    print("")

    """
    Take TOML config file and output as JSON
    """
    print("Writing Dictionary object to JSON file...")
    # Open file and write the dictionary object to JSON
    cs_JSON.set_mode("w+")
    cs_JSON.open_file()
    cs_JSON.write_config(toml_Contents)
    # Close file after usage
    cs_JSON.close_file()

    print("")

    print("(+) Successfully converted TOML file [{}] => JSON file [{}]".format(toml_cfg_filename, json_cfg_filename))

    print("")

    print("Reading newly created JSON file...")
    # Set file to read and open file and read contents
    cs_JSON.set_mode("r")
    cs_JSON.open_file()
    json_Contents = cs_JSON.read_config()
    # Close file after usage
    cs_JSON.close_file()

    # Print JSON contents
    print(json_Contents)

def convert_json_to_toml():
    """
    Open, read, print and close JSON configuration file
    """
    print("===================================")
    print(" Converting JSON file [{}] => [{}] ".format(json_cfg_filename, toml_cfg_filename))
    print("===================================")

    print("")

    print("Reading JSON Configuration file...")
    cs_JSON.open_file()
    json_Contents = cs_JSON.read_config()
    # Close file after usage
    cs_JSON.close_file()

    # Print TOML contents
    print_toml(json_Contents)

    print("")

    """
    Take JSON config file and output as TOML
    """
    print("Writing Dictionary object to TOML file...")
    # Set new file name
    cs_Toml.set_filename("data2.toml")
    # Set file write mode to Write+Read
    cs_Toml.set_mode("w+")
    # Open file and write the dictionary object to JSON
    cs_Toml.open_file()
    cs_Toml.write_config(json_Contents)
    # Close file after usage
    cs_Toml.close_file()

    print("")

    print("(+) Successfully converted JSON file [{}] => TOML file [{}]".format(json_cfg_filename, "data2.toml"))

    print("")

    print("Reading newly created TOML file...")
    # Set new file name
    cs_Toml.set_filename("data2.toml")
    # Set file to read and open file and read contents
    cs_Toml.set_mode("r")
    # Open file and write the dictionary object to JSON
    cs_Toml.open_file()
    toml_Contents = cs_Toml.read_config()
    # Close file after usage
    cs_Toml.close_file()

    # Print JSON contents
    print(toml_Contents)

"""
YAML
"""
def convert_yaml_to_json():
    """
    Open, read, print and close YAML configuration file
    """
    print("===================================")
    print(" Converting YAML file [{}] => [{}] ".format(yaml_cfg_filename, json_cfg_filename))
    print("===================================")

    print("")

    print("Reading YAML Configuration file...")
    cs_Yaml.open_file()
    yaml_Contents = cs_Yaml.read_config()
    cs_Yaml.close_file()

    # Print YAML contents
    print_yaml(yaml_Contents)

    print("")

    """
    Take YAML config file and output as JSON
    """
    print("Writing Dictionary object to JSON file...")
    # Open file and write the dictionary object to JSON
    cs_JSON.set_mode("w+")
    cs_JSON.open_file()
    cs_JSON.write_config(yaml_Contents)
    # Close file after usage
    cs_Yaml.close_file()

    print("")

    print("(+) Successfully converted YAML file [{}] => JSON file [{}]".format(yaml_cfg_filename, json_cfg_filename))

    print("")

    print("Reading newly created JSON file...")
    # Set file to read and open file and read contents
    cs_JSON.set_mode("r")
    cs_JSON.open_file()
    json_Contents = cs_JSON.read_config()
    # Close file after usage
    cs_Yaml.close_file()

    # Print JSON contents
    print(json_Contents)

def convert_json_to_yaml():
    """
    Open, read, print and close JSON configuration file
    """
    print("===================================")
    print(" Converting JSON file [{}] => [{}] ".format(json_cfg_filename, yaml_cfg_filename))
    print("===================================")

    print("")

    print("Reading JSON Configuration file...")
    cs_JSON.open_file()
    json_Contents = cs_JSON.read_config()
    # Close file after usage
    cs_JSON.close_file()

    # Print YAML contents
    print_yaml(json_Contents)

    print("")

    """
    Take JSON config file and output as YAML
    """
    print("Writing Dictionary object to YAML file...")
    # Set new file name
    cs_Yaml.set_filename("data2.yaml")
    # Set file write mode to Write+Read
    cs_Yaml.set_mode("w+")
    # Open file and write the dictionary object to JSON
    cs_Yaml.open_file()
    cs_Yaml.write_config(json_Contents)
    # Close file after usage
    cs_Yaml.close_file()

    print("")

    print("(+) Successfully converted JSON file [{}] => YAML file [{}]".format(json_cfg_filename, yaml_cfg_filename))

    print("")

    print("Reading newly created YAML file...")
    # Set new file name
    cs_Yaml.set_filename("data2.yaml")
    # Set file to read and open file and read contents
    cs_Yaml.set_mode("r")
    # Open file and write the dictionary object to JSON
    cs_Yaml.open_file()
    yaml_Contents = cs_Yaml.read_config()
    # Close file after usage
    cs_Yaml.close_file()

    # Print JSON contents
    print(yaml_Contents)

def main():
    convert_yaml_to_json()
    convert_json_to_yaml()
    convert_json_to_toml()
    convert_toml_to_json()

if __name__ == "__main__":
    setup()
    main()
