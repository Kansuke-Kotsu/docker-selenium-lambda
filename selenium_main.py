# Import Base libraries
from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By

# Import 
import selenium_Able 
import selenium_REINS
import selenium_RNP
import selenium_TAKUTO
import selenium_Tokyu

def main(chromesetting, ):
    # それぞれの関数を実行して、結果を取得する
    output_Able = selenium_Able.get()
