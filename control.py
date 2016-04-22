#!/usr/bin/env python
# -*- coding: utf-8 -*-

import worker

result_list = []
result = worker.test.delay("lijin09")

result_list.append(result)

for result in result_list:
    if result.ready():
        print("%s ready" % result.id)
    else:
        print("%s not ready" % result.id)
