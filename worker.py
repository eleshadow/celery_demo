#!/usr/bin/env python
# -*- coding: utf-8 -*-

import celery
import config

app = celery.Celery('celery_demo')
app.config_from_object('config')

@app.task()
def test(message):
    print("hello %s" % message)
