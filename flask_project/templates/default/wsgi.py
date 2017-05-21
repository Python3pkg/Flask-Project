# coding=utf-8


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from web_site import create_app

app = create_app(os.getenv('SYSTEM_CONFIG') or 'production')
