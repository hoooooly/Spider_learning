import requests

url = "https://www.zhipin.com/job_detail/?query=python&city=101190100&industry=&position="

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
    "referer": "https://www.zhipin.com/job_detail/?query=python&city=101190100&industry=&position="
}

r = requests.get(url=url, headers=headers)

print(r.text)
