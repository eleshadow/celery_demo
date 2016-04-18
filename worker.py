#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import celery

app = celery.Celery('celery_demo', 'redis://127.0.0.1:6379')