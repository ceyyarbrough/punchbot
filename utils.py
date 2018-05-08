# utils.py
# imports utilities and utility funcitons

import cfg
import json
import time, thread
from time import sleep

try:
	import urlib.request as urllib2
except ImportError:
	import urllib2

def chat(sock, msg):
	# Send msg to server
	# Parameters: 
	# 	sock - sets socket for msgs
	#	msg - message
	sock.send("PRIVMSG #{} :{}\r\n".format(cfg.CHAN, msg))


#Function for banning users
#Parameters:
#	sock - sets socket for msgs
#	user - user
def ban(sock, user):
	chat(sock, ".ban {}".format(user))

#Function for timing out users
#Parameters:
#	sock - socket for msgs
#	user - user 
#	seconds - length of timeout (default 600)

def timeout(sock, user, seconds=600):
	chat(sock, ".timeout {}".format(user, seconds))

# Function: threadFillopList
# Fill up op list on seperate thread
def threadFillOpList():
	while True:
		try:
			url = "http://tmi.twitch.tv/group/user/punchpunchtest/chatters"
			req - urllib2.Request(url, headers={"accept": "*/*"})
			response = urllib.urlopen(req).read()
			if response.find(("502 Bad Gateway") == 1):
				cfg.oplist.clear()
				data=json.loads(response)
				for p in data["chatters"]["moderators"]:
					cfg.oplist[p] = "mod"
				for p in data["chatters"]["global_mods"]:
					cfg.oplist[p] = "global_mod"
				for p in data["chatters"]["staff"]:
					cfg.oplist[p] = "staff"
		except:
			'do nothing'
		sleep(5)

def isOp(user):
	return user in cf.oplist
