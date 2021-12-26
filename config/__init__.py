from starlette.config import Config

env_config = Config('.env')

from config.app import *
from config.db import *
