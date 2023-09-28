# Configuration file transpiler in Python

## Information
### Background
```
YAML <=> TOML <=> JSON Configuration file converter/transpiler
```

## Setup
### Dependencies
- yaml
    + ruamel.yaml : YAML parser
- toml
    - Python version >= 3.11
        + tomllib : TOML parser; Built-in
    - Python version < 3.11
        + tomli : TOML parser - Read only
        + tomli-w : TOML parser writer - Write-only counterpart to tomli
- JSON
    + json : JSON parser; Built-in

### Pre-Requisites
- (Optional; Recommended) Create virtual environment
    - Install package dependencies
        + virtualenv / venv
    - Create Virtual Environment
        ```console
        python -m venv env
        ```
    - Source and enter into the virtual environment
        - In Linux
            ```console
            . env/bin/activate
            ```
        - In Windows
            ```console
            env\Scripts\activate
            ```

- Install python-pypi requirements
    ```console
    python -m pip install -Ur requirements.txt
    ```

## Documentations

## Resources

## References

## Remarks

