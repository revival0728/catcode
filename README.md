# catcode
---
A repository that prints source code in terminal prettier

## Installation
### Linux
```
sudo python3 setup.py install
```

### Windows
```
python setup.py install
```


or install from the compressed file

## How to Use
### With Installation
```
catcode [File Name] [Language]
```

### Without Installation
```
python3 catcode.py [File Name] [Language]
```

If the `[Language]` argument is empty then it will recognize it from the file extension

## Support Language
- cpp
- python3
- javascript (beta)

## Customize Language and Color
You can edit the file `./catcode/config/config.py` to customize

Than add your customize variables to `language_list` in `./catcode/config/__init__.py`

And add the file extension to `language_extension` in `./catcode/config/__init__.py`

The argument `singleWords`, `multiWords` are important. If they are not complete, the program will be unable to work properly
