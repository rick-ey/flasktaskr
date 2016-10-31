
import os

# grab the folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'rM\xb1\xdc\x12o\xd6i\xff+9$T\x8e\xec\x00\x13\x82.*\x16TG\xbd'

# define the full path for hte database
DATABASE_PATH = os.path.join(basedir, DATABASE)
