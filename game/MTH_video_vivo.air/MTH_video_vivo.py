# -*- encoding=utf8 -*-
__author__ = "chenshengming"

from airtest.core.api import *

auto_setup(__file__)

def tryAgain(self):
    if exists(Template(r"tpl1571661336226.png", record_pos=(-0.001, 0.517), resolution=(720, 1520))):
                touch(Template(r"tpl1571661346984.png", record_pos=(0.007, 0.517), resolution=(720, 1520)))
                sleep(32)
    else :
        touch((650,130),1)
    
        

while True:
    if exists(Template(r"tpl1571661173353.png", record_pos=(-0.344, 0.665), resolution=(720, 1520))):
        touch(Template(r"tpl1571661190139.png", record_pos=(-0.343, 0.65), resolution=(720, 1520)))
        sleep(32)
        if exists(Template(r"tpl1571661871970.png", record_pos=(0.006, 0.035), resolution=(720, 1520))):
            touch((200,890),1)

            if exists(Template(r"tpl1571661292397.png", record_pos=(0.003, 0.169), resolution=(720, 1520))):
                touch(Template(r"tpl1571661304006.png", record_pos=(0.001, 0.168), resolution=(720, 1520)))
                sleep(5)
        self.tryAgain
            
                
#         else:
#             keyevent("back")