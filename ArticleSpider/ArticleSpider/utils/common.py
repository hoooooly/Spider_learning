import hashlib


def get_md5(url: str) -> str:
    """
    用于将长字符串比如网址，转成长度固定的MD5字符串

    :param url 网页或图片的链接地址，字符串类型

    :return 返回生成的mod5字符串
    """
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)

    return m.hexdigest()

# test
# if __name__ == '__main__':
#     m = get_md5("https://img2020.cnblogs.com/news/66372/202109/66372-20210904091640217-779609551.png")
#     print(m)  # 5a5ecad7f153a8114f6086e34f709032
