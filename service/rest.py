import time

import requests
import json

import config
from common import log
from config import socket_conf

def send_message(message):
    url = socket_conf('rest_url')

    headers = {
        'token': socket_conf('token')
    }
    payload = json.dumps({
        "msg": message
    })
    start_time = time.time()  # 记录结束时间
    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        content = response.json().get("content")
    except Exception as e:
        log.error("response content is not json")
        content = "发生错误了"
    end_time = time.time()  # 记录结束时间
    execution_time = end_time - start_time  # 计算执行时间
    log.info("[Execution Time] {:.4f} seconds", execution_time)  # 打印执行时间
    return content
