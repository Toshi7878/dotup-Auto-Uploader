import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options # オプションを使うために必要

if len(sys.argv) < 2:
    #引数がない場合の処理。今回は何もしない。
    pass
else:
	#sys.argv[1]に指定ファイルのフルパスが入る。Outlookでリンクを張るために<>で囲う。
	file_path = sys.argv[1]

	option = Options()                          # オプションを用意
	option.add_argument('--headless')           # ヘッドレスモードの設定を付与
	chrome = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
	chrome.get("https://dotup.org/")
	chrome.find_elements(By.NAME,"upfile")[0].send_keys(file_path)
	chrome.find_element(By.CSS_SELECTOR, 'input[value="アップロード"]').click()
	# 定義済みの条件で待機
	wait = WebDriverWait(chrome, 20)

	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="https://dotup.org/uploda/dotup.org"]')))

	pyperclip.copy(chrome.find_element(By.CSS_SELECTOR, 'a[href*="https://dotup.org/uploda/dotup.org"]').text.replace('.html', ''))
	chrome.quit()
