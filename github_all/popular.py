#!/usr/bin/python
import re
import urllib2
import sys
import requests
import json
import array
import time
from dateutil import parser
#urls = urllib2.urlopen("https://api.github.com/search/repositories?q=bitcoin+miner").read()
page=1
url='https://api.github.com/search/repositories?q=bitcoin+miner'
params  = {'page': page, 'per_page': 30}
headers = {'Authorization':'token %s' % 'ec9d1d664e94d3fe0f6d3a51f79bbcfa407d6e4c'}
repositories=["https://api.github.com/repos/ufasoft/coin","https://api.github.com/repos/gr0bi42/BTCMiner", "https://api.github.com/repos/TheSeven/Modular-Python-Bitcoin-Miner","https://api.github.com/repos/progranism/Open-Source-FPGA-Bitcoin-Miner","https://api.github.com/repos/phoenix2/phoenix","https://api.github.com/repos/m0mchil/poclbm","https://api.github.com/repos/colinrgodsey/scalaminer","https://api.github.com/repos/ckolivas/cgminer","https://api.github.com/repos/Diablo-D3/DiabloMiner","https://api.github.com/repos/luke-jr/bfgminer"]
i=0
for repo in repositories:
	i=i+1
	time.sleep(0.72001)
	repo_tmp=repo+"/branches"
	repo_json= requests.get(repo_tmp,headers=headers)
	parsed_json=json.loads(repo_json.text)
	branches=[]
	for br in parsed_json:
		branches.append(br['commit']['url'])
		print br['commit']['url']
	dates_lines={}
	dates_commits={}
	for branch in branches:
		time.sleep(0.72001)
		branch_json= requests.get(branch,headers=headers)
		parsed_json=json.loads(branch_json.text)
		if len(parsed_json['parents']) != 0:
			branches.append(parsed_json['parents'][0]['url'])
		date=parser.parse(parsed_json['commit']['author']['date']).date()
		if date in dates_lines: 
			dates_lines[date]+=parsed_json['stats']['total']
		else:
			dates_lines[date]=parsed_json['stats']['total']
		if date in dates_commits:
			dates_commits[date]+=1
		else:
			dates_commits[date]=1
		print branch +" "+ str(date)
	line_name="lines_per_date_"+str(i)+".csv"
	lines = open(line_name, 'w')
	lines.write(repo)
	lines.write('\n')
	for day in dates_lines:
		lines.write(str(day))
		lines.write(',')
		lines.write(str(dates_lines[day]))
		lines.write('\n')
	commits_name="commits_per_date_"+str(i)+".csv"
	commits = open(commits_name, 'w')
	commits.write(repo)
	commits.write('\n')
	for day in dates_commits:
		commits.write(str(day))
		commits.write(",")
		commits.write(str(dates_commits[day]))
		commits.write('\n')

		