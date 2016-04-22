#!/usr/bin/env python
# -*- coding: utf-8 -*-

import celery
import config
import worker

app = celery.Celery('celery_beat')
app.config_from_object('config')

