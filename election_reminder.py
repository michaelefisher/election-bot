#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import requests

import dateutil.parser
import dateutil.utils
import dateutil.tz

token = os.getenv("SLACK_TOKEN")

contests = [ ]

with open('data.json') as f:
	contests = json.load(f)

text = None
for contest in contests:
	dflt_tz = dateutil.tz.tzoffset("EST", -18000)
	today = dateutil.utils.today(dflt_tz)
	d = dateutil.parser.parse(contest['date']) - today
	if d.days < 0:
		continue # go to next contest
	try:
		fact = contest['facts'][d.days]
	except:
		fact = ''
	if d.days >= 2:
		text = "It is %s. %s %s in %s days. %s" % (today.strftime("%A"), contest['event'], contest['verb'], d.days, fact)
	else:
		when = ["today", "tomorrow"][d.days]
		text = "It is %s. The %s %s %s. %s" % (today.strftime("%A"), contest['event'], contest['verb'], when, fact)

	break

payload = {"username": "ElectionReminder", "text": text, "icon_emoji": ":ghost:"}

print "Sending Payload:"
print json.dumps(payload, sort_keys=True)

if text is not None and token is not None:
	requests.post(token, json = payload)
