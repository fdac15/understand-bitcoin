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
urls= requests.get(url,headers=headers)
parsed_json=json.loads(urls.text)
repo_count= parsed_json['total_count']
repositories=[]
while(1):
	time.sleep(0.72001)
	temp_url=url+'&page='+str(page)
	urls= requests.get(temp_url,headers=headers)
	page+=1
	parsed_json=json.loads(urls.text)
	repos= parsed_json['items']
	for repo in repos:
		repositories.append(repo['url'])
	if (page-1)*30 > repo_count:
		break
branches=[]
for repo in repositories:
	time.sleep(0.72001)
	repo_tmp=repo+"/branches"
	repo_json= requests.get(repo_tmp,headers=headers)
	parsed_json=json.loads(repo_json.text)
	for br in parsed_json:
		branches.append(br['commit']['url'])
		print br['commit']['url']
dates_lines={}
dates_commits={}
commits = open("commits.txt",'w')
for branch in branches:
	time.sleep(0.72001)
	commits.write(branch)
	commits.write("\n")
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
lines = open("lines_per_date.csv", 'w')
for day in dates_lines:
	lines.write(str(day))
	lines.write(',')
	lines.write(str(dates_lines[day]))
	lines.write('\n')
commits = open("commits_per_date.csv", 'w')
for day in dates_commits:
	commits.write(str(day))
	commits.write(",")
	commits.write(str(dates_commits[day]))
	commits.write('\n')

		