# Benjamin Chu
# Python Script - Test Case #5

# Using the World of Warcraft Item Set Web API,
# retrieve data for a non-existent item and
# confirm the API fails gracefully.

import requests
import json

item_id = 123456789012345678901234567890 # item id out of unsigned integer bounds

# API Urls for individual regions
api_us_url = "http://us.battle.net/api/wow/item/" + str(item_id)
api_tw_url = "http://tw.battle.net/api/wow/item/" + str(item_id)
api_kr_url = "http://kr.battle.net/api/wow/item/" + str(item_id)
api_eu_url = "http://eu.battle.net/api/wow/item/" + str(item_id)
api_cn_url = "http://www.battlenet.com.cn/api/wow/item/" + str(item_id)

request500 = requests.get(api_us_url)
request_dict = request500.json()
passNum = 0;

# Compare response
if (str(request500) == "<Response [500]>"):
	passNum = passNum + 1
else:
	print "Incorrect code"

# Compare status
if (str(request_dict["status"]) == "nok"):
	passNum = passNum + 1
else:
	print "Incorrect status"

# Compare reason
if (str(request_dict["reason"]) == "Item id should be integer."):
	passNum = passNum + 1
else:
	print "Incorrect reason"

print "\n"
print str(request500)
print str(request_dict["status"])
print str(request_dict["reason"])

if (passNum == 3):
	print "\nTest Case PASSED"
else:
	print "\nTest Case FAILED"

# Example Output
# Test Case PASSED