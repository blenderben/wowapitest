# Benjamin Chu
# Python Script - Test Case #6

# Using the World of Warcraft Item Set Web API,
# retrieve the item ids for all items in the
# "Deep Earth Vestments" set and verify that
# the item id for each item matches that which
# is returned by the Item Web API.

import requests
import json

setitem_id = 1060 # item id out of unsigned integer bounds

# API Urls for individual regions
api_us_url = "http://us.battle.net/api/wow/item/set/" + str(setitem_id)
api_tw_url = "http://tw.battle.net/api/wow/item/set/" + str(setitem_id)
api_kr_url = "http://kr.battle.net/api/wow/item/set/" + str(setitem_id)
api_eu_url = "http://eu.battle.net/api/wow/item/set/" + str(setitem_id)
api_cn_url = "http://www.battlenet.com.cn/api/wow/item/set/" + str(setitem_id)

# GET request
itemset = requests.get(api_us_url)
itemset_dict = itemset.json()
passNum = 0

# Output Deep Earth Vestments item IDs
print "\nThese are the item IDs for all items in the Deep Earth Vestments:"
print str(itemset_dict["items"])

# Loop through Deep Earth Vestments, grab each item id and compare with Item Web API
for x in range(0, len(itemset_dict["items"])):
	item_api_us_url = "http://us.battle.net/api/wow/item/" + str(itemset_dict["items"][x])
	item = requests.get(item_api_us_url)
	item_dict = item.json()
	if ( str(item_dict["id"]) == str(itemset_dict["items"][x]) ):
		print str(item_dict["id"]) + " - Item Web API & Item Set Web API match!"
		passNum = passNum + 1
	else:
		print str(itemset_dict["items"][x]) + " is not a match."

if ( passNum == len(itemset_dict["items"]) ):
	print "Test Case PASSED"
else:
	print "Test Case FAILED"

# Example Output
# These are the item IDs for all items in the Deep Earth Vestments:
# [76749, 76750, 76751, 76752, 76753]
# 76749 - Item Web API & Item Set Web API match!
# 76750 - Item Web API & Item Set Web API match!
# 76751 - Item Web API & Item Set Web API match!
# 76752 - Item Web API & Item Set Web API match!
# 76753 - Item Web API & Item Set Web API match!
# Test Case PASSED