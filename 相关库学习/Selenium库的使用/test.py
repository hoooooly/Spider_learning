list = [
    {
        "domain": ".baidu.com",
        "expiry": 1624077494,
        "httpOnly": False,
        "name": "BA_HECTOR",
        "path": "/",
        "secure": False,
        "value": "2d0lah0k8l0l04650k1gcqpl60r",
    },
    {
        "domain": ".baidu.com",
        "expiry": 1655609894,
        "httpOnly": False,
        "name": "BAIDUID_BFESS",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "value": "08F0DBA3E79D4831F6AC7ABA6503BD5A:FG=1",
    },
    {
        "domain": ".baidu.com",
        "httpOnly": False,
        "name": "H_PS_PSSID",
        "path": "/",
        "secure": False,
        "value": "34131_33763_34004_33607_34134_34111",
    },
    {
        "domain": ".baidu.com",
        "expiry": 1655609893,
        "httpOnly": False,
        "name": "BAIDUID",
        "path": "/",
        "secure": False,
        "value": "08F0DBA3E79D4831F6AC7ABA6503BD5A:FG=1",
    },
    {
        "domain": ".baidu.com",
        "expiry": 3771557540,
        "httpOnly": False,
        "name": "BIDUPSID",
        "path": "/",
        "secure": False,
        "value": "08F0DBA3E79D4831A2B7495A40432FE9",
    },
    {
        "domain": ".baidu.com",
        "expiry": 3771557540,
        "httpOnly": False,
        "name": "PSTM",
        "path": "/",
        "secure": False,
        "value": "1624073892",
    },
    {
        "domain": "www.baidu.com",
        "expiry": 1624937894,
        "httpOnly": False,
        "name": "BD_UPN",
        "path": "/",
        "secure": False,
        "value": "12314753",
    },
    {
        "domain": "www.baidu.com",
        "httpOnly": False,
        "name": "BD_HOME",
        "path": "/",
        "secure": False,
        "value": "1",
    },
]


def parse_cookies(json_cookies):
    """将获取到的json格式的cookies提取"""
    cookie = ""
    for json_cookie in json_cookies:
        cookie = cookie + str(json_cookie['name']) + ":" + str(json_cookie['value']) + ";"
    return cookie

print(parse_cookies(list))