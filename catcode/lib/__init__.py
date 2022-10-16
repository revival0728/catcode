from . import BAS
from . import IO
from . import highlight
from . import segment
from . import seperate

config = {}

def setConfig(customConfig):
    global config
    config = customConfig
    BAS.config = customConfig
    IO.config = customConfig
    highlight.config = customConfig
    segment.config = customConfig
    seperate.config = customConfig
