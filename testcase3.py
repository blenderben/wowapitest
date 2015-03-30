# Benjamin Chu
# Python Script - Test Case #3

# Using the World of Warcraft Item Set Web API,
# retrieve data for 'Finkle's Lava Dredger' 10,000+
# times to confirm throttling.

import requests
import json

item_id = 18803 # Finkle's Lava Dredger Item ID

# API Urls for individual regions
api_us_url = "http://us.battle.net/api/wow/item/" + str(item_id)
api_tw_url = "http://tw.battle.net/api/wow/item/" + str(item_id)
api_kr_url = "http://kr.battle.net/api/wow/item/" + str(item_id)
api_eu_url = "http://eu.battle.net/api/wow/item/" + str(item_id)
api_cn_url = "http://www.battlenet.com.cn/api/wow/item/" + str(item_id)

# Put the total number of unauthorized requests that can be made per day
# 10,000 unauthorized requests allowed per day via Service Availability Notice
# http://blizzard.github.io/api-wow-docs/#policies-and-support/api-policy
maxRequests = 10000;
count = 0;

print "\nCalling API " + str(maxRequests) + " times"

# Makes maxRequests + 10 of requests to the API and outputs the elapsed time for each request
for x in range(0, maxRequests + 1):
	print "\nConnection #" + str(x + 1)
	timer = requests.get(api_us_url).elapsed.total_seconds()
	count = count + 1
	print "Elapsed: " + str(timer)

print "\n" + str(count) + " requests made."
print "Max allowed is: " + str(maxRequests)

if ( count > maxRequests ):
	print "Test Case FAILED"
else:
	print "Test Case PASSED"

# Example Output
# Calling API 5 times

# Connection #1
# Elapsed: 0.093609

# Connection #2
# Elapsed: 0.075952

# Connection #3
# Elapsed: 0.095353

# Connection #4
# Elapsed: 0.082381

# Connection #5
# Elapsed: 0.080393

# Connection #6
# Elapsed: 0.090236

# 6 requests made.
# Max allowed is: 5
# Test Case FAILED
