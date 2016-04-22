#!/usr/bin/env python
# -*- coding: utf-8 -*-

import celery

BROKER_URL = 'redis://127.0.0.1/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1/1'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
        'test-every-seconds': {
            'task': 'worker.test',
            'schedule': timedelta(seconds=1),
            'args': (['lijin09'])
            },
        'test-every-2-seconds': {
            'task': 'worker.test',
            'schedule': timedelta(seconds=2),
            'args': (['ligeng01'])
            },
        }
