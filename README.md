from syncFunc import autoFormatfrom fileinput import filename

# SyncConfig
## 1. Structure
`main.py` is the main python code

`config.ini` is the configuration file. It consists `[section] `, ``Key`` and ``value``.
A sample configuration file looks like this:
```ini
[DEFAULT]
var1=6
var2=2
var3=9

```

`syncFunc.py` is the functions to use. See [2.1](#2.1-import-function) for instruction to use and function description

`config.m` uses the functions in `IniConfig.m` which is a class shared on MATLAB file exchange platform. Variables can be changed in `config.m` and be saved to the `config.ini` file


## 2. To Use
### 2.1 Import function
 to import functions, just simply use
```python
import syncFunc
```
### 2.2 use function

to use function, do:

```python
import syncFunc

syncFunc.autoFormat(description, var)
syncFunc.ini_config()
syncFunc.read_config(filename=filename, section=section, key=key, verbose=False)
```

### 2.3 function description
#### autoFormat

```python
def autoFormat(description: {__add__},
               var: {__len__}) -> A
```
Input: description `string`, var `list`

Output: new_var `string`


#### readConfig
```python
def read_config(filename: Any,
                section: Any,
                key: Any,
                verbose: bool = False) -> str

```

**Input:** filename `string`, section `Any`

**Output:** value `str`
