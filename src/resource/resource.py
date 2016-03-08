# -*- coding: utf-8 -*-


import falcon
import error


class IndexResource:

    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        req.context['result'] = 'index'


class LoginResource:

    def __init__(self):
        pass

    def on_post(self, req, resp):
        rjson = req.context['json']
        username = rjson.get('username')
        passwd = rjson.get('passwd')
        if 'pass' not in (username, passwd):
            raise error.LoginError
        resp.body = {
            'token': '12345678'
        }


class ArticleListResource:

    def __init__(self):
        pass

    def on_get(self, req, resp):
        pass


class ArticleResource:

    def __init__(self):
        pass

    def on_get(self, req, resp, article_id):
        pass

    def on_post(self, req, resp):
        rjson = req.context['json']
        title = rjson.get('title')
        tags = rjson.get('tags')
        author = rjson.get('author')
        markdown = rjson.get('markdown')

    def on_patch(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass
