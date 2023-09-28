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
from lib.configs import YAML, JSON, Dictionary

def setup():
    """
    Perform initialization setup
    """
    global yaml_cfg_filename, json_cfg_filename, cs_Yaml, cs_JSON, cs_Dict
    # Initialize Variables
    yaml_cfg_filename = "data.yaml"
    json_cfg_filename = "data.json"

    # Initialize Classes
    cs_Yaml = YAML(yaml_cfg_filename)
    cs_JSON = JSON(json_cfg_filename, "w+")
    cs_Dict = Dictionary()

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

def main():
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

if __name__ == "__main__":
    setup()
    main()
