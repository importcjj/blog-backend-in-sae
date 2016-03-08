# -*- coding: utf-8 -*-

import falcon
import logging
from .middlewares import (
    JOSNTranslator,
    AuthMiddleware,
    ScopeSessionRemover
)
from .resource import (
    IndexResource,
    LoginResource
)
from .error import error_serializer

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)


app = falcon.API(middleware=[
    JOSNTranslator(),
    AuthMiddleware(),
    # remove scope session in the last
    ScopeSessionRemover(),
])

app.set_error_serializer(error_serializer)

index = IndexResource()
login = LoginResource()

app.add_route('/index', index)
app.add_route('/', index)
app.add_route('/login', login)
