# -*- coding: utf-8 -*-
"""Configuration for Wiki
"""

# For Maverick
site_prefix = "http://wiki.139931.xyz/"
source_dir = "../src/"
build_dir = "../dist/"
template = {
    "name": "Kepler",
    "type": "local",
    "path": "../Kepler"
}
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "jhx520/site-Wiki@gh-pages"
}
category_by_folder = True
for_manual_build_trigger = 1

# 站点设置
site_name = "三刀鱼"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2020-02-08T12:00+08:00"
author = "Anony"
email = "1046880355@qq.com"
author_homepage = "http://139931.xyz"
description = "熊猫小A的Wiki站点"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'wiki']
language = 'zh-CN'

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "uM4TdSOqBxnHFm3gcy0VRcVC-gzGzoHsz",
    "appKey": "S8PiDx66GTKdtjwmQ5dMnCK6",
    "visitor": True,
    "recordIP": True,
    "placeholder": "请不吝赐教"
}

external_links = [ 
 { 
 "name": "三刀魚", 
 "url": "http://anony.pp.ua", 
 "brief": "🏄‍ Go My Own Way." 
 }, 
 { 
 "name": "小游戏", 
 "url": "https://weigame.pp.ua", 
 "brief": "放松小游戏" 
 }, 
 { 
 "name": "云盘", 
 "url": "https://onedrive.pp.ua", 
 "brief": "Anony的云盘" 
 } 
 ] 
nav = [
    {
        "name": "HOME",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "ARCHIVES",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "ABOUT",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [ 
 { 
 "name": "Twitter", 
 "url": "https://twitter.com/Cv2Ln", 
 "icon": "gi gi-twitter" 
 }, 
 { 
 "name": "GitHub", 
 "url": "https://github.com/jhx520", 
 "icon": "gi gi-github" 
 }, 
 { 
 "name": "Weibo", 
 "url": "https://weibo.com/2975939221/", 
 "icon": "gi gi-weibo" 
 } 
 ] 

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//static.imalan.cn" />
<link rel="stylesheet" href="${static_prefix}brand_font/embed.css" />
<style>.brand{font-family:FZCuJinLFW,serif;font-weight: normal!important;}</style>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="apple-touch-icon" sizes="180x180" href="${static_prefix}apple-touch-icon.png?v=PY43YeeEKx">
<link rel="icon" type="image/png" sizes="32x32" href="${static_prefix}favicon-32x32.png?v=yyLyaqbyRG">
<link rel="icon" type="image/png" sizes="16x16" href="${static_prefix}favicon-16x16.png?v=yyLyaqbyRG">
<link rel="mask-icon" href="${static_prefix}safari-pinned-tab.svg?v=yyLyaqbyRG" color="#505050">
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
<meta name="application-name" content="無知識">
<meta name="apple-mobile-web-app-title" content="無知識">
<meta name="msapplication-TileColor" content="#000000">
<meta name="theme-color" content="#000000">
<meta name="baidu-site-verification" content="Or6aUYr0De" />
'''

footer_addon = ''

body_addon = ''