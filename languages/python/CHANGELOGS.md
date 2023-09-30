# CHANGELOGS

## Table of Contents
> version | date        time | status
+ v0.1.0  | 2023-09-28 0846H | Pushed to main
+ v0.2.0  | 2023-09-30 1104H | Development; Testing

## Entries
### v0.1.0
- New
    + Created project source code filesystem for python
    + Created configuration file handler library in 'lib/config.py'
    + Added dependency: python package 'pyyaml' for YAML file management
- Updates
    + Changed dependency: python package 'pyyaml' => 'ruamel.yaml'

### v0.2.0
- Updates
    - Additions
        + Added function 'convert_json_to_yaml()' corresponding to the yaml to json alternative
    - Moved
        + Moved the lines in main into a standalone function 'convert_yaml_to_json()'
    - Renames
        + Renamed 'YAML', 'TOML' and 'JSON' classes into 'YAMLConfig', 'TOMLConfig', and 'JSONConfig' class respectively
    - Removal
        + Removed the 'as yaml' label when importing YAML, and initialized 'yaml' as class variable in the YAMLConfigs class instead
    - Fixes
        + Fixed bug where dumping of Dictionary Object via '.write_config()' will throw an error

