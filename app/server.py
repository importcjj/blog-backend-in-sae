# -*- coding: utf-8 -*-

import hug
import logging

logger = logging.getLogger()


@hug.get(output=hug.output_format.json)
def index():
    logger.info('index')
    return {
        'index': 'index'
    }
