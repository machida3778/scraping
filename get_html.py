from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from time import sleep
import time

def IgnoreException(proc):
    flg = True
    while flg:
        try:
            proc()
            flg = False
        except:
            pass

def Get(patentNum: str):
    
    # ドライバを取得してブラウザでページを開く
    chrome_service = fs.Service(executable_path="./chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service)
    driver.get("https://www.j-platpat.inpit.go.jp/p0000")

    # 特許番号(B)･特許発明明細書番号(C)を選択する
    driver \
        .find_element(By.ID, "p00_srchCondtn_selDocNoInputType0") \
        .click()
    driver \
        .find_element(By.ID, "mat-option-15") \
        .click()

    # 特許番号を入力する
    driver \
        .find_element(By.ID, "p00_srchCondtn_txtDocNoInputNo0") \
        .send_keys(patentNum)

    # 照会ボタンを押下する
    driver \
        .find_element(By.ID, "p00_searchBtn_btnDocInquiry") \
        .click()

    sleep(2.0) #　読み込みに伴い、0.5秒スリープする

    for i, num in enumerate(str.split(patentNum, " ")):

        if not num: continue

        # 経過情報ボタンを押下する
        IgnoreException(lambda: \
            driver \
                .find_element(By.ID, f"patentUtltyIntnlNumOnlyLst_tableView_progReferenceInfo{i}") \
                .click()
        )

        # 操作対象を新しいウィンドウに切り替える
        newhandles = driver.window_handles
        driver.switch_to.window(newhandles[1])

        # 登録情報ボタンを押下する
        IgnoreException(lambda: \
            driver \
                .find_element(By.ID, "mat-tab-label-0-2") \
                .click()
        )

        sleep(2.0)

        # ファイルサイズが50kBを超えるか10秒経過するかしてから次のステップに進む
        t = time.time()
        while len(driver.page_source) < 50 * 10e2:
            if time.time() - t > 10:
                print(f"{num} : 10秒経過しましたが、htmlファイルのバイト数が50kBを越えませんでした。")
                break

        # htmlファイルを保存する
        with open(f"./html/page-{num}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        
        driver.close()

        # 操作対象を新しいウィンドウに切り替える
        newhandles = driver.window_handles
        driver.switch_to.window(newhandles[0])