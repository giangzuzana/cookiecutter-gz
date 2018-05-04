#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta
from random import randint
           
def run_time(start, format_str='%Y%m%d-%H%M%S'):
    diff = time.mktime(datetime.strptime(time.strftime(format_str), format_str).timetuple()) - \
           time.mktime(datetime.strptime(start, format_str).timetuple())
    return timedelta(seconds=diff)

