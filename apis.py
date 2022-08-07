import requests


class NinjaAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.api-ninjas.com/v1/"
        self.api_key = api_key

        session = requests.Session()
        self.headers = {"X-Api-Key": api_key}
        self.session = session

    def fact(self, num=1):
        r = requests.get(self.base_url + f"facts?limit={num}", headers=self.headers)
        list_facts = r.json()
        out = []
        for i in range(0, num):
            item = list_facts[i]["fact"]
            out.append(item)
        if num > 1:
            return out
        else:
            return out[0]

    def quote(self, category=""):

        r = requests.get(
            self.base_url + f"quotes?category={category}", headers=self.headers
        )
        data = r.json()[0]

        text = data["quote"]
        author = data["author"]
        cat = data["category"]
        return text, author, cat
