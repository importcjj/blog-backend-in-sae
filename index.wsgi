# -*- coding: utf-8 -*-

import sae
import sys
import os

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'libraries))

from app import __hug_wsgi__

application = sae.create_wsgi_app(__hug_wsgi__)
