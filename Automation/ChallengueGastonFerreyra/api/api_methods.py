import requests
from requests import request

def get(url):
	return requests.get(url=url)

def post(url, body):
	return requests.post(url=url, json=body)