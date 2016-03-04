# -*- coding: utf-8 -*-

import sae
from app import __hug_wsgi__

application = sae.create_wsgi_app(__hug_wsgi__)
