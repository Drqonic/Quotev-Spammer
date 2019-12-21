import sys
import time
import random
import requests

username = "USERNAME"
password = "PASSWORD"

uk = input("UK: ")
_id = input("ID: ")
amount = int(input("Amount of messages (at least 3): "))

if amount < 3:
	sys.exit("Sorry but the minimum amount of messages is 3.")

messages = []

for i in range(1, amount+1):
	messages.append(input("Message #{}: ".format(i)))

user_agents = [
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
	"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
	"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
	"Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
]

with requests.Session() as session:
	session.post(
		"https://www.quotev.com/user/login",
		data={
			"username": username,
			"password": password,
			"save": "on"
		}
	)

	while True:
		for message in messages:
			session.post(
				"https://www.quotev.com/ajax/comment-data",
				headers={
					"Content-Type": "application/x-www-form-urlencoded",
					"Origin": "https://www.quotev.com",
					"Referer": "https://www.quotev.com",
					"User-Agent": random.choice(user_agents),
					"X-Ajax": "1"
				},
				data={
					"uk": uk,
					"t": "3",
					"d": "-1",
					"id": _id,
					"act": "add",
					"data": message
				}
			)

			time.sleep(1)
