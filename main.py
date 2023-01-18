import load_input
import get_html
import save_csv
import csv

if __name__ == "__main__":
    
    # input.csvファイルの読み込み
    max_get = 2
    patentNum = load_input.load(max_get)

    # 対象のhtmlファイルをスクレイピング
    step = 100
    for i in range(0, len(patentNum), step):
        last_idx = i + step
        if len(patentNum) <= last_idx:
            last_idx = len(patentNum)
        
        str_num = " ".join(patentNum[i:last_idx])
        get_html.Get(str_num)

    # 全htmlファイルをcsvファイルに変換して保存する
    headers = [ "出願記事",
                "登録記事",
                "権利者記事",
                "発明等の名称(漢字)記事",
                "請求項の数記事",
                "登録細項目記事",
                "最終納付年分記事",
                "更新日付"]
    save_csv.Save(headers)