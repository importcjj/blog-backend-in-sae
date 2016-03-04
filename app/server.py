# -*- coding: utf-8 -*-

import falcon
import logging
from .middlewares import JOSNTranslator

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Index:

    def on_get(self, req, resp):
        logger.info('logger')
        resp.status = falcon.HTTP_200
        resp.context['result'] = {
            'mame': 'falcon',
            'version': '0.3.0'
        }

app = falcon.API(
    middleware=[JOSNTranslator()]
)

index = Index()

app.add_route('/index', index)
app.add_route('/', index)
