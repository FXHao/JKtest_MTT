# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
auto_setup(__file__)
using(_project_root)
from channel.Channel import Channel
from helper import exists_any

class oppo(Channel):
    
    def getProcessDict(self):
        return {}
    
    '''=============== 对应渠道流程相关 ================'''
    
    # 登录
    def login(self):
        for i in range(0, 10):
            pos = exists_any([
                Template(r"tpl1568174154529.png", record_pos=(-0.057, -0.36), resolution=(1080, 1920)),
                Template(r"tpl1569228712107.png", record_pos=(0.019, -0.407), resolution=(1080, 1920))
            ])
            if (pos != False):
                keyevent("BACK")
                continue
            pos = exists_any([
                Template(r"tpl1568883448109.png", record_pos=(0.381, 0.02), resolution=(1080, 1920)),
                Template(r"tpl1568883477317.png", record_pos=(-0.397, 0.765), resolution=(1080, 1920))
            ])
            if (pos != False):
                break
            keyevent("BACK")
            sleep(5)
        self.Game.skip_beginner_gift()
    
    '''================= Poco Getter ================='''

    def getPoco(self, PocoType = Channel.eCheckPoint["None"]):
        
        poco = self.poco
        
        if (PocoType == self.eCheckPoint["None"]):
            return None
        
        if (PocoType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["OrdinarySplash_Close"]):        # 普通开屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["NativeSplash_Exist"]):          # 原生开屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["NativeSplash_Close"]):          # 原生开屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return None
        
        if (PocoType == self.eCheckPoint["NativeBanner_Exist"]):          # 原生Banner_存在
            return None
        
        if (PocoType == self.eCheckPoint["OrdinaryInterstitial_Exist"]):  # 普通插屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["OrdinaryInterstitial_Close"]):  # 普通插屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["NativeInterstitial_Exist"]):    # 原生插屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["NativeInterstitial_Close"]):    # 原生插屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["Video_Exist"]):                 # Video_存在
            return None
        
        if (PocoType == self.eCheckPoint["Video_End"]):                   # Video_结束
            # return None
            return poco(textMatches = '^.*关闭')

        if (PocoType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return None

        if (PocoType == self.eCheckPoint["Video_Interstitial_Exist"]):    # 视频插屏
            return poco(nameMatches = "(.*)id/tt_reward_root")

        if (PocoType == self.eCheckPoint["Video_Interstitial_Close"]):
            return [
                poco(nameMatches = "(.*)id/tt_top_skip"),
                poco(nameMatches = "(.*)id/tt_video_ad_close")
            ]
        return None

    def getImage(self, ImageType = Channel.eCheckPoint["None"]):
        
        if (ImageType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            return None
        
        if (ImageType == self.eCheckPoint["OrdinarySplash_Close"]):        # 普通开屏_关闭
            return None
        
        if (ImageType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return None
        
        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Exist"]):  # 普通插屏_存在
            return None
        
        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Close"]):  # 普通插屏_关闭
            return None
        
        if (ImageType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return None
        
        # Defalut
        return None
    

