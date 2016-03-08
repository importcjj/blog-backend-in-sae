# -*- coding: utf-8 -*-

import falcon


def error_serializer(req, ex):
    return 'application/json', '{"code": "%s", "message":"%s"}' % (ex.title, ex.description)

UnauthorizedError = falcon.HTTPError(
    falcon.HTTP_401, 'UNAUTHORIZED', 'user unauthorized.')
LoginError = falcon.HTTPError(
    falcon.HTTP_200, 'LOGIN_FAILED', 'login failed.')
EmptyRequestError = falcon.HTTPError(
    falcon.HTTP_400, 'EMPTY_REQUEST', 'empty request body.')
MalformedJsonError = falcon.HTTPError(
    falcon.HTTP_400, 'MALFORMED_JSON', 'malformed json.'
)
