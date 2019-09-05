#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import time
import datetime

timestamp = str(int(round((time.time()) * 1000)))


def qingtuan_list():
    """
    青豆列表
    :return:
    """
    url = "https://api.qtshe.com/taskCenter/taskUserApp/list/v1"
    headers = {
        "charset": "utf-8",
        "Accept-Encoding": "gzip",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4MTE4MTgzIiwiaWF0IjoxNTY3MjU3OTY2LCJzdWIiOiJ7XCJhY2NvdW50SWRcIjo4MTE4MTgzLFwidXNlcklkXCI6ODA0NzE3OSxcInZlcnNpb25cIjoxfSIsImV4cCI6MTU3MjQ0MTk2Nn0.gYOu2rqoAcsG-aBn_xIvwxlptBkSzwme3WF03ClBLBI",
        # "referer": "https://servicewechat.com/wx165313433c130ed7/308/page-frame.html",
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; GM1910 Build/PKQ1.190110.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand0 NetType/WIFI Language/zh_CN",
        # "Content-Length": "226",
        "Host": "api.qtshe.com",
        "Connection": "Keep-Alive",
    }

    data = {
        "appKey": "QTSHE_MINI_APP",
        "version": "4.26.0",
        "deviceId": "0.16706620504565484",
        "token": "63e543c3a3a3b88f9ff8f4e4458e3ab8",
        "timestamp": timestamp,
        "sign": "06083b399bf1f2ffce72fc2109e65b83",
        "townId": "73",
        "pageNum": "1",
        "pageSize": "20",
        "deviceOS": "android",
        "sortType": "0",
        "payType": "1"
    }
    data1 = requests.post(url=url, headers=headers, data=data).json()
    # print(data["data"]["totalPageNum"])
    pgs = data1["data"]["totalPageNum"]
    dd_list = list()
    for pg in range(1, pgs + 1):
        data["pageNum"] = pg
        data1 = requests.post(url=url, headers=headers, data=data).json()
        datas = data1["data"]["results"]
        for data in datas:
            # print(data.get("taskBaseId"))
            dd_list.append(data.get("taskBaseId"))
    print("dd_list", dd_list)
    print("len", len(dd_list))

    return dd_list


def qingtuan_tijiaozhong():
    """
    提交中列表
    :return:
    """
    url = "https://api.qtshe.com/taskCenter/taskApplyUserApp/listOngoing"
    headers = {
        "charset": "utf-8",
        "Accept-Encoding": "gzip",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4MTE4MTgzIiwiaWF0IjoxNTY3MjU3OTY2LCJzdWIiOiJ7XCJhY2NvdW50SWRcIjo4MTE4MTgzLFwidXNlcklkXCI6ODA0NzE3OSxcInZlcnNpb25cIjoxfSIsImV4cCI6MTU3MjQ0MTk2Nn0.gYOu2rqoAcsG-aBn_xIvwxlptBkSzwme3WF03ClBLBI",
        # "referer": "https://servicewechat.com/wx165313433c130ed7/308/page-frame.html",
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; GM1910 Build/PKQ1.190110.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand0 NetType/WIFI Language/zh_CN",
        # "Content-Length": "188",
        "Host": "api.qtshe.com",
        "Connection": "Keep-Alive",
    }

    data = {
        "appKey": "QTSHE_MINI_APP",
        "version": "4.26.0",
        "deviceId": "0.16706620504565484",
        "token": "63e543c3a3a3b88f9ff8f4e4458e3ab8",
        "timestamp": "1567591299975",
        "sign": "2aa74711cf52eabc59adbe0a5e052476",
        "pageNum": "1",
        "pageSize": "10",
    }
    data1 = requests.post(url=url, headers=headers, data=data).json()
    # print(data1)
    pgs = data1["data"]["totalPageNum"]
    dd_list = list()
    for pg in range(1, pgs + 1):
        data["pageNum"] = pg
        data1 = requests.post(url=url, headers=headers, data=data).json()
        datas = data1["data"]["results"]
        for data in datas:
            # print(data.get("taskBaseId"))
            dd_list.append(data.get("taskBaseId"))
    taskBaseIds.extend(dd_list)
    return dd_list


