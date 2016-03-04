# -*- coding: utf-8 -*-

import falcon
import json


class JOSNTranslator(object):

    def process_request(self, req, resp):
        if req.content_length in (0, None):
            return

        body = req.steam.read()
        if not body:
            raise falcon.HTT_400

        try:
            req.context['data'] = json.loads(body)
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode')

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return

        resp.body = json.dums(req.context['result'])
