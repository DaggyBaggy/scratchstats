import requests
import json

def getprojectinfo(id):
  url = f'https://scratchdb.lefty.one/v3/project/info/{id}'
  response = (requests.get(url)).text
  parsedjson = json.loads(response)
  return parsedjson

def getuserinfo(username):
  url = f'https://scratchdb.lefty.one/v3/user/info/{username}'
  response = (requests.get(url)).text
  parsedjson = json.loads(response)
  return parsedjson