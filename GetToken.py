import requests
import json
from pprint import pprint
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")

URL = "https://sandboxdnac2.cisco.com"
AuthorizationAPI = "/dna/system/api/v1/auth/token"
InterfaceAPI = "/dna/intent/api/v1/interface"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

TokenAuth = URL + AuthorizationAPI

response = requests.post(TokenAuth, auth=HTTPBasicAuth(username,password), headers=headers, data=payload, verify=False)

TokenJSON = response.json()

Token = TokenJSON['Token']

Interfaces = URL + InterfaceAPI

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': Token
}

response = requests.get(Interfaces, headers=headers, data=payload, verify=False)

Reply = response.json()


pprint(Reply)
