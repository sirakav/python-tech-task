# Standart library
import os
from distutils.util import strtobool

# Flask and other third party packages
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TESTING = strtobool(os.getenv("TESTING"))
    DEBUG = strtobool(os.getenv("DEBUG"))
