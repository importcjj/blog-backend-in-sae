# -*- coding: utf-8 -*-

import json
import error
import falcon
from .model import Session


class JOSNTranslator(object):

    def process_request(self, req, resp):
        if req.content_length in (0, None):
            return

        body = req.stream.read()
        if not body:
            raise error.EmptyRequestError

        try:
            req.context['json'] = json.loads(body)
        except (ValueError, UnicodeDecodeError):
            raise error.MalformedJsonError

    def process_response(self, req, resp, resource):
        if not resp.body:
            resp.status = falcon.HTTP_204
        else:
            resp.status = falcon.HTTP_200
            if isinstance(resp.body, (list, dict)):
                resp.body = json.dumps(resp.body)


class AuthMiddleware(object):

    def process_reqest(self, req, resp):
        token = req.get_header('x-token')
        print token
        if token not in ('12345678'):
            raise error.UnauthorizedError

    def process_response(self, req, reqsp, resource):
        pass


class ScopeSessionRemover(object):

    def process_request(self, req, resp):
        pass

    def process_response(self, req, resp, resource):
        Session.remove()
