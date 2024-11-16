# Import Base libraries
from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
import json

import selenium_main

def handler(event, context=None):
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService("/opt/chromedriver")

    options.binary_location = '/opt/chrome/chrome'
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    chrome = webdriver.Chrome(options=options, service=service)
            
    # ユーザーからの入力を取得
    user_input = event.get('queryStringParameters', {}).get('text')
    if not user_input:
        response = {
            'statusCode': 200,
            'body': "入力内容を確認してください",
            'headers': {
                'Content-Type': 'text/plain'
            }
        }
        
    try:
        outputs = selenium_main.main(chromesetting=chrome, user_input=user_input)
        response = {
            'statusCode': 200,
            'body': outputs[0],
            'headers': {
                'Content-Type': 'text/plain'
            }
        }
    except:
        response = {
            'statusCode': 500,
            'body': "errorだよ",
            'headers': {
                'Content-Type': 'text/plain'
            }
        }

    return response
