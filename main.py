# Import Base libraries
from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
import json

# Import actual logic
#from selenium_main import main

def handler(event=None, context=None):
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

    # Extract user inputs from the event object.  Assume JSON format.
    user_inputs = json.loads(event['body']) if 'body' in event else {}

    # Chrome設定 ==> スクレイピング結果を一つの配列で取得
    # outputs = main(chromesetting=chrome)

    chrome.get("https://www.google.com/")
    response = {
        'statusCode': 200,
        'body': chrome.find_element(by=By.XPATH, value="//html").text,
        'headers': {
            'Content-Type': 'text/plain'
        }
    }

    return response
