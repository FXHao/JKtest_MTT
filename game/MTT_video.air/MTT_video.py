# -*- encoding=utf8 -*-
__author__ = "chenshengming"

from airtest.core.api import *

auto_setup(__file__)
nativeInterstitial = 0
ordinaryInterstitial = 0
nativeSplash = 0
ordinarySplash = 0
nativeBigInterstitial = 0
nativeBanner = 0
ordinaryBanner = 0

def Interstitial():
    global nativeInterstitial, ordinaryInterstitial, nativeBigInterstitial
    if exists(Template(r"tpl1568798608788.png", record_pos=(-0.244, -0.028), resolution=(1080, 1920))):
        nativeInterstitial += 1
        keyevent("back")
    elif exists(Template(r"tpl1574995679220.png", record_pos=(-0.427, -0.048), resolution=(1080, 2340))):
        nativeBigInterstitial += 1
    elif exists(Template(r"tpl1571801246856.png", record_pos=(0.001, 0.469), resolution=(720, 1520))):
        ordinaryInterstitial += 1
        touch((360,1100),1)
    else:
        pass
    
    return nativeInterstitial,ordinaryInterstitial,nativeBigInterstitial

def Banner():
    global nativeBanner, ordinaryBanner
    if exists():
        pass
    elif exists():
        pass
    else :
        pass
    return nativeBanner, ordinaryBanner

def Splash():
    global nativeSplash, ordinarySplash
#     if exists(Template(r"tpl1571803011845.png", record_pos=(0.051, -0.408), resolution=(720, 1520))):
#         nativeSplash += 1
#         sleep(5)
#     elif exists(Template(r"tpl1567911842071.png", record_pos=(0.031, 0.77), resolution=(1080, 1920))):
#         ordinarySplash += 1
#         sleep(5)
    
#     else:
#         pass
#     if exists(Template(r"tpl1575031172066.png", record_pos=(-0.022, 0.351), resolution=(720, 1280))):
#         nativeSplash += 1
#         sleep(5)
#     elif exists(Template(r"tpl1575031243403.png", record_pos=(-0.019, 0.818), resolution=(1080, 2280))):
#         ordinarySplash += 1
#         sleep(5)

    if exists(Template(r"tpl1575533576649.png", record_pos=(0.02, 0.902), resolution=(1080, 2280))):
        nativeSplash += 1
        sleep(4)
    elif exists():
        ordinarySplash += 1
        sleep(4)
    
    else:
        pass

    return nativeSplash, ordinarySplash



while True:
    start_app("com.outfit7.herodash.nearme.gamecenter")
    Splash()
    sleep(1) 
    print("nativeSplash:", nativeSplash)
    print("ordinarySplash:", ordinarySplash)
    stop_app("com.outfit7.herodash.nearme.gamecenter")
#     touch((560,2206),1)
#     sleep(1)
#     Interstitial()
#     if nativeBigInterstitial == 1:
#         break
#     else:
#         pass
#     print("nativeInterstitial:", nativeInterstitial)
#     print("ordinaryInterstitial:", ordinaryInterstitial)
#     touch((350,2206),1)
#     sleep(1)
#     Interstitial()
#     if nativeBigInterstitial == 1:
#         break
#     else:
#         pass
#     print("nativeInterstitial:", nativeInterstitial)
#     print("ordinaryInterstitial:", ordinaryInterstitial)



        