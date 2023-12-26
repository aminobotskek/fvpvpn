import requests
class Client():
	def __init__(self):
		self.api="https://app-how-to-use-it.com"
		self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def get_proxy_list(self):
		return requests.get(f"{self.api}/FVPVPN.json",headers=self.headers).json()