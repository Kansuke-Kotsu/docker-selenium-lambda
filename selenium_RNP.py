from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def get(name, place_1, chromedriver_path, selected_headless):
    print("-------- RNP --------")
    # Chromeオプションを設定
    chrome_options = Options()
    if selected_headless == "非表示":
        chrome_options.add_argument("--headless")
    # サービスを作成
    service = Service(chromedriver_path)
    # ブラウザを起動
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 指定したURLにアクセス
    url = "https://www.realnetpro.com/index.php"
    USERNAME = 'wandyidpw'
    PASSWORD = 'Y5vPxXMD'
    driver.get(url)

    step = 0
    try:
        driver.get(url)
        step = 1
        # ユーザー名とパスワードを入力（フィールドをクリアしてから入力）
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'id')))
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'pass')))
        email_field.clear()
        email_field.send_keys(USERNAME)
        password_field.clear()
        password_field.send_keys(PASSWORD)

        # フォームを送信（クリックメソッドを使用）
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login_button"]'))
        )
        login_button.click()

        sleep(3)

        print("ログイン完了")
        step = 2
        # 地域選択
        change_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class="change_pref pref_area_buttun"]'))
        )
        change_button.click()
        # ユーザーが入力する都道府県
        input_prefecture = place_1
        # 都道府県とvalue属性の対応を辞書で定義
        prefecture_values = {
            "北海道": "01",
            "青森県": "02",
            "岩手県": "03",
            "宮城県": "04",
            "秋田県": "05",
            "山形県": "06",
            "福島県": "07",
            "茨城県": "08",
            "栃木県": "09",
            "群馬県": "10",
            "埼玉県": "11",
            "千葉県": "12",
            "東京都": "13",
            "神奈川県": "14",
            "新潟県": "15",
            "富山県": "16",
            "石川県": "17",
            "福井県": "18",
            "山梨県": "19",
            "長野県": "20",
            "岐阜県": "21",
            "静岡県": "22",
            "愛知県": "23",
            "三重県": "24",
            "滋賀県": "25",
            "京都府": "26",
            "大阪府": "27",
            "兵庫県": "28",
            "奈良県": "29",
            "和歌山県": "30",
            "鳥取県": "31",
            "島根県": "32",
            "岡山県": "33",
            "広島県": "34",
            "山口県": "35",
            "徳島県": "36",
            "香川県": "37",
            "愛媛県": "38",
            "高知県": "39",
            "福岡県": "40",
            "佐賀県": "41",
            "長崎県": "42",
            "熊本県": "43",
            "大分県": "44",
            "宮崎県": "45",
            "鹿児島県": "46",
            "沖縄県": "47"
        }
        # 該当するチェックボックスのvalue属性を取得
        value = prefecture_values.get(input_prefecture)
        #print(value)
        # すべてのチェックボックスを取得
        checkboxes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//label[@class="input-item"]/input[@type="checkbox"]')))
        #print("get")
        # 指定した都道府県のチェックボックスにチェックを付け、それ以外のチェックを外す
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == value:
                if not checkbox.is_selected():
                    checkbox.click()
                    print(f"{input_prefecture}のチェックボックスを選択しました")
            else:
                if checkbox.is_selected():
                    checkbox.click()
        confirm_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="確定"]')))
        confirm_button.click()

        sleep(3)
        
        # 検索ワードを入力
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'top_free'))
        )
        search_input.clear()
        search_input.send_keys(name)  # 検索したいワードを入力
        #print("検索ワード入力")

        # 検索ボタンを押す
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class="submit free_word_submit"]/span'))
        )
        search_button.click()
        print("検索ボタン押下")

        result = []
        try:
            # main_contents内のdiv要素を取得して表示する
            div_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.main_contents div.one_building'))
            )
            for div_element in div_elements[:3]:
                home_text = div_element.find_element(By.CSS_SELECTOR, 'div.building_name').text
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

#get(name="サンハイツ藤", place_1="東京都")