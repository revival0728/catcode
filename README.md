# catcode
---
A repository that prints source code in terminal prettier

## How to Use
You can add the repository path to environment variables which is `Path` and enter the following command
```
$ python3 catcode.py [FileName] [Language]
```
Or compile the python file to exe file

The later one will be more convenient

If the `[Language]` argument is empty then it will recognize it from the file extension

## Support Language
- cpp
- python3

## Customize Language and Color
You can edit the file `./config/config.py` to customize

Than add your customize variables to `language_list` in `./config/__init__.py`

And add the file extension to `language_extension` in `./config/__init__.py`

The argument `singleWords`, `multiWords` are important. If they are not complete, the program will be unable to work properly
