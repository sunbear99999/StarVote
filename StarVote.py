# coding=utf-8
import requests
import json
import time
import sys
from random import randint

__author__	 	= 'QD'
__copyright__   = 'Copyright (C) 2015 QD'
__version__ 	= '0.2'
__email__ 		= 'inside.QD@googlemail.com'
__github__		= 'http://github.com/DestructiveInfluence/StarVote'
__python__		= '2.7'

headers = {'user-agent':'StarVote 0.2 by QD'}
sleepTimer = 3

def redditLogin(username,password):
	password = password.replace('\n','')
	print('[/] Logging in as ' + username)
	login_dict = {'user':username,'passwd':password,'api_type':'json'}
	client = requests.session()
	client.headers = headers
	r = client.post(r'http://www.reddit.com/api/login',data=login_dict)
	j = r.json()
	return j

def redditUpvote(client,uniqueID):
	url = 'http://www.reddit.com/api/vote'
	data = {'uh': client.modhash,'dir':1,'id':uniqueID}
	client.headers = {'user-agent':'StarVote 0.2 by QD','X-Modhash':client.modhash}
	r = client.post(url,data=data,cookies={'reddit_session':client.cookie})
	return r

def redditRegister(usernameBase,passwordBase,registerAmount):
	url = 'http://www.reddit.com/api/register/'
	client = requests.session()
	client.headers = headers
	f = open('accounts.txt','a')
	for x in range(1,registerAmount):
		username = usernameBase + str(randint(0,9999999999999999999))
		username = username[:20]
		data = {'op':'reg','user':username,'passwd':passwordBase,'passwd2':passwordBase,'api_type':'json'}
		r = client.post(url + username,data=data)
		j = r.json()
		if j['json']['errors'] == []:
			f.write(username + ':' + passwordBase + '\n')
			print('[/] Successfully registered ' + username + ' [' + str(x) + '/' + str(registerAmount) + ']')
			print('[/] Now waiting 10 minutes...')
		time.sleep(610)
	f.close()	

def redditInfo(uniqueID):
	url = 'http://www.reddit.com/api/info.json?id=' + uniqueID
	client = requests.session()
	client.headers = headers
	r = client.get(url)
	j = r.json()
	return j

def redditUpvoteHandler(tX):
	print('[/] Specify ID of the item you want to upvote.')
	uniqueID = raw_input('[/] ID Input: ')
	uniqueID = tX + uniqueID
	jsonInfo = redditInfo(uniqueID)
	if jsonInfo['data']['children'] != []:
		print('[/] Title: ' + jsonInfo['data']['children'][0]['data']['title'])
		lines = accountReader()
		for element in lines:
			username,password = element.split(':',1)
			j = redditLogin(username,password)
			time.sleep(sleepTimer)
			if j['json']['errors'] == []:
				client.modhash = j['json']['data']['modhash']
				client.cookie = j['json']['data']['cookie']
				r = redditUpvote(client,uniqueID)
				if r.status_code == 200:
					print('[/] Successfully upvoted as ' + username)
			else:
				print(j['json']['errors'])
			time.sleep(sleepTimer)
		print('[/] Upvoting finished.')
		print('[/] Achieve more upvotes, by')
		print('[/] - using reputable reddit accounts')
		print('[/] - setting a higher sleep timer')
		print('[/] - using proxies')

def redditRegisterHandler():
	print('[/] Registering accounts is very slow. [1 Account / 10 Minutes]')
	usernameBase = raw_input('[/] Enter usernameBase (max. 10 char): ')
	if len(usernameBase) <= 10:
		passwordBase = raw_input('[/] Enter password: ')
		registerAmount = raw_input('[/] Enter registerAmount: ')
		redditRegister(usernameBase,passwordBase,int(registerAmount))
	else:
		print('[/] usernameBase too long.')

def accountReader():
	with open('accounts.txt') as f:
		lines = f.readlines()
		f.close()
	return lines

def setSleepTimer():
	print('[/] Sleep timer in seconds. Default is 3')
	global sleepTimer
	sleepTimer = float(raw_input('[/] Set new sleep timer: '))
	print("[/] Sleep timer set to " + str(sleepTimer))
	main()

def switch(x):
    if x == '1':
    	redditUpvoteHandler('t3_')
    elif x == '2':
    	redditUpvoteHandler('t1_')
    elif x == '3':
    	redditRegisterHandler()
    elif x == '4':
    	setSleepTimer()
    elif x == '5':
    	creditZ()

def welcome():
	securit_ascii =['    ______          _   __     __   \n',
					'   / __/ /____ ____| | / /__  / /____  \n',
					'  _\ \/ __/ _ `/ __/ |/ / _ \/ __/ -_) \n',
					' /___/\__/\_,_/_/  |___/\___/\__/\__/ \n']
	print('')
	print('')
	print('')
	for line in securit_ascii:
		for c in line:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.005)
	print('')
	print('')
	print('01010001 01000100')
	print('[/] Reddit Upvote Script by QD (c) 2015')
	print('[/] Feature Requests: inside.QD@gmail.com')
	print('-------------------------------------------------')
	print('')

def menu():
	print('     StarVote v0.2')
	print(u'\u2554' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2557')
	print(u'\u2551' + ' [1] Upvote Link       ' + u'\u2551')
	print(u'\u2551' + ' [2] Upvote Comment    ' + u'\u2551')
	print(u'\u2551' + ' [3] Register Accounts ' + u'\u2551')
	print(u'\u2551' + ' [4] Set Sleep Timer   ' + u'\u2551')
	print(u'\u2551' + ' [5] Credits           ' + u'\u2551')
	print(u'\u255A' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u255D')
	print('')

def main():
	welcome()
	menu()
	switchChoice = raw_input('[/] Please chose: ')
	print('')
	switch(switchChoice)

main()
print('[/] StarVote v0.2 finished its job. QD <3')
time.sleep(10)