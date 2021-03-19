from requests import post
from sys import argv
from time import sleep, time
from random import choice
from os import _exit

def closeBot(message="", show_run_log=0):
	if show_run_log:
		run_log["end_time"] = time()
		run_log["time"] = run_log["end_time"] - run_log["start_time"]

		print("\n\n==================================\n\n")
		print(f"start_time - {run_log['start_time']} sec")
		print(f"end_time - {run_log['end_time']} sec")
		print(f"time - {run_log['time']} sec\n")
		print(f"sended_messages - {run_log['sended_messages']}\n")
		print(f"channel - {run_log['channel']}")
		print(f"delay - {run_log['delay']} sec")
		print(f"log_messages - {run_log['log_messages']}")

	if(message != ""):
		print("\n\n==================================")
		print("\n\n" + message)
	print("\n\n==================================")
	print("============= Goodbye ============")
	print("==================================\n")
	_exit(0)

global run_log

try:
	run_log = {
		"sended_messages": 0,
		"start_time": time()
	}

	print(chr(27) + "[2J")

	print("=================================")
	print("===== discord-auto-messages =====")
	print("=================================\n\n\n")

	# Get the discord Token
	token_file = open("token.txt", "r")
	disc_token = token_file.readline()

	if disc_token[-1] == "\n":
		disc_token = disc_token[:-1]

	token_file.close()

	header = {
		"authorization": disc_token
	}

	# Get the Discord Channel
	try:
		run_log["channel"] = int(argv[1])

	except:
		closeBot("Invalid Channel")

	# Delay betwen messages
	try:
		run_log["delay"] = int(argv[2])

	except :
		run_log["delay"] = 1

	print("Delay - " + str(run_log["delay"]) + " sec")

	# Log each message
	try:
		run_log["log_messages"] = int(argv[3])

	except:
		run_log["log_messages"] = 1

	print("log_messages - " + str(run_log["log_messages"]))

	print("\n\n==================================")
	print("\n\nStarting the requests\n\n")

	while True:
		# Messages to be send to Discord
		messages = [
			"Discord"
		]

		message = choice(messages)

		payload = {
			"content": message
		}

		if run_log["log_messages"]:
			print(f"Sending - '{message}'")
		
		r = post(
			f"https://discord.com/api/v8/channels/{run_log['channel']}/messages",
			data=payload,
			headers=header
		)

		run_log['sended_messages'] += 1

		sleep(run_log["delay"])

except KeyboardInterrupt:
	closeBot(show_run_log=1)

except:
	closeBot("Unexpected error")
