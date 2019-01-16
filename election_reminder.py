# -*- coding: utf-8 -*-

import datetime
import os
import requests

contests = [
	{
    "contest":"Iowa Caucuses",
	"date": datetime.date(2020,02,03),
	"verb": "are",
	"facts": []
	},
]
text = None
for contest in contests:
	d = contest['date'] - datetime.date.today()
	if d.days < 0:
		continue #go to next contest
	try:
		fact = contest['facts'][d.days]
	except:
		fact = ''
	if d.days >= 2:
		text = "It is %s. %s %s in %s days. %s" % (datetime.date.today().strftime("%A"), contest['contest'], contest['verb'], d.days, fact)
	else:
		when = ["today", "tomorrow"][d.days]

		text = "It is %s. The %s %s %s. %s" % (datetime.date.today().strftime("%A"), contest['contest'], contest['verb'], when, fact)

	payload = {"username": "ElectionReminder", "text": "I was asked to move to this channel by someone who hates fun", "icon_emoji": ":ghost:"}
	break
if text is not None:
    requests.post(os.get_env(SLACK_TOKEN), json = payload)
