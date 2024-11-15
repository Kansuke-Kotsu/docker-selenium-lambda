from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def get(name, chromedriver_path, selected_headless):
    print("-------- エイブル --------")
    print(name)
    # Chromeオプションを設定
    chrome_options = Options()
    if selected_headless == "非表示":
        chrome_options.add_argument("--headless")
    # サービスを作成
    service = Service(chromedriver_path)
    # ブラウザを起動
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 指定したURLにアクセス
    url = "https://heya.a-hosho.co.jp/"
    USERNAME = '0368246611'
    PASSWORD = 'D7dk8KEC'

    step = 0

    try:
        driver.get(url)
        step = 1
        # ユーザー名とパスワードを入力（フィールドをクリアしてから入力）
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login_id')))
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))
        email_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)

        # フォームを送信（クリックメソッドを使用）
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@src="./img/button_login.jpg"]')))
        login_button.click()

        print("ログイン完了")
        step = 2
        # 検索ワードを入力
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="building_name"]'))
        )
        search_input.clear()
        search_input.send_keys(name)  # 検索したいワードを入力

        # 検索ボタンを押す
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="search_button"]/span/span')))
        search_button.click()
        print("検索ボタン押下")
        
        result = []
        try:
            div_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr.one_room_tr'))
            )
            for div_element in div_elements[:3]:
                home_text = div_element.find_element(By.CSS_SELECTOR, 'td.building_name_td').text
                detail_url = div_element.find_element(By.CSS_SELECTOR, 'a.detail_button')
                detail_url = detail_url.get_attribute('href')
                print(home_text)
                print(detail_url)
                result.append(home_text)
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

'''
results = [
        ("サイト名：", "リンク", "物件名", "その他詳細")
    ]
'''
#result = get(name="ハイツ")
#print(result)
