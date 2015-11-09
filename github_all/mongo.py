from pymongo import MongoClient
import sys
import requests
import json
import array
import time
from dateutil import parser


client = MongoClient()
db = client.fdac
table=client.fdac.repos
false=False



headers = {'Authorization':'token %s' % 'ec9d1d664e94d3fe0f6d3a51f79bbcfa407d6e4c'}
repo="https://api.github.com/repos/ckolivas/cgminer/branches"
repo_json= requests.get(repo,headers=headers)
parsed_json=json.loads(repo_json.text)
branches=[]
for br in parsed_json:
	branches.append(br['commit']['url'])
	print br['commit']['url']
commits=branches
for commit in commits:
	time.sleep(0.72001)
	commit_json= requests.get(commit,headers=headers)
	parsed_json=json.loads(commit_json.text)
	table.insert_one(parsed_json)
	for i in range(len(parsed_json['parents'])):
		branches.append(parsed_json['parents'][i]['url'])