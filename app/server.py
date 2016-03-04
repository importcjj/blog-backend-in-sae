# -*- coding: utf-8 -*-

import falcon
import logging


logger = logging.getLogger(__name__)


class Index:

    def on_get(self, req, resp):
        logger.info('logger')
        resp.status = falcon.HTTP_200
        resp.body = ('hello falcon!')

app = falcon.API()

index = Index()

app.add_route('/index', index)
app.add_route('/', index)
