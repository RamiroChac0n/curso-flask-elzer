import os
from os.path import join, dirname
from dotenv import load_dotenv
import datetime 

# Configuracion base
class base_config():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path, override=True)

    # JWT
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = SECRET_KEY

    #SQLAlchemy
    SQLALCHEMY_DATABASE_URI = ''

    SQLALCHEMY_TRACK_MODIFICATION = False

    SQLALCHEMY_POOL_RECYCLE = 5
    SQLALCHEMY_POOL_PRE_PING = True

# Configuracion para developer
class developer_config(base_config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

# Configuracion para testing
class testing_config(base_config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')

# Configuracion para produccion
class production_config(base_config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI') 