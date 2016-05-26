#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import yate
import cgitb
cgitb.enable()
print(yate.start_response())
print(yate.do_form('add_timing_data.py',["Timevalue"],text='send'))