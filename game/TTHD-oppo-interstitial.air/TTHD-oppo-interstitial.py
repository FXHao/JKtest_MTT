# -*- encoding=utf8 -*-
__author__ = "chenshengming"

from airtest.core.api import *

auto_setup(__file__)

while True:
    touch((370,780),1)
    sleep(3)
    touch((645,197),1)
    if exists(Template(r"tpl1573642397814.png", record_pos=(0.003, 0.372), resolution=(720, 1440))):
        keyevent("back")
    else:
        pass
    