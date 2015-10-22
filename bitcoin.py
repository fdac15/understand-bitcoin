#!/usr/bin/env python3

from git import *
import datetime
import os
import time
import operator
from collections import *

class nesteddict(dict):
	def __missing__(self,key):
		self[key] = nesteddict()
		return self[key]


repo = Repo("bitcoin")
tree = repo.tree()
paths = [obj.path for obj in tree]

lst = nesteddict()
counter = dict()

latest_commits = {}

for commit in repo.iter_commits(paths=paths):
	for f in commit.stats.files.keys():
		p = f[:f.index('/')] if '/' in f else f
		name = commit.committer.name
		date = str(time.asctime(time.gmtime(commit.committed_date)))
#.formatter("%(asctime)s","%Y-%m-%d")
#		print(newtime)
		location = f
		if not location in counter:
			counter[location] = 1
		else:
			counter[location] += 1
		lst[name][date] = location
		latest_commits[p] = commit
	if len(latest_commits) == len(paths):
		break

print("List of Contributers:\n")
for i in lst:
	print("\n\n")
	print("NAME: ", i, "---- Contributions: ", len(lst[i]))
	for j in lst[i]:
		print(j," : ", lst[i][j])
#		print(lst[i][j])
print("\n\n")
print("Number of changes\n")
#counter2 = sorted(counter.items(), key=operator.itemgetter(1))
for i in counter:
	print(i, counter[i])

o = repo.remotes.origin
o.pull()

#master = repo.head.reference
#print master.log()

#print(master.commit.message)
