# -*- encoding=utf8 -*-
__author__ = "chenshengming"

from airtest.core.api import *

auto_setup(__file__)

def guanbi():
    
    if exists(Template(r"tpl1572073095413.png", record_pos=(0.003, -0.001), resolution=(720, 1280))):
            touch(Template(r"tpl1572073110060.png", record_pos=(-0.229, 0.147), resolution=(720, 1280)))
            sleep(1)
            shishi()
            jixu()
    else:
        shishi()

def jixu():
    if exists(Template(r"tpl1572075161953.png", record_pos=(-0.013, 0.347), resolution=(720, 1280))):
        touch((335,890),1)
        sleep(32)
        guanbi()
        shishi()
    else:
        touch((650,60),1)
        sleep(1)

def shishi():
    if exists(Template(r"tpl1572075309113.png", record_pos=(0.0, 0.103), resolution=(720, 1280))):
        touch((350,720),1)
        sleep(5)
        jixu()
    else:
        pass


while True:
    if exists(Template(r"tpl1572073031429.png", record_pos=(-0.311, 0.546), resolution=(720, 1280))):
        touch((140,1040),1)
        sleep(31)
        guanbi()
    else:
        pass
