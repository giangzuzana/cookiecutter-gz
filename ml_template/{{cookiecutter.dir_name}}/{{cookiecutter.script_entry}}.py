#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import {{cookiecutter.script_constants}} as sc
import {{cookiecutter.script_utils}} as su
import time

start = time.strftime("%Y%m%d-%H%M%S")      			# timestamp

print("Hello from, {{cookiecutter.greeting_recipient}}!")

print su.run_time(start)
