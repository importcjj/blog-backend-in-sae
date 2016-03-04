# -*- coding: utf-8 -*-

import sae
import sys
import os

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'libraries'))

from app import app

application = sae.create_wsgi_app(app)
