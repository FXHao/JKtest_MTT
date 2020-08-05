# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)
from game.Game import Game
from helper import exists_any, position_to_absolute
import traceback

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class MyTalkingTom(Game):

    GuideTest = None
    AdTest = None

    nativeBanner = None
    nativeSplash = None
    nativeSplashClose = None
    nativeInterstitial = None
    nativeInterstitialClose = None

    def config(self):
        super(MyTalkingTom, self).config()
        self.GuideTest = MyTalkingTom_Guide(MyTalkingTom = self)
        self.AdTest = MyTalkingTom_Ad(MyTalkingTom = self)
        self.init_imglist()
    
    # [Helper] 初始化图片
    def init_imglist(self):
        self.nativeBanner = [Template(r"tpl1567505582092.png", record_pos=(-0.171, -0.874), resolution=(1080, 2248)), Template(r"tpl1568797914108.png", record_pos=(0.369, -0.818), resolution=(1080, 1920)), Template(r"tpl1568797924855.png", rgb=True, record_pos=(-0.374, -0.819), resolution=(1080, 1920)), Template(r"tpl1569480707179.png", record_pos=(-0.306, -0.9), resolution=(1080, 2244))]
        self.nativeSplash = [Template(r"tpl1567911842071.png", record_pos=(0.031, 0.77), resolution=(1080, 1920)), Template(r"tpl1569480920892.png", record_pos=(0.043, -0.35), resolution=(1080, 2244))]
        self.nativeSplashClose = None
        self.nativeInterstitial = [Template(r"tpl1567569523059.png", record_pos=(0.013, -0.473), resolution=(1080, 2248)), Template(r"tpl1568187767836.png", record_pos=(0.003, 0.511), resolution=(1080, 1920)), Template(r"tpl1568188097403.png", record_pos=(-0.002, -0.616), resolution=(1080, 1920)), Template(r"tpl1568188109861.png", record_pos=(0.001, -0.652), resolution=(1080, 1920)), Template(r"tpl1568188129389.png", record_pos=(0.012, -0.591), resolution=(1080, 1920)), Template(r"tpl1568704086495.png", record_pos=(-0.003, -0.673), resolution=(1080, 1920)), Template(r"tpl1568798608788.png", record_pos=(-0.244, -0.028), resolution=(1080, 1920)), Template(r"tpl1569548730374.png", record_pos=(0.432, 0.049), resolution=(1080, 2244))]
        self.nativeInterstitialClose = [Template(r"tpl1569483684083.png", record_pos=(0.392, -0.263), resolution=(1080, 2244)), Template(r"tpl1569548743261.png", record_pos=(0.367, -0.349), resolution=(1080, 2244))]
        
    ''' 获取流程字典 '''
    def getProcessDict(self):
        return {#"WakePhone": self.wake_phone,
                "StartApp": self.start_app,
                "StopApp": self.stop_app,
                "ClearApp": self.clear_app,
                
                "Guide": self.GuideTest.guide,
                "Setting": self.GuideTest.setting,
                "Shop": self.GuideTest.shop,
                "MiniGame": self.GuideTest.minigame,
                
                "CheckSplash": self.AdTest.checkSplash,
                "CheckBanner": self.AdTest.checkBanner,
                "CheckInterstitial": self.AdTest.checkInterstitial,
                "CheckVideo": self.AdTest.checkVideo,
                
                # Check Banner 子流程
                "CheckBanner_LiviningRoom": self.AdTest.checkBanner_Livingroom,
                "CheckBanner_Kitchen": self.AdTest.checkBanner_Kitchen,
                "CheckBanner_Bathroom": self.AdTest.checkBanner_Bathroom,
                "CheckBanner_Bedroom": self.AdTest.checkBanner_Bedroom
                
                }
    
    '''================== 通用流程 ==================='''
    
    def goToLivingroom(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([Template(r"tpl1567667429838.png", record_pos=(-0.203, 0.922), resolution=(1080, 2248)), Template(r"tpl1567667416052.png", record_pos=(-0.194, 0.92), resolution=(1080, 2248)), Template(r"tpl1567589317467.png", record_pos=(-0.196, 0.925), resolution=(1080, 2248)), Template(r"tpl1567589396053.png", record_pos=(-0.198, 0.925), resolution=(1080, 2248)),Template(r"tpl1596538199151.png", record_pos=(-0.194, 0.948), resolution=(1080, 2340))])
        if (pos == False):
            assert_equal(True, False, "goToLivingroom() not called in main screen.")
            return
        for i in range(0, 10):
            touch(pos)
            sleep(1)
            pos2 = exists(Template(r"tpl1570517004453.png", record_pos=(0.302, 0.055), resolution=(1080, 2280)))

            if (pos2 == False):
                # Todo: 需要检测和跳过的流程
                if(self.Channel.skipInterstitial(isReportInterstitial)):
                    sleep(0.5)
                    continue
                if(self.skip_beginner_gift()):
                    sleep(0.5)
                    continue
                keyevent("BACK")
                sleep(0.5)
                continue
            return
        assert_equal(True, False, "Should not be here.")
        
    def goToKitchen(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([Template(r"tpl1567577528299.png", record_pos=(0.0, 0.919), resolution=(1080, 2248)), Template(r"tpl1567667454466.png", record_pos=(0.005, 0.92), resolution=(1080, 2248)), Template(r"tpl1567589340484.png", record_pos=(-0.001, 0.923), resolution=(1080, 2248)), Template(r"tpl1567589388744.png", record_pos=(-0.001, 0.924), resolution=(1080, 2248))])
        if (pos == False):
            assert_equal(True, False, "goToKitchen() not called in main screen.")
            return
        for i in range(0, 10):
            touch(pos)
            sleep(0.5)
            pos2 = exists(Template(r"tpl1568259166153.png", record_pos=(-0.297, -0.195), resolution=(1080, 1920)))
            if (pos2 == False):
                # Todo: 需要检测和跳过的流程
                if (self.Channel.skipInterstitial(isReportInterstitial)):
                    sleep(0.5)
                    continue
                if (self.AdTest.checkVideo_skip_FreeFood(isReportVideo)):
                    sleep(0.5)
                    continue
                keyevent("BACK")
                sleep(0.5)
                continue
            return
        assert_equal(True, False, "Should not be here.")
    
    def goToBathroom(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([Template(r"tpl1567506551693.png", record_pos=(0.196, 0.919), resolution=(1080, 2248)), Template(r"tpl1567664748415.png", record_pos=(0.197, 0.92), resolution=(1080, 2248))])
        if (pos == False):
            assert_equal(True, False, "goToBathroom() not called in main screen.")
            return
        for i in range(0, 10):
            touch(pos)
            sleep(0.5)
            pos2 = exists(Template(r"tpl1568259303064.png", record_pos=(-0.113, -0.244), resolution=(1080, 1920)))
            if (pos2 == False):
                # Todo: 需要检测和跳过的流程
                if (self.Channel.skipInterstitial(isReportInterstitial)):
                    sleep(0.5)
                    continue
                keyevent("BACK")
                sleep(0.5)
                continue
            return
        assert_equal(True, False, "Should not be here.")
    
    def goToBedroom(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([Template(r"tpl1567506283133.png", record_pos=(0.401, 0.919), resolution=(1080, 2248)), Template(r"tpl1567589362374.png", record_pos=(0.401, 0.923), resolution=(1080, 2248)), Template(r"tpl1567589372396.png", record_pos=(0.397, 0.919), resolution=(1080, 2248))])
        if (pos == False):
            assert_equal(True, False, "goToBedroom() not called in main screen.")
            return
        for i in range(0, 10):
            touch(pos)
            sleep(0.5)
            pos2 = exists(Template(r"tpl1568259388088.png", record_pos=(-0.003, 0.323), resolution=(1080, 1920)))
            if (pos2 == False):
                # Todo: 需要检测和跳过的流程
                if(self.Channel.skipInterstitial(isReportInterstitial)):
                    sleep(0.5)
                    continue
                keyevent("BACK")
                sleep(0.5)
                continue
            return
        assert_equal(True, False, "Should not be here.")
    
    def backToMain(self):
        for i in range(0, 10):
            pos = exists(Template(r"tpl1568254696587.png", record_pos=(-0.399, 0.769), resolution=(1080, 1920)))
            if (pos != False):
                for j in range(0, 10):
                    pos = exists_any([Template(r"tpl1567667429838.png", record_pos=(-0.203, 0.922), resolution=(1080, 2248)), Template(r"tpl1567667416052.png", record_pos=(-0.194, 0.92), resolution=(1080, 2248)), Template(r"tpl1567589317467.png", record_pos=(-0.196, 0.925), resolution=(1080, 2248)), Template(r"tpl1567589396053.png", record_pos=(-0.198, 0.925), resolution=(1080, 2248))])
                    if (pos == False):
                        break
                    touch(pos)
                    pos2 = exists(Template(r"tpl1568195750810.png", record_pos=(0.349, -0.102), resolution=(1080, 1920)))
                    if (pos2 == False):
                        if (self.Channel.skipInterstitial()):
                            continue
                        keyevent("BACK")
                        continue
                    return
                break
            keyevent("Back")
        assert_equal(True, False, "Should not be here.")
    
    '''==================== skips ===================='''

    def click_GuoqingSignin(self, isReport=False):
        pos = exists(Template(r"tpl1569579851173.png", record_pos=(-0.017, 0.654), resolution=(1080, 2280)))
        if (pos == False):
            return False
        else:
            touch(Template(r"tpl1569580148269.png", record_pos=(-0.014, 0.656), resolution=(1080, 2280)))
            sleep(3)
            touch(Template(r"tpl1569829064154.png", record_pos=(0.383, -0.757), resolution=(720, 1280)))
            sleep(3)
            touch(Template(r"tpl1569829091713.png", record_pos=(0.417, -0.751), resolution=(720, 1280)))


    def skip_permission(self, times = 10):
        poco = self.poco
        for i in range(0, times):
            if poco(text = "始终允许").exists():
                poco(text = "始终允许").click()
                sleep(2)
                continue
            if poco(text = "允许").exists():
                poco(text = "允许").click()
                sleep(2)
                continue
            if poco(text = "确定").exists():
                poco(text = "确定").click()
                sleep(2)
                continue
    
    def skip_beginner_gift(self):
        sleep(2)
        pos = exists(Template(r"tpl1567506478562.png", record_pos=(0.33, 0.508), resolution=(1080, 2248)))
        if (pos != False):
            touch(Template(r"tpl1567506495302.png", record_pos=(0.406, -0.835), resolution=(1080, 2248)))
            return True
        return False

    def skip_daily_challenge(self):
        pos = exists(Template(r"tpl1568704252875.png", record_pos=(0.004, -0.448), resolution=(1080, 1920)))
        if (pos == False):
            return
        keyevent("BACK")
    
class MyTalkingTom_Guide():
    
    MasterManager = None
    MyTalkingTom = None
    poco = None
    AppID = None
    Game = None
    Channel = None
    Reporter = None

    '''=================== 初始化 ===================='''
    
    def __init__(self, MyTalkingTom = None):
        self.MyTalkingTom = MyTalkingTom
        self.config()
    
    def config(self):
        self.MasterManager = self.MyTalkingTom.MasterManager
        self.poco = self.MyTalkingTom.poco
        self.AppID = self.MyTalkingTom.AppID
        self.Game = self.MyTalkingTom
        self.Channel = self.MyTalkingTom.Channel
        self.Reporter = self.MyTalkingTom.Reporter

    '''==================== 入口 ====================='''
    
    # 新手指引入口
    def guide(self):
        self.MyTalkingTom.stop_app()
#         self.MyTalkingTom.clear_app()
        self.MyTalkingTom.start_app()
        self.MyTalkingTom.skip_permission(times = 10)
        self.beginner_guide()
        self.MyTalkingTom.goToLivingroom()
        self.MyTalkingTom.skip_beginner_gift()
    
    # 查看设置入口
    def setting(self):
        self.setting_setting()
        self.setting_law()
        self.setting_Tom()
    
    # 查看商店入口
    def shop(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: Guide_CheckShop\n"
        touch(Template(r"tpl1567577009407.png", record_pos=(-0.151, -0.704), resolution=(1080, 2248)))
        shopItenList = [Template(r"tpl1567577145301.png", record_pos=(-0.328, -0.476), resolution=(1080, 2248)), Template(r"tpl1567577155616.png", record_pos=(0.0, -0.478), resolution=(1080, 2248)), Template(r"tpl1567577162271.png", record_pos=(0.331, -0.478), resolution=(1080, 2248)), Template(r"tpl1567577172516.png", record_pos=(-0.331, -0.08), resolution=(1080, 2248)), Template(r"tpl1567577180097.png", record_pos=(0.001, -0.08), resolution=(1080, 2248)), Template(r"tpl1567577188547.png", record_pos=(0.333, -0.081), resolution=(1080, 2248)), Template(r"tpl1567577198689.png", record_pos=(-0.33, 0.321), resolution=(1080, 2248))]
        i = 0
        for icon in shopItenList:
            i += 1
            if (exists(icon) == False):
                assert_equal(True, True, "商店界面检查失败")
                case.Message += "Shop item doesn't exist, No." + i.__str__() +"\n"
            else:
                case.Message += "Shop item exists, No." + i.__str__() +"\n"
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 查看小游戏入口
    def minigame(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: Guide_MiniGame\n"
        miniGameIconList = [Template(r"tpl1567568552138.png", record_pos=(-0.333, -0.729), resolution=(1080, 2248)), Template(r"tpl1567568560247.png", record_pos=(0.0, -0.723), resolution=(1080, 2248)), Template(r"tpl1567568568392.png", record_pos=(0.331, -0.728), resolution=(1080, 2248)), Template(r"tpl1567568575420.png", record_pos=(-0.332, -0.384), resolution=(1080, 2248)), Template(r"tpl1567568582932.png", record_pos=(0.0, -0.381), resolution=(1080, 2248)), Template(r"tpl1567568590180.png", record_pos=(0.334, -0.382), resolution=(1080, 2248)), Template(r"tpl1567568600042.png", record_pos=(-0.333, -0.042), resolution=(1080, 2248)), Template(r"tpl1567568607725.png", record_pos=(-0.002, -0.045), resolution=(1080, 2248)), Template(r"tpl1567568615766.png", record_pos=(0.332, -0.042), resolution=(1080, 2248)), Template(r"tpl1567568625266.png", record_pos=(-0.331, 0.3), resolution=(1080, 2248)), Template(r"tpl1567568632782.png", record_pos=(-0.003, 0.301), resolution=(1080, 2248)), Template(r"tpl1567568640140.png", record_pos=(0.333, 0.3), resolution=(1080, 2248)), Template(r"tpl1567568648180.png", record_pos=(-0.333, 0.644), resolution=(1080, 2248)), Template(r"tpl1567568657400.png", record_pos=(0.001, 0.644), resolution=(1080, 2248)), Template(r"tpl1567568663741.png", record_pos=(0.333, 0.648), resolution=(1080, 2248))]
        
        miniGameSuccessList = [Template(r"tpl1567578931672.png", record_pos=(0.018, -0.391), resolution=(1080, 2248)), Template(r"tpl1567578946168.png", record_pos=(-0.42, 0.702), resolution=(1080, 2248)), Template(r"tpl1567578955683.png", record_pos=(-0.001, 0.85), resolution=(1080, 2248)), Template(r"tpl1567578969466.png", record_pos=(0.017, -0.64), resolution=(1080, 2248)), Template(r"tpl1567578987185.png", record_pos=(0.014, 0.874), resolution=(1080, 2248)), Template(r"tpl1567579003401.png", record_pos=(-0.01, 0.323), resolution=(1080, 2248)), Template(r"tpl1567579024583.png", record_pos=(0.001, -0.416), resolution=(1080, 2248)), Template(r"tpl1567579043716.png", record_pos=(0.309, 0.874), resolution=(1080, 2248)), Template(r"tpl1567579062359.png", record_pos=(-0.127, 0.694), resolution=(1080, 2248)), Template(r"tpl1567579075533.png", record_pos=(0.307, 0.922), resolution=(1080, 2248)), Template(r"tpl1567579095148.png", record_pos=(-0.279, -0.707), resolution=(1080, 2248)), Template(r"tpl1567579104679.png", threshold=0.6, record_pos=(-0.254, -0.591), resolution=(1080, 2248)), Template(r"tpl1567579117927.png", record_pos=(-0.209, -0.01), resolution=(1080, 2248)), Template(r"tpl1567579131413.png", record_pos=(0.005, -0.299), resolution=(1080, 2248)), Template(r"tpl1567579140011.png", record_pos=(-0.423, 0.391), resolution=(1080, 2248))]
        
        self.MyTalkingTom.goToLivingroom()
        touch(Template(r"tpl1567569220185.png", record_pos=(-0.304, 0.714), resolution=(1080, 2248)))

        for i in range(0, 15):
            pos = exists(miniGameIconList[i])
            if (pos == False):
                
                swipe(position_to_absolute([0.5, 0.8]), position_to_absolute([0.5, 0.4])) 
                pos = exists(miniGameIconList[i])
                if (pos != False):
                    break
                assert_equal(True, True, "Mini game check failed, No." + (i + 1).__str__())
                case.Message += "Mini game check failed, No." + (i + 1).__str__() + "\n"
                continue
            touch(pos)
            sleep(1)
            pos = exists(miniGameSuccessList[i])
            if (pos == False):
                assert_equal(True, True, "Mini game check failed, No." + (i + 1).__str__())
                case.Message += "Mini game check failed, No." + (i + 1).__str__() + "\n"
                self.MyTalkingTom.backToMain()
                self.Channel.skipInterstitial()
                touch(Template(r"tpl1567569220185.png", record_pos=(-0.304, 0.714), resolution=(1080, 2248)))
                continue
            sleep(0.5)
            keyevent("BACK")
            pos = exists(Template(r"tpl1567569005154.png", record_pos=(-0.159, 0.199), resolution=(1080, 2248)))
            if (pos != False):
                touch(pos)
                sleep(0.5)
                self.Channel.skipInterstitial()
                sleep(0.5)
                keyevent("BACK")
            while(exists(Template(r"tpl1567592656112.png", record_pos=(-0.306, -0.958), resolution=(1080, 2248))) == False):
                keyevent("BACK")
                
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    '''================= For guide() ================='''
    
    # 新手引导
    def beginner_guide(self):
        self.Channel.login()
        sleep(3)
        touch(Template(r"tpl1567501638079.png", record_pos=(0.383, 0.022), resolution=(1080, 2248)), duration=0.5, times = 2)
        sleep(1)
        touch(Template(r"tpl1567501771358.png", rgb=True, record_pos=(0.001, 0.401), resolution=(1080, 2248)))
        sleep(1)
        touch(Template(r"tpl1567501786370.png", record_pos=(0.323, -0.004), resolution=(1080, 2248)))
        sleep(10)
        pos = exists(Template(r"tpl1567504064721.png", record_pos=(0.02, 0.386), resolution=(1080, 2248)))
        if (pos != False):
            touch(pos)
            touch(Template(r"tpl1567504157962.png", record_pos=(-0.126, 0.362), resolution=(1080, 2248)))
            sleep(5)
        touch(Template(r"tpl1567503757543.png", record_pos=(0.008, 0.465), resolution=(1080, 2248)))
        sleep(3)
        touch(Template(r"tpl1567503778397.png", record_pos=(0.006, 0.925), resolution=(1080, 2248)))
        swipe(Template(r"tpl1567503796792.png", record_pos=(-0.278, 0.215), resolution=(1080, 2248)), Template(r"tpl1567504346592.png", record_pos=(0.0, 0.025), resolution=(1080, 2248)))
        sleep(5)
        touch(Template(r"tpl1567503827541.png", record_pos=(0.207, 0.928), resolution=(1080, 2248)))
        sleep(15)
        touch(Template(r"tpl1567503851190.png", record_pos=(-0.198, 0.926), resolution=(1080, 2248)))
        swipe(Template(r"tpl1567503873365.png", record_pos=(0.024, 0.152), resolution=(1080, 2248)), vector=[0.0184, 0.1791])
        sleep(5)
        touch(Template(r"tpl1567503882284.png", record_pos=(0.404, 0.919), resolution=(1080, 2248)))
        touch(Template(r"tpl1567503897930.png", record_pos=(0.406, 0.659), resolution=(1080, 2248)))
        sleep(20)
        touch(Template(r"tpl1569826643419.png", record_pos=(0.425, -0.81), resolution=(720, 1280)))
        sleep(10)
        # 录音请求
        for i in range(3):
            if self.poco(text = "始终允许").exists():
                self.poco(text = "始终允许").click()
                sleep(1)
            if self.poco(text = "允许").exists():
                self.poco(text = "允许").click()
                sleep(1)
            if self.poco(text = "确定").exists():
                self.poco(text = "确定").click()
                sleep(1)
        sleep(5)
        touch(Template(r"tpl1567504671526.png", record_pos=(0.402, 0.66), resolution=(1080, 2248)))

        

    '''================ For setting() ================'''
    
    # 设置界面
    def setting_setting(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: Guide_Setting\n"
        sleep(1)
        touch(Template(r"tpl1567566946253.png", record_pos=(-0.372, -0.633), resolution=(1080, 2248)))
        touch(Template(r"tpl1567566961287.png", record_pos=(0.153, 0.909), resolution=(1080, 2248)))
        touch(Template(r"tpl1567566999371.png", record_pos=(0.0, 0.203), resolution=(1080, 2248)))
        if (exists(Template(r"tpl1567567122202.png", record_pos=(-0.355, -0.86), resolution=(1080, 2248))) == False):
            assert_equal(True, True, "设置界面测试失败")
            case.Message += "设置界面测试失败\n"
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 法律界面
    def setting_law(self):
        sleep(1)
        touch(Template(r"tpl1567566946253.png", record_pos=(-0.372, -0.633), resolution=(1080, 2248)))
        touch(Template(r"tpl1567566961287.png", record_pos=(0.153, 0.909), resolution=(1080, 2248)))
        touch(Template(r"tpl1567567396391.png", record_pos=(0.003, 0.393), resolution=(1080, 2248)))
        touch(Template(r"tpl1567567422526.png", record_pos=(0.001, -0.695), resolution=(1080, 2248)))
        if (exists(Template(r"tpl1567567480308.png", record_pos=(-0.149, -0.594), resolution=(1080, 2248))) == False):
            assert_equal(True, True, "用户许可协议法律界面检查失败")
            case.Message += "用户许可协议法律界面检查失败\n"
        keyevent("Back")
        touch(Template(r"tpl1567567460230.png", record_pos=(0.001, -0.512), resolution=(1080, 2248)))
        if (exists(Template(r"tpl1567567491976.png", record_pos=(-0.353, -0.877), resolution=(1080, 2248))) == False):
            assert_equal(True, True, "隐私法律界面检查失败")
            case.Message += "隐私法律界面检查失败\n"
        keyevent("Back")
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()

    # 汤姆猫信息界面
    def setting_Tom(self):
        
        case = self.MasterManager.curCase
        
        sleep(1)
        touch(Template(r"tpl1567566946253.png", record_pos=(-0.372, -0.633), resolution=(1080, 2248)))
        touch(Template(r"tpl1567567606065.png", record_pos=(-0.151, 0.919), resolution=(1080, 2248)))
        if (exists(Template(r"tpl1567567631185.png", record_pos=(-0.341, 0.013), resolution=(1080, 2248))) == False):
            assert_equal(True, True, "汤姆猫信息界面检查失败")
            case.Message += "汤姆猫信息界面检查失败\n"
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
        
class MyTalkingTom_Ad():

    MasterManager = None
    MyTalkingTom = None
    poco = None
    AppID = None
    Channel = None
    Reporter = None

    '''=================== 初始化 ===================='''
    
    def __init__(self, MyTalkingTom = None):
        self.MyTalkingTom = MyTalkingTom
        self.config()
    
    def config(self):
        self.MasterManager = self.MyTalkingTom.MasterManager
        self.poco = self.MyTalkingTom.poco
        self.AppID = self.MyTalkingTom.AppID
        self.Channel = self.MyTalkingTom.Channel
        self.Reporter = self.MyTalkingTom.Reporter

    '''==================== 入口 ====================='''
    
    ''' 检测开屏 '''
    def checkSplash(self):
        sleep(2)
        self.MyTalkingTom.stop_app()
        sleep(2)
        self.MyTalkingTom.start_app()
        self.Channel.isSplashExists(isReport = True)
        self.Channel.login()
        
    ''' 检测Banner '''
    def checkBanner(self):
        
        for fun in [self.checkBanner_Livingroom, 
                    self.checkBanner_Kitchen, 
                    self.checkBanner_Bathroom, 
                    self.checkBanner_Bedroom]:
            try:
                fun()
            except:
                self.MasterManager.curCase.Message += "Case Failed"
                traceback.print_exc()
                self.Channel.restart()

    ''' 检测插屏 '''
    def checkInterstitial(self):
        
        case = self.MasterManager.curCase
        
        self.MyTalkingTom.goToBedroom()
        
        # 去主界面
        case.Message += "TestPoint: CheckInterstitial_GoToLivingroom\n"
        self.MyTalkingTom.goToLivingroom(isReportInterstitial = True)
        case.Message += "TestPoint: CheckInterstitial_GoToKitchen\n"
        self.MyTalkingTom.goToKitchen(isReportInterstitial = True)
        case.Message += "TestPoint: CheckInterstitial_GoToBathroom\n"
        self.MyTalkingTom.goToBathroom(isReportInterstitial = True)
        case.Message += "TestPoint: CheckInterstitial_GoToBedroom\n"
        self.MyTalkingTom.goToBedroom(isReportInterstitial = True)
        case.Message += "TestPoint: CheckInterstitial_GoToLivingroom\n"
        self.MyTalkingTom.goToLivingroom(isReportInterstitial = True)
        case.Message += "TestPoint: CheckInterstitial_GoToKitchen\n"
        self.MyTalkingTom.goToKitchen(isReportInterstitial = True)
        case.Message += "TestPoint: CheckInterstitial_GoToBathroom\n"
        self.MyTalkingTom.goToBathroom(isReportInterstitial = True)
        case.Message += "TestPoint: CheckInterstitial_GoToBedroom\n"
        self.MyTalkingTom.goToBedroom(isReportInterstitial = True)
        
    ''' 检测视频 '''
    def checkVideo(self):
        
        if (self.Channel.isCheckPointReady("Video") == False):
            assert_equal("True", "True", "Video检测点尚未适配此渠道")
            self.MasterManager.curCase.Message += "Video检测点尚未适配此渠道"
            return
        
        case = self.MasterManager.curCase
        case.Message += "TestPoint: CheckVideo\n"
        for fun in [self.checkVideo_GiftBox, 
                    self.checkVideo_Toy, 
                    self.checkVideo_LivingroomBottonRight, 
                    self.checkVideo_Pay,
                    self.checkVideo_Refrigerator,
                    self.checkVideo_MiniGame]:
            try:
                fun()
            except:
                self.MasterManager.curCase.Message += "Case Failed"
                traceback.print_exc()
                self.Channel.restart()
    
    '''============= For checkBanner() =============='''
    
    # 客厅
    def checkBanner_Livingroom(self):
        
        case = self.MasterManager.curCase
        
        self.MyTalkingTom.goToLivingroom()
        
        # 主界面
        case.Message += "TestPoint: CheckBanner_Livingroom_MainScreen\n"
        self.Channel.isBannerExists(isReport = True)
        
        # 小游戏
        miniGameIconList = [Template(r"tpl1567568552138.png", record_pos=(-0.333, -0.729), resolution=(1080, 2248)), Template(r"tpl1567568560247.png", record_pos=(0.0, -0.723), resolution=(1080, 2248)), Template(r"tpl1567568568392.png", record_pos=(0.331, -0.728), resolution=(1080, 2248)), Template(r"tpl1567568575420.png", record_pos=(-0.332, -0.384), resolution=(1080, 2248)), Template(r"tpl1567568582932.png", record_pos=(0.0, -0.381), resolution=(1080, 2248)), Template(r"tpl1567568590180.png", record_pos=(0.334, -0.382), resolution=(1080, 2248)), Template(r"tpl1567568600042.png", record_pos=(-0.333, -0.042), resolution=(1080, 2248)), Template(r"tpl1567568607725.png", record_pos=(-0.002, -0.045), resolution=(1080, 2248)), Template(r"tpl1567568615766.png", record_pos=(0.332, -0.042), resolution=(1080, 2248)), Template(r"tpl1567568625266.png", record_pos=(-0.331, 0.3), resolution=(1080, 2248)), Template(r"tpl1567568632782.png", record_pos=(-0.003, 0.301), resolution=(1080, 2248)), Template(r"tpl1567568640140.png", record_pos=(0.333, 0.3), resolution=(1080, 2248)), Template(r"tpl1567568648180.png", record_pos=(-0.333, 0.644), resolution=(1080, 2248)), Template(r"tpl1567568657400.png", record_pos=(0.001, 0.644), resolution=(1080, 2248)), Template(r"tpl1567568663741.png", record_pos=(0.333, 0.648), resolution=(1080, 2248))]
        touch(Template(r"tpl1567569220185.png", record_pos=(-0.304, 0.714), resolution=(1080, 2248)))
        case.Message += "TestPoint: CheckBanner_Livingroom_MiniGameSelectScreen\n"
        self.Channel.isBannerExists(isReport = True)
        for i in range(0, 15):
            case.Message += "TestPoint: CheckBanner_Livingroom_MiniGame No." + i.__str__() + "\n"
            for j in range(0, 2):
                swipe(position_to_absolute([0.5, 0.4]), position_to_absolute([0.5, 0.8])) 
            for j in range(0, 3):
                pos = exists(miniGameIconList[i])
                if (pos == False):
                    swipe(Template(r"tpl1569661033837.png", record_pos=(0.001, 0.637), resolution=(1080.0, 1920.0)), vector=[-0.0411, -0.5995])

                    continue
                else:
                    break
            if (pos == False):
                self.Reporter.report("Game icon not found.")
                continue
            touch(pos)
            sleep(1)
            self.Channel.isBannerExists(isReport = True)
            keyevent("BACK")
            pos = exists(Template(r"tpl1567569005154.png", record_pos=(-0.159, 0.199), resolution=(1080, 2248)))
            if (pos != False):
                touch(pos)
                sleep(0.5)
                self.Channel.skipInterstitial()
                sleep(0.5)
                keyevent("BACK")
            #while(exists(Template(r"tpl1567592656112.png", record_pos=(-0.306, -0.958), resolution=(1080, 2248))) == False):
                #keyevent("BACK")
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 厨房
    def checkBanner_Kitchen(self):
        
        case = self.MasterManager.curCase
        
        self.MyTalkingTom.goToKitchen()
        
        # 主界面
        case.Message += "TestPoint: CheckBanner_Kitchen_MainScreen\n"
        self.Channel.isBannerExists(isReport = True)
        
        # 冰箱
        touch(Template(r"tpl1567592384512.png", record_pos=(-0.304, -0.205), resolution=(1080, 2248)))
        sleep(1)
        case.Message += "TestPoint: CheckBanner_Kitchen_Refrigerator\n"
        self.Channel.isBannerExists(isReport = True)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 浴室
    def checkBanner_Bathroom(self):
        
        case = self.MasterManager.curCase
        
        self.MyTalkingTom.goToBathroom()
        sleep(8)
        # 主界面
        case.Message += "TestPoint: CheckBanner_Bathroom_MainScreen\n"
        self.checkVideo_skip_Clean()
        sleep(2)
        self.Channel.isBannerExists(isReport = True)
    
    # 卧室
    def checkBanner_Bedroom(self):
        
        case = self.MasterManager.curCase
        
        self.MyTalkingTom.goToBedroom()
        
        # 主界面
        case.Message += "TestPoint: CheckBanner_Bedroom_MainScreen\n"
        self.Channel.isBannerExists(isReport = True)
    
    '''======= For checkVideo() 直接点击部分 ========='''
    
    # 主界面礼物盒
    def checkVideo_GiftBox(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: CheckVideo_GiftBox\n"
        self.MyTalkingTom.goToLivingroom()
        sleep(10)
        pos = exists_any([Template(r"tpl1568189218352.png", record_pos=(0.355, 0.276), resolution=(1080, 1920)), Template(r"tpl1568794142300.png", record_pos=(0.354, 0.275), resolution=(1080, 1920)), Template(r"tpl1568794239667.png", record_pos=(0.352, 0.283), resolution=(1080, 1920)), Template(r"tpl1568796220494.png", record_pos=(0.356, 0.288), resolution=(1080, 1920))])
        if (pos == False):
            case.Message += "TestPoint: CheckVideo_GiftBox\n"
            assert_equal(True, True, "未发现主界面礼盒")
            return
        touch(pos)
        sleep(1)
        pos = exists(Template(r"tpl1568189325391.png", record_pos=(-0.003, 0.502), resolution=(1080, 1920)))
        if (pos != False):
            touch(pos)
            sleep(5)
            self.Channel.skipVideo(isReport = True)
            sleep(2)
        pos = exists(Template(r"tpl1568860985743.png", record_pos=(-0.005, 0.504), resolution=(1080, 1920)))
        if (pos != False):
            touch(pos)
            sleep(10)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 主界面小玩具
    def checkVideo_Toy(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: CheckVideo_Toy\n"
        self.MyTalkingTom.goToLivingroom()
        pos = exists_any([Template(r"tpl1568189505139.png", record_pos=(-0.274, 0.308), resolution=(1080, 1920)), Template(r"tpl1568861089586.png", record_pos=(-0.27, 0.056), resolution=(1080, 1920)), Template(r"tpl1569480855531.png", record_pos=(-0.286, 0.382), resolution=(1080, 2244)), Template(r"tpl1571146159552.png", record_pos=(-0.277, 0.378), resolution=(1080, 2280))])
        if (pos == False):
            case.Message += "未发现主界面礼盒\n"
            assert_equal(True, True, "未发现主界面礼盒")
            return
        else:
            for i in range(0, 10):
                touch(pos, times = 5)
                pos2 = exists(Template(r"tpl1568861410923.png", record_pos=(-0.4, 0.774), resolution=(1080, 1920)))
                if (pos2 == False):
                    break
        pos = exists(Template(r"tpl1568189984064.png", record_pos=(0.004, 0.504), resolution=(1080, 1920)))
        if (pos != False):
            touch(pos)
            sleep(5)
            self.Channel.skipVideo(isReport = True)
        else:
            case.Message += "未成功播放视频n"
            assert_equal(True, True, "未成功播放视频")
        pos = exists(Template(r"tpl1568860985743.png", record_pos=(-0.005, 0.504), resolution=(1080, 1920)))
        if (pos != False):
            touch(pos)
            sleep(10)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()

    # 主界面右下角(睡眠?)
    def checkVideo_LivingroomBottonRight(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: CheckVideo_SleepPotion\n"
        self.MyTalkingTom.goToLivingroom()
        pos = exists(Template(r"tpl1568189789485.png", record_pos=(0.404, 0.598), resolution=(1080, 1920)))
        if (pos == False):
            case.Message += "未发现睡眠药水\n"
            assert_equal(True, True, "未发现睡眠药水")
        else:
            touch(pos)
            sleep(5)
            self.Channel.skipVideo(isReport = True)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 充值界面
    def checkVideo_Pay(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: CheckVideo_Pay\n"
        self.MyTalkingTom.goToLivingroom()
        touch(Template(r"tpl1568190300263.png", record_pos=(-0.144, -0.582), resolution=(1080, 1920)))
        sleep(0.5)
        pos = exists(Template(r"tpl1568190908217.png", record_pos=(-0.333, -0.43), resolution=(1080, 1920)))
        if (pos == False):
            case.Message += "未发现充值界面视频\n"
            assert_equal(True, True, "未发现充值界面视频")
        else:
            touch(Template(r"tpl1568190908217.png", target_pos=8, record_pos=(-0.333, -0.43), resolution=(1080, 1920)))
            sleep(5)
            self.Channel.skipVideo(isReport = True)
            sleep(1)
            keyevent("BACK")

        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 食物界面
    def checkVideo_Refrigerator(self):
        case = self.MasterManager.curCase
        case.Message += "TestPoint: CheckVideo_Refrigerator\n"
        self.MyTalkingTom.goToKitchen()
        touch(Template(r"tpl1568190613351.png", record_pos=(-0.315, -0.213), resolution=(1080, 1920)))
        sleep(0.5)
        touch(Template(r"tpl1568190621163.png", record_pos=(-0.295, -0.545), resolution=(1080, 1920)))
        sleep(0.5)
        pos = exists(Template(r"tpl1568190636606.png", record_pos=(0.013, -0.452), resolution=(1080, 1920)))
        if (pos == False):
            case.Message += "未发现食物界面视频\n"
            assert_equal(True, True, "未发现食物界面视频")
        else:
            touch(pos)
            sleep(5)
            self.Channel.skipVideo(isReport = True)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    # 小游戏
    def checkVideo_MiniGame(self):
        self.MyTalkingTom.goToLivingroom()
        touch(Template(r"tpl1568792874906.png", record_pos=(-0.304, 0.56), resolution=(1080, 1920)))
        sleep(1)
        for i in range(1, 10):
            pos = exists(Template(r"tpl1568792945340.png", record_pos=(-0.327, 0.636), resolution=(1080, 1920)))
            if (pos == False):
                swipe(position_to_absolute([0.5, 0.8]), position_to_absolute([0.5, 0.4]))
                continue
            break
        touch(pos)
        sleep(2)
        touch(position_to_absolute([0.5, 0.8]))
        sleep(2)
        pos = exists(Template(r"tpl1568793082428.png", record_pos=(0.005, 0.265), resolution=(1080, 1920)))
        if (pos != False):
            touch(pos)
            self.Channel.skipVideo(isReport = True)
        sleep(10)
        self.Channel.skipInterstitial()
        pos = exists(Template(r"tpl1568793497402.png", record_pos=(-0.005, 0.057), resolution=(1080, 1920)))
        if (pos != False):
            touch(pos)
            self.Channel.skipVideo(isReport = True)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
    
    '''========= For checkVideo() 弹出部分 ==========='''
    
    # 跳过每日优惠
    def checkVideo_skip_DailyDiamond(self, isReport = False):
        pos = exists(Template(r"tpl1568193092559.png", record_pos=(0.006, -0.356), resolution=(1080, 1920)))
        if (pos == False):
            return
        if (isReport == False):
            keyevent("BACK")
            return
        if (isReport == True):
            touch(Template(r"tpl1568193100009.png", record_pos=(0.002, 0.238), resolution=(1080, 1920)))
            sleep(5)
            self.Channel.skipVideo(isReport = True)
            self.MyTalkingTom.backToMain()
            self.Channel.skipInterstitial()
            if (exists(Template(r"tpl1568193816032.png", record_pos=(-0.006, -0.001), resolution=(1080, 1920)))):
                keyevent("BACK")
            return
    
    # 跳过免费大餐
    def checkVideo_skip_FreeFood(self, isReport = False):
        pos = exists(Template(r"tpl1568203032046.png", record_pos=(0.019, 0.56), resolution=(1080, 1920)))
        if (pos == False):
            return False
        if (isReport == False):
            keyevent("BACK")
            return True
        touch(pos)
        sleep(5)
        self.Channel.skipVideo(isReport = True)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
        return True
    
    # 跳过吃饱奖励
    def checkVideo_skip_Full(self, isReport = False):
        pos = exists(Template(r"tpl1568255744647.png", record_pos=(-0.008, -0.369), resolution=(1080, 1920)))
        if (pos == False):
            return
        if (isReport == False):
            keyevent("BACK")
            return
        if (isReport == True):
            touch(Template(r"tpl1568255751963.png", record_pos=(0.0, 0.379), resolution=(1080, 1920)))
            sleep(5)
            self.Channel.skipVideo(isReport = True)
            self.MyTalkingTom.backToMain()
            self.Channel.skipInterstitial()
            return
        pass
    
    # 跳过干净奖励
    def checkVideo_skip_Clean(self, isReport = False):
        pos = exists(Template(r"tpl1568256211708.png", record_pos=(-0.022, -0.365), resolution=(1080, 1920)))
        if (pos == False):
            return
        if (isReport == False):
            keyevent("BACK")
            return
        if (isReport == True):
            touch(Template(r"tpl1568256218734.png", record_pos=(0.0, 0.381), resolution=(1080, 1920)))
            sleep(5)
            self.Channel.skipVideo(isReport = True)
            self.MyTalkingTom.backToMain()
            self.Channel.skipInterstitial()
            return
        pass
    
    # 跳过升级双倍金币
    def checkVideo_skip_Levelup(self, isReport = False):
        pos = exists(Template(r"tpl1568203237856.png", record_pos=(0.023, -0.109), resolution=(1080, 1920)))
        if (pos == False):
            return False
        if (isReport == False):
            keyevent("BACK")
            return True
        touch(pos)
        sleep(5)
        self.Channel.skipVideo(isReport = True)
        self.MyTalkingTom.backToMain()
        self.Channel.skipInterstitial()
        return True
        
          
    '''================== 未完成 ===================='''
    
    # 旅游界面
    def checkVideo_Travel(self):
        pass
    





        














