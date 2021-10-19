import json

import requests


def scrape():
    datas = []
    response = requests.get("https://nwdb.info/db/recipes/page/1.json?sort=recipe-skill-level_desc")
    content = response.json()
    datas.append(content["data"])
    for page in range(2, content["pageCount"] + 1):
        print(f"requesting page {page}")
        res = requests.get(f"https://nwdb.info/db/recipes/page/{page}.json?sort=recipe-skill-level_desc")
        datas.append(res.json()["data"])

    with open("pickle.json", "w+") as f:
        print("writing file")
        f.write(json.dumps([item for sublist in datas
                            for item in sublist]))

    print("done")


def transform():
    with open("pickle.json", "r") as f:
        data = json.loads(f.read())

    print([d["id"] for d in data])
    pass


if __name__ == '__main__':
    transform()
