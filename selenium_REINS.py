from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def get(name, place_1, place_2, chromedriver_path, selected_headless):
    print("-------- レインズ --------")
    # Chromeオプションを設定
    chrome_options = Options()
    if selected_headless == "非表示":
        chrome_options.add_argument("--headless")
    # サービスを作成
    service = Service(chromedriver_path)
    # ブラウザを起動
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 指定したURLにアクセス
    url = "https://system.reins.jp/login/main/KG/GKG001200"
    USERNAME = '770000067230'
    PASSWORD = 'qD4iSz2w'

    result = []
    step = 0

    try:
        driver.get(url)
        step = 1
        # ユーザー名とパスワードを入力（フィールドをクリアしてから入力）
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__13"]')))
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__16"]')))
        email_field.send_keys(USERNAME)
        password_field.clear()
        password_field.send_keys(PASSWORD)
        # チェックボックスのラベル要素を取得
        checkbox_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[@class="custom-control-label" and text()="所属機構の規程及びガイドラインを遵守します"]')))
        # ラベル要素に関連するチェックボックスを選択
        checkbox_label.click()
        # フォームを送信（クリックメソッドを使用）
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="ログイン"]')))
        login_button.click()

        print("ログイン完了")
        step = 2
        # 賃貸物件検索ボタン
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="賃貸 物件検索"]')))
        search_button.click()

        # 物件種別 # Selectクラスを使用して、<select>タグを操作
        type_select = login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__178"]')))
        type_select = Select(type_select)
        type_select.select_by_value("03")

        # 所在地
        area_1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__210"]')))
        area_1.send_keys(place_1)
        area_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__214"]')))
        area_2.send_keys(place_2)
        area_3 =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__222"]')))
        area_3.send_keys(name)

        # 検索ボタン
        search_2_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="検索"]')))
        search_2_button.click()
        print("検索ボタン押下")

        div_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.p-table-body-row'))
        )
        if len(div_elements) > 0:
            for div_element in div_elements[:3]:
                # 12番目の行を取得する
                row = div_element  # 12番目の要素はインデックス11に該当する
                # p-table-body-item要素を取得する
                items = row.find_elements(By.CSS_SELECTOR, '.p-table-body-item')
                if len(items) > 11:
                    # 12番目のitemのテキストを取得する
                    item_text = items[11].text
                    result.append(item_text)
            print("結果あり")
        else:
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