taskBaseIds = list()


def qingtuan_lingqv(taskBaseId):
    """
    获取taskApplyId
    :return:
    """
    url = "https://api.qtshe.com/taskCenter/taskApplyUserApp/add"
    headers = {
        "charset": "utf-8",
        "Accept-Encoding": "gzip",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4MTE4MTgzIiwiaWF0IjoxNTY3MjU3OTY2LCJzdWIiOiJ7XCJhY2NvdW50SWRcIjo4MTE4MTgzLFwidXNlcklkXCI6ODA0NzE3OSxcInZlcnNpb25cIjoxfSIsImV4cCI6MTU3MjQ0MTk2Nn0.gYOu2rqoAcsG-aBn_xIvwxlptBkSzwme3WF03ClBLBI",
        # "referer": "https://servicewechat.com/wx165313433c130ed7/308/page-frame.html",
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; GM1910 Build/PKQ1.190110.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand2 NetType/WIFI Language/zh_CN",
        # "Content-Length": "245",
        "Host": "api.qtshe.com",
        "Connection": "Keep-Alive",
    }

    data = {
        "appKey": "QTSHE_MINI_APP",
        "version": "4.26.0",
        "deviceId": "0.16706620504565484",
        "token": "63e543c3a3a3b88f9ff8f4e4458e3ab8",
        "timestamp": timestamp,
        "sign": "e4543eb65239081b392091e01ff39ddb",
        "taskBaseId": taskBaseId,
        "thirdPartyId": "",
        "deviceOS": "android",
        "authorizedKey": "",
        "ticketDetailId": "",
    }

    data = requests.post(url=url, headers=headers, data=data).json()
    # print(data)
    if str(data["code"]) == "4000":
        datas = data["data"]["taskApplyId"]
        taskBaseIds.append(datas)
        print(datas)


def qingtuan_tijiao(taskApplyId):
    url = "https://api.qtshe.com/taskCenter/taskApplyUserApp/addResult"
    headers = {
        "charset": "utf-8",
        "Accept-Encoding": "gzip",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4MTE4MTgzIiwiaWF0IjoxNTY3MjU3OTY2LCJzdWIiOiJ7XCJhY2NvdW50SWRcIjo4MTE4MTgzLFwidXNlcklkXCI6ODA0NzE3OSxcInZlcnNpb25cIjoxfSIsImV4cCI6MTU3MjQ0MTk2Nn0.gYOu2rqoAcsG-aBn_xIvwxlptBkSzwme3WF03ClBLBI",
        # "referer": "https://servicewechat.com/wx165313433c130ed7/308/page-frame.html",
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; GM1910 Build/PKQ1.190110.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand2 NetType/WIFI Language/zh_CN",
        # "Content-Length": "644",
        "Host": "api.qtshe.com",
        "Connection": "Keep-Alive",
    }

    data = {
        "appKey": "QTSHE_MINI_APP",
        "version": "4.26.0",
        "deviceId": "0.16706620504565484",
        "token": "63e543c3a3a3b88f9ff8f4e4458e3ab8",
        "timestamp": timestamp,
        "sign": "8f95c9a11c8e549620493992670edd5a",
        "taskApplyId": taskApplyId,
        "condition": '[{"title":"在留言框内提交你认为的正确答案即可完成任务，答对即得薪资！（留言“a”或“b”）\n","type":1,"imgList":null,"content":"a"}]',
    }
    data = requests.post(url=url, headers=headers, data=data).json()
    print(data)


if __name__ == '__main__':
    ddlists = qingtuan_list()
    for ddlist in ddlists:
        qingtuan_lingqv(ddlist)

    qingtuan_tijiaozhong()
    print("taskBaseIds", taskBaseIds)

    for taskBaseId in taskBaseIds:
        qingtuan_tijiao(taskBaseId)

