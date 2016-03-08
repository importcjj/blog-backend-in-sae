# -*- coding: utf-8 -*-


from app import app
from wsgiref.simple_server import make_server


server = make_server('', 5000, app)
server.serve_forever()
