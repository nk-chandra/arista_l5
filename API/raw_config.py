import requests,pprint

url = "https://192.168.0.21/command-api"

commands = open("eth3.json","r")

response = requests.post(url,auth=('arista','arista33rq'),data=commands,verify=False)

pprint.pprint(response.text)
