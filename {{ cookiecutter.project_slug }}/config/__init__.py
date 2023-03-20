import pathlib

import environ

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
)

env.read_env(str(BASE_DIR / '.env'))
