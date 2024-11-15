# Import Base libraries
from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
import json

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

    # ユーザーからの入力を取得
    user_input = json.dumps(event, indent=2)
    response = {
            'statusCode': 200,
            'body': event["key1"],
            'headers': {
                'Content-Type': 'text/plain'
            }
        }
        
    """try:
        chrome = webdriver.Chrome(options=options, service=service)
        chrome.get(user_input)
        body = chrome.find_element(by=By.XPATH, value="//html").text
        response = {
            'statusCode': 200,
            'body': body,
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
        }"""

    return response
