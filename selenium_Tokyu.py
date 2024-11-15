from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def get(name, chromedriver_path, selected_headless):
    print("-------- 東急 --------")
    # Chromeオプションを設定
    chrome_options = Options()
    if selected_headless == "非表示":
        chrome_options.add_argument("--headless")
    # サービスを作成
    service = Service(chromedriver_path)
    # ブラウザを起動
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 指定したURLにアクセス
    url = "https://map.cyber-estate.jp/mediation/login.asp?ggid=813054"
    USERNAME = '1041928277'
    PASSWORD = '1041928277'

    step = 0

    try:
        driver.get(url)
        step = 1
        # ユーザー名とパスワードを入力（フィールドをクリアしてから入力）
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtLoginId"]')))
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtLoginPass"]')))
        email_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)

        # フォームを送信（クリックメソッドを使用）
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@src="images/btn_login_off.gif"]')))
        login_button.click()
        print("ログイン完了")
        step = 2
        # 検索ワードを入力
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtSearchBkn"]'))
        )
        search_input.clear()
        search_input.send_keys(name)  # 検索したいワードを入力

        # 検索ボタンを押す
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//img[@alt="検索"]')))
        search_button.click()
        print("検索ボタン押下")

        result = []
        try:
            # main_contents内のdiv要素を取得して表示する
            div_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td.big'))
            )
            for div_element in div_elements[:3]:
                home_text = div_element.find_element(By.CSS_SELECTOR, 'a').text
                result.append(home_text)
            print(result)
            print("結果あり")
        except:
            result.append("結果なし")
            print("結果なし")
        
    except Exception as e:
        if step == 0: 
            result.append("アクセスに失敗しました。ネットワーク or PC負荷を確認してください")
        elif step == 1:
            result.append("ログインに失敗しました。パスワードが変更されてないか確認してください")
        elif step == 2:
            result.append("ログイン完了後、検索に失敗しました。何度も失敗するようであれば連絡ください")

    driver.quit()  # ブラウザを閉じる

    return result

#get(name="ハイツ")
