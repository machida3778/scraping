import csv

def load(max=None):
    patentNum = []

    if max == 0: return patentNum

    with open("./csv/input.csv", encoding="utf-8", newline="") as f:
        for i, num in enumerate(csv.reader(f)):
            patentNum += num
            if max is not None and i + 1 >= max: break
    
    return patentNum