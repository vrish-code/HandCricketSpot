import requests as r
import json

with open("scriptsmodules/apiKeys.json", "r", encoding='utf-8') as f:
    URLS=json.load(f)

def patch(data):
    resp=r.patch(URLS["json"], json=data)


def get():
    resp=r.get(URLS["json"])
    return resp.json()