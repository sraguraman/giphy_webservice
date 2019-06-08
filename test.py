from flask import Flask
import requests
import json


def query_giphy():
    url = 'http://api.giphy.com/v1/gifs/search'
    key = 'vIa6iVvRwwONNxkoXfSvGnyKuGvDgg3d'
    num_requests_allowed = 5
    payload = {'q': 'ryangosling', 'api_key': 'vIa6iVvRwwONNxkoXfSvGnyKuGvDgg3d'}
    r = requests.get(url, params=payload)
    print(r.json())


query_giphy()