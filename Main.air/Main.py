# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../.."))
auto_setup(__file__)
using(_project_root)
from airtest.core.android.adb import *
from TestManager.TestMasterManager import MasterManager
from airtest.core.android.android import *

def run():
    m_MasterManager = MasterManager()
    m_MasterManager.config(config_file = "config.ini")
    m_MasterManager.print_test_list()
    m_MasterManager.run_test()

    m_MasterManager.TestSummarize_print()
    m_MasterManager.LogToFile()

run()

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
