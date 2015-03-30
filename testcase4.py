# Benjamin Chu
# Python Script - Test Case #4

# Using the World of Warcraft Item Set Web API,
# retrieve data for a non-existent item and
# confirm the API fails gracefully.

import requests
import json

item_id = 1 # non-existant item id / item

# API Urls for individual regions
api_us_url = "http://us.battle.net/api/wow/item/" + str(item_id)
api_tw_url = "http://tw.battle.net/api/wow/item/" + str(item_id)
api_kr_url = "http://kr.battle.net/api/wow/item/" + str(item_id)
api_eu_url = "http://eu.battle.net/api/wow/item/" + str(item_id)
api_cn_url = "http://www.battlenet.com.cn/api/wow/item/" + str(item_id)

# authRequest = requests.get(api_us_url, auth = ('user', 'pass'))
request404 = requests.get(api_us_url)
request_dict = request404.json()
passNum = 0;

# Compare response
if (str(request404) == "<Response [404]>"):
	passNum = passNum + 1
else:
	print "Incorrect code"

# Compare status
if (str(request_dict["status"]) == "nok"):
	passNum = passNum + 1
else:
	print "Incorrect status"

# Compare reason
if (str(request_dict["reason"]) == "unable to get item information."):
	passNum = passNum + 1
else:
	print "Incorrect reason"

if (passNum == 3):
	print "\nTest Case PASSED"
else:
	print "\nTest Case FAILED"

# Example Output
# Test Case PASSED