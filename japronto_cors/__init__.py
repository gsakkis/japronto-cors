# -*- coding: utf-8 -*-
"""
    japronto_cors
    ~~~~
    Japronto-CORS is a simple extension to Japronto allowing you to support cross
    origin resource sharing (CORS) using a simple decorator.

    :copyright: (c) 2017 by George Sakkis (based on sanic-cors by Ashley Sommer
        and flask-cors by Cory Dolphin).
    :license: MIT, see LICENSE for more details.
"""
from .decorator import cross_origin
from .extension import CORS
from .version import __version__

__all__ = ['CORS', 'cross_origin']

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

# Set initial level to WARN. Users must manually enable logging for
# japronto_cors to see our logging.
rootlogger = logging.getLogger(__name__)
rootlogger.addHandler(NullHandler())

if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)
