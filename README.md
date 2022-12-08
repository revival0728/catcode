<div align="center">

# catcode

[![revival0728 - catcode](https://img.shields.io/badge/revival0728-catcode-2ea44f?logo=github)](https://github.com/revival0728/catcode)
[![tag - v1.0.0](https://img.shields.io/badge/tag-v1.0.0-2ea44f)](https://github.com/revival0728/catcode/tree/v1.0.0)
[![License - MIT](https://img.shields.io/badge/License-MIT-2ea44f)](https://github.com/revival0728/catcode/blob/master/LICENSE)
[![Python - >=3.9](https://img.shields.io/badge/Python->=3.9-2ea44f?logo=python)](https://github.com/revival0728/catcode/blob/master/LICENSE)

</div>

---

## Overview
A repository that prints source code in terminal prettier

![preview1](https://i.imgur.com/h8hNC13.png)

## Installation
First clone repository from github or download sources from release

then run the following command
### Linux
```
sudo python3 setup.py install
```

### Windows
```
python setup.py install
```

## How to Use
### With Installation
```
catcode [File Name] [--name] [--icon] [--flx[Langauge Name]]
```

### Without Installation
```
python3 catcode.py [File Name] [--name] [--icon] [--flx[Langauge Name]]
```

## Support Language
- cpp
- python3
- javascript (beta)

## Customize Language and Color
The customization must be done before the installation for now.

### Step 1
Copy the `empty_config.py` file and rename it to `[language name]_config.py`

### Step 2
Edit the content of the file

### Step 3
Add the following code to the `config.py`

```python
from .default_config import DEFAULT
from .cpp_config import cpp
from .python3_config import python3
from .javascript_config import javascript
from .[langauge name]_config import [language name]     # modified

class Export:
    def language_config(self) -> dict:
        return {
            'cpp': cpp,
            'python3': python3,
            'javascript': javascript,
            'DEFAULT': DEFAULT,
            '[language name]': [language name],     # modified
        }

    ...
```