import get_html
import save_csv
import csv

if __name__ == "__main__":
    
    # input.csvファイルの読み込み
    patentNum = ""
    with open("./csv/input.csv", encoding="utf-8", newline="") as f:
        for i in csv.reader(f):
            patentNum += " ".join(i) + " "

    # 対象のhtmlファイルをスクレイピング
    get_html.Get(patentNum)

    # htmlファイルをcsvファイルに変換して保存する
    headers = [ "出願記事",
                "発明等の名称(漢字)記事",
                "請求項の数記事",
                "登録細項目記事",
                "最終納付年分記事" ]
    save_csv.Save(headers)