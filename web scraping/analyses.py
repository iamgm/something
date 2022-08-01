import os
import csv
import json
import requests
import datetime as dt


def collect_data():
    date = dt.datetime.now().strftime("%d_%M_%Y")
    res = requests.get("https://www.lifetime.plus/api/analysis2")

    with open(f"info_{date}.json", "w", encoding ='utf8') as file:
        json.dump(res.json(), file, indent=4, ensure_ascii = False)

    categories = res.json()["categories"]
    result = []
    for c in categories:
        name = c["name"]
        items = c["items"]

        for i in items:
            item_name =  i["name"].strip()
            item_price = i["price"]
            item_desc = i["description"].strip()
            item_time = i["days"]
            item_bio = i["biomaterial"]
            item_desc = item_desc.replace("β", "betta")
            item_desc = item_desc.replace("α", "alpha")
            item_desc = item_desc.replace("γ", "gamma")
            result.append((name, item_name, item_bio, \
                          item_desc, item_price, item_time))
    
    with open(f"result_{date}.csv", "a", encoding ='cp1251') as file:
        writer = csv.writer(file)

        writer.writerow(
                (
                    "Категория",
                    "Анализ",
                    "Биоматериал",
                    "Описание",
                    "Стоимость",
                    "Готовность (дней)"
                )
            )

        writer.writerows(result)


def main():
    collect_data()


if __name__ == '__main__':
    main()
