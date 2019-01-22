# -*- coding: utf-8 -*-

import os
import datetime
import requests

contests = [
	{
    "contest":"Iowa Caucuses",
	"date": datetime.date(2020,02,03),
	"verb": "are",
	"facts": []
	},
]

# Just add in the 3 components of the Slack webhook URL: team, channel, secret token
SLACK_WEBHOOK_TOKEN = os.getenv("SLACK_WEBHOOK_TOKEN", None)
SLACK_URL = "https://hooks.slack.com/services/%s" % SLACK_WEBHOOK_TOKEN

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
	payload = {"username": "ElectionReminder", "text": text, "icon_emoji": ":ghost:"}
	break
if text is not None and SLACK_WEBHOOK_TOKEN is not None:
    requests.post(SLACK_URL, json = payload)
