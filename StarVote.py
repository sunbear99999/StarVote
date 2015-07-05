# coding=utf-8
import requests
import json
from pprint import pprint
from random import randint
import time
import sys
from colorama import init, Fore, Style

__author__	 	= 'QD'
__copyright__   = 'Copyright (C) 2015 QD'
__version__ 	= '0.2'

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
print('[Console] Reddit Upvote Script by QD (c) 2015')
print('[Console] Feature Requests: inside.QD@gmail.com')
print('-------------------------------------------------')

instanceID = str(randint(0,50000))
sleepTimer = 3

def creditZ():
	print('')
	print('')
	print('')
	
	print(Fore.GREEN + Style.BRIGHT)
	for line in securit_ascii:
		print('                    '),
		for c in line:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.005)
	print('')
	print('')

	print(    '                            ' + u'\u2554' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			 + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			 + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			 + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			 + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2557')
	print(    '                            ' + u'\u2551' + '                       ' + u'\u2551')
	print(    '                            ' + u'\u2551' + '  Reddit Upvote Script ' + u'\u2551')
	print(    '                            ' + u'\u2551' + '     by QD (c) 2015    ' + u'\u2551')
	print(    '                            ' + u'\u2551' + '  inside.QD@gmail.com  ' + u'\u2551')
	print(    '                            ' + u'\u2551' + '  All rights reserved  ' + u'\u2551')
	print(    '                            ' + u'\u2551' + '                       ' + u'\u2551')
	print(    '                            ' + u'\u255A' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550'
			+ u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u255D')
	print('')
	print('')
	print('')
	print('')
	print(Fore.RESET + Style.RESET_ALL)
	raw_input("")
	print('')
	print('')
	print('')
	print('')
	print('')
	print('')
	print('')
	print('')
	print('')
	print('')
	main()

def setSleepTimer():
	print('[Console] Sleep timer in seconds. Default is 3')
	global sleepTimer
	sleepTimer = float(raw_input('[Console] Set new sleep timer: '))
	print("[Console] Sleep timer set to " + str(sleepTimer))
	main()

def redditLogin(username,password):
	password = password.replace('\n','')
	print('[Console] Logging in as ' + username)
	login_dict = {'user':username,'passwd':password,'api_type':'json'}
	headers = {'user-agent':'StarVote 0.2 by QD - Instance ' +  instanceID}
	client = requests.session()
	client.headers = headers
	r = client.post(r'http://www.reddit.com/api/login',data=login_dict)
	j = r.json()
	#pprint(j)
	if j['json']['errors'] == []:
		client.modhash = j['json']['data']['modhash']
		client.cookie = j['json']['data']['cookie']
		return client
	else:
		pprint(j['json']['errors'])
		return 'Error'

def redditUpvote(client,uniqueID):
	url = 'http://www.reddit.com/api/vote'
	data = {'uh': client.modhash,'dir':1,'id':uniqueID}
	headers = {'user-agent':'StarVote 0.2 by QD - Instance ' + instanceID,'X-Modhash':client.modhash}
	client.headers = headers
	r = client.post(url,data=data,cookies={'reddit_session':client.cookie})
	#j = r.json()
	#pprint(j)
	return r

def redditInfo(uniqueID):
	url = 'https://www.reddit.com/api/info.json?id=' + uniqueID
	headers = {'user-agent':'StarVote 0.2 by QD - Instance ' + instanceID}
	client = requests.session()
	client.headers = headers
	r = client.get(url)
	j = r.json()
	return j
	#pprint(j)

def accountReader():
	with open('accounts.txt') as f:
		lines = f.readlines()
		f.close()
	return lines

def redditUpvoteHandler(tX):
	print('[Console] Specify ID of the item you want to upvote.')
	uniqueID = raw_input('[Console] ID Input: ')
	uniqueID = tX + uniqueID
	jsonInfo = redditInfo(uniqueID)
	if jsonInfo['data']['children'] != []:
		infoScoreBefore = jsonInfo['data']['children'][0]['data']['score']
		infoTitle = jsonInfo['data']['children'][0]['data']['title']
		print('[Console] Title: ' + infoTitle  + u'\u00A6' + ' Score: ' + str(infoScoreBefore))
		lines = accountReader()
		for element in lines:
			username,password = element.split(':',1)
			client = redditLogin(username,password)
			time.sleep(sleepTimer)
			if client != 'Error':
				r = redditUpvote(client,uniqueID)
				if r.status_code == 200:
					print('[Console] Successfully upvoted as ' + username)
				if r.status_code == 404:
					print('[Console] Unique ID doesn''t exist, scrub.')
					break
			print('')
			time.sleep(sleepTimer)
		jsonInfo = redditInfo(uniqueID)
		infoScoreAfter = jsonInfo['data']['children'][0]['data']['score']
		infoScore = (infoScoreAfter - infoScoreBefore)+1
		print('[Console] Upvoting finished. Overall permitted upvotes: ' + Fore.GREEN + Style.BRIGHT + str(infoScore) + ' [+/- 3]' + Fore.RESET + Style.RESET_ALL)
		print('[Console] Achieve more upvotes, by setting a higher sleep timer.')

	else:
		print('[Console] Unique ID doesn''t exist, scrub.')

def redditRegister(usernameBase,passwordBase,registerAmount):
	url = 'https://www.reddit.com/api/register/'
	headers = {'user-agent':'StarVote 0.2 by QD - Instance ' +  instanceID}
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
			print('')
			print('[Console] Successfully registered ' + username + ' [' + str(x) + '/' + str(registerAmount) + ']')
			print('[Console] Now waiting 10 minutes...')
		time.sleep(620)
	f.close()

def redditRegisterHandler():
	print('[Console] Registering accounts is very slow. [1 Account / 10 Minutes]')
	usernameBase = raw_input('[Console] Enter usernameBase (max. 10 char): ')
	if len(usernameBase) <= 10:
		passwordBase = raw_input('[Console] Enter password: ')
		registerAmount = raw_input('[Console] Enter registerAmount: ')
		redditRegister(usernameBase,passwordBase,int(registerAmount))
	else:
		print('[Console] usernameBase too long.')

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

def main():
	init()
	print('')
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
	switchChoice = raw_input('[Console] Please chose: ')
	print('-------------------------------------------------')
	print('')
	switch(switchChoice)

main()
print('[Console] StarVote v0.2 finished its job. QD <3')
time.sleep(10)