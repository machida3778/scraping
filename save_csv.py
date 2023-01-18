from bs4 import BeautifulSoup
import glob
import pandas as pd
import load_input

def Save(headers: list):

    headers = ["Page"] + headers
    df = pd.DataFrame(columns=headers)

    path = glob.glob("./html/*.html")
    patentNum = load_input.load()

    a, b = len("./html\\page-"), len(".html")
    path = filter(lambda x: x[a:-b] in patentNum, path)
    path = sorted(path, key=lambda x: patentNum.index(x[a:-b]))

    for p in path:

        name = p.replace(".html", "").replace("./html\\", "")  
        html = open(p, "r", encoding="utf-8_sig")
        soup = BeautifulSoup(html, "html.parser")
        tr = soup.find_all("tr")

        # \u2002 is a space
        try:
            data = [[i.replace("\u2002", "") for i in j.text.split("\n") if i] for j in tr]
            data = list(filter(lambda x: x[0] in headers, data))
            data = [[name] + ["".join(i[1:]) for i in data]]
            data = pd.DataFrame(data, columns=headers)
            df = pd.concat([df, data])
        except ValueError as e:
            print(e)
            print(f"{p}に必要な情報が含まれていない可能性があります。処理は続行されます")

    msgFlg = True
    while True:
        try:
            df.to_csv(f'./csv/patents.csv', encoding='utf_8_sig', index=False)
            break
        except PermissionError:
            if msgFlg:
                print("Excelファイルを閉じてください")
                msgFlg = False
