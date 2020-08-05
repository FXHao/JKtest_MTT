# -*- encoding=utf8 -*-
__author__ = "chenshengming"

from airtest.core.api import *

auto_setup(__file__)

# import random

# def randomSecond():
#     random_second = random.randint(10,25)
#     return random_second

# while True:
#     swipe([540,1700],[540,700])
#     sleep(randomSecond())
# #     swipe([540,1700],[540,700])
# #     sleep(18)
# #     swipe([540,1700],[540,700])
# #     sleep(16)
# #     swipe([540,1700],[540,700])
# #     sleep(25)
ysSplash = 0
ptSplash = 0

while True:
    start_app("com.outfit7.herodash.vivo")
    sleep(1)
    if exists(Template(r"tpl1592981854825.png", record_pos=(-0.298, 0.493), resolution=(1080, 2340))):
#     if exists(Template(r"tpl1587388958300.png", record_pos=(0.016, 0.446), resolution=(1080, 2340))):
#     if exists(Template(r"tpl1592905578496.png", record_pos=(0.005, 0.065), resolution=(2340, 1080))):

        ysSplash += 1
        sleep(5)
#         if exists(Template(r"tpl1586942594497.png", record_pos=(-0.002, 0.867), resolution=(1080, 2340))):
#             keyevent("back")
#             sleep(3)
#     elif exists(Template(r"tpl1587389116306.png", record_pos=(-0.052, 0.878), resolution=(1080, 2340))):
    elif exists(Template(r"tpl1592981982577.png", record_pos=(0.028, 0.955), resolution=(1080, 2340))):
#     elif exists(Template(r"tpl1592224260199.png", record_pos=(-0.006, 0.948), resolution=(1080, 2340))):
#     elif exists(Template(r"tpl1592901837286.png", record_pos=(-0.369, 0.191), resolution=(1600, 720))):

        ptSplash += 1
        sleep(5)
#         if exists(Template(r"tpl1586942594497.png", record_pos=(-0.002, 0.867), resolution=(1080, 2340))):
#             keyevent("back")
#             sleep(3)

        
#     if exists(Template(r"tpl1582274275939.png", record_pos=(0.0, 0.894), resolution=(1080, 2340))):
#         ptSplash +=1
#     elif exists(Template(r"tpl1582274484287.png", record_pos=(0.168, -0.32), resolution=(1080, 2340))):
#         ysSplash += 1
    else:
        pass
    print("ysSplash:%d" % ysSplash)
    print("ptSplash:%d" % ptSplash)
    sleep(3)
    stop_app("com.outfit7.herodash.vivo")
    