# -*- coding: utf-8 -*-


class ArticleResource:

    def on_get(self, req, resp, id):
        pass

    def on_post(self, req, resp):
        pass

    def on_patch(self, req, resp, id):
        pass

    def on_delete(self, req, resp, id):
        pass


class ArticlesResource:

    def on_get(self, req, resp):
        pass


class LabelResource:

    def on_get(self, req, resp):
        pass

    def on_post(self, req, resp):
        pass

    def on_patch(self, req, resp):
        pass

    def on_delete(self, req, resp, id):
        pass


class ArticleLabelResource:

    def on_get(self, req, resp):
        pass


def get_article(article_id):
    pass


def create_article(**kwargs):
    pass


def udpate_article(article_id, **kwargs):
    pass


def remove_article(article_id):
    pass


def get_labels(offset=0, limit=10, status=0):
    pass


def create_label(**kwargs):
    pass


def update_label(label_id, **kwargs):
    pass


def remove_label(label_id):
    pass


def get_article_by_label(labels, offset=0, limit=10, status=0):
    pass
