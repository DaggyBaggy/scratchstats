# ScratchStats
### First of all, credits:
- @cagboo on scratch and DaggyBaggy on github for writing some of the code for this project
- DatOneLefty for ScratchDB API, which powers the entire project.

### How to install ScratchStats:
To install write this in command promp / shell:
```
pip install scratchstats --upgrade
```
### How to use ScratchStats:
```
import scratchstats as ss

project_info = ss.getprojectinfo(PROJECT_ID)

print(project_info)
```
#### OR
```
import scratchstats as ss

user_info = ss.getuserinfo(USERNAME)

print(user_info)
```
### After that you can look at the data in the console:
##### Example, project info, I put in "100000":
```
# ScratchStats
### First of all, credits:
- @cagboo on scratch and DaggyBaggy on github for writing some of the code for this project
- DatOneLefty for ScratchDB API, which powers the entire project.

### How to install ScratchStats:
To install write this in command promp / shell:
```
pip install git+https://github.com/DaggyBaggy/scratchstats
```
### How to use ScratchStats:
```
import scratchstats as ss

project_info = ss.getprojectinfo(PROJECT_ID)

print(project_info)
```
#### OR
```
import scratchstats as ss

user_info = ss.getuserinfo(USERNAME)

print(user_info)
```
### After that you can look at the data in the console:
##### Example, project info, I put in "100000":
```
{"id":100000,"sys_id":3933088,"username":"pinkhollyspark","title":"happy_birthday_funkadelihippo!!!!!!!!!!!!!!","description":"Happy birthday funkadelihippo!!!!!!!!","instructions":"","public":true,"comments_allowed":true,"times":{"created":"2008-02-15T10:49:33.000Z","modified":"2016-07-05T15:11:39.000Z","shared":"2008-02-15T10:49:33.000Z","last_check":"2022-04-23T13:58:42.000Z","last_metadata_check":"2021-03-26T02:54:44.000Z"},"remix":{"parent":88886,"root":88886},"statistics":{"ranks":{"views":34903,"loves":43421,"favorites":42362},"views":10605,"loves":274,"favorites":225,"comments":803},"metadata":{"version":2,"costumes":0,"blocks":0,"variables":0,"assets":7,"hash":"d452b0e9c182f18209f7b4348b1cd2a3","user_agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0","history":{"2016-07-05T15:11:39.000Z":"d452b0e9c182f18209f7b4348b1cd2a3"}}}
```
### How to make this more easy to read:
First of all this is json so any experienced coder has got it from here. For the less exprerienced coders though, this is hard to read. So, copy that code and go to this link: https://codebeautify.org/jsonviewer Then, paste your code on the left side and you should get something like this:
```
object		{12}
id	:	100000
sys_id	:	3933088
username	:	pinkhollyspark
title	:	happy_birthday_funkadelihippo!!!!!!!!!!!!!!
description	:	Happy birthday funkadelihippo!!!!!!!!
instructions	:	
public	:	true
comments_allowed	:	true
	times		{5}
created	:	2008-02-15T10:49:33.000Z
modified	:	2016-07-05T15:11:39.000Z
shared	:	2008-02-15T10:49:33.000Z
last_check	:	2022-04-23T13:58:42.000Z
last_metadata_check	:	2021-03-26T02:54:44.000Z
	remix		{2}
parent	:	88886
root	:	88886
	statistics		{5}
	ranks		{3}
views	:	34903
loves	:	43421
favorites	:	42362
views	:	10605
loves	:	274
favorites	:	225
comments	:	803
	metadata		{8}
version	:	2
costumes	:	0
blocks	:	0
variables	:	0
assets	:	7
hash	:	d452b0e9c182f18209f7b4348b1cd2a3
user_agent	:	Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
	history		{1}
2016-07-05T15:11:39.000Z	:	d452b0e9c182f18209f7b4348b1cd2a3
```
### Let's say I want the amount of favorites. How do I get that?
Well, you get it by doing this:
```
sample = getprojectinfo
print(sample['statistics']['favorites'])
```
which should return this in the console:
```
225
```
### And that is how to use ScratchStats!
