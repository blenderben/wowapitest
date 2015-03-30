# Benjamin Chu
# Python Script - Test Case #2

# Using the World of Warcraft Item Set Web API,
# retrieve data for 'Finkle's Lava Dredger' and
# confirm that request and response time with the API is acceptable.

import requests
import json

item_id = 18803 # Finkle's Lava Dredger Item ID

# API Urls for individual regions
api_us_url = "http://us.battle.net/api/wow/item/" + str(item_id)
api_tw_url = "http://tw.battle.net/api/wow/item/" + str(item_id)
api_kr_url = "http://kr.battle.net/api/wow/item/" + str(item_id)
api_eu_url = "http://eu.battle.net/api/wow/item/" + str(item_id)
api_cn_url = "http://www.battlenet.com.cn/api/wow/item/" + str(item_id)

timeArray = []

# Grabbing total elapsed seconds for request time 10 times in a row for US host
print "\nTesting Request/Response Time...\n"
print "Host: US"
for x in range(0, 10):
	timer = requests.get(api_us_url).elapsed.total_seconds()
	timeArray.append(timer)
	print "Elapsed: " + str(timer)

# Output Min, Max, and Average times
print "Shortest time: " + str(min(timeArray)) + " seconds."
print "Longest time: " + str(max(timeArray)) + " seconds."
print "Average time: " + str(sum(timeArray)/len(timeArray)) + " seconds."
del timeArray[:]

# Grabbing total elapsed seconds for request time 10 times in a row for KR host
print "\nTesting Request/Response Time...\n"
print "Host: KR"
for x in range(0, 10):
	timer = requests.get(api_kr_url).elapsed.total_seconds()
	timeArray.append(timer)
	print "Elapsed: " + str(timer)

# Output Min, Max, and Average times
print "Shortest time: " + str(min(timeArray)) + " seconds."
print "Longest time: " + str(max(timeArray)) + " seconds."
print "Average time: " + str(sum(timeArray)/len(timeArray)) + " seconds."
del timeArray[:]

# Grabbing total elapsed seconds for request time 10 times in a row for TW host
print "\nTesting Request/Response Time...\n"
print "Host: TW"
for x in range(0, 10):
	timer = requests.get(api_tw_url).elapsed.total_seconds()
	timeArray.append(timer)
	print "Elapsed: " + str(timer)

# Output Min, Max, and Average times
print "Shortest time: " + str(min(timeArray)) + " seconds."
print "Longest time: " + str(max(timeArray)) + " seconds."
print "Average time: " + str(sum(timeArray)/len(timeArray)) + " seconds."

# Example Output
# Testing Request/Response Time...

# Host: US
# Elapsed: 0.13882
# Elapsed: 0.139732
# Elapsed: 0.140561
# Elapsed: 0.204194
# Elapsed: 0.1431
# Elapsed: 0.146859
# Elapsed: 0.175106
# Elapsed: 0.138512
# Elapsed: 0.133154
# Elapsed: 0.136201
# Shortest time: 0.133154 seconds.
# Longest time: 0.204194 seconds.
# Average time: 0.1496239 seconds.

# Testing Request/Response Time...

# Host: KR
# Elapsed: 0.297568
# Elapsed: 0.377586
# Elapsed: 0.407056
# Elapsed: 0.304568
# Elapsed: 0.305795
# Elapsed: 0.295946
# Elapsed: 0.35319
# Elapsed: 0.352201
# Elapsed: 0.374894
# Elapsed: 0.308483
# Shortest time: 0.295946 seconds.
# Longest time: 0.407056 seconds.
# Average time: 0.3377287 seconds.

# Testing Request/Response Time...

# Host: TW
# Elapsed: 0.361108
# Elapsed: 0.352334
# Elapsed: 0.376749
# Elapsed: 0.358737
# Elapsed: 0.309634
# Elapsed: 0.301213
# Elapsed: 0.311688
# Elapsed: 0.372092
# Elapsed: 0.284276
# Elapsed: 0.322574
# Shortest time: 0.284276 seconds.
# Longest time: 0.376749 seconds.
# Average time: 0.3350405 seconds.