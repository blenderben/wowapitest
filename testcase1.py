# Benjamin Chu
# Python Script - Test Case #1

# Using the World of Warcraft Item Set Web API
# retrieve data for 'Finkle's Lava Dredger' on the
# US region and confirm that the returned item id,
# disenchantingSkillRank and icon, return the same
# value on the TW and KR regions.

import requests
import json

item_id = 18803 # Finkle's Lava Dredger Item ID

print "\nTesting item ID: " + str(item_id) + "\n"

# API Urls for individual regions
api_us_url = "http://us.battle.net/api/wow/item/" + str(item_id)
api_tw_url = "http://tw.battle.net/api/wow/item/" + str(item_id)
api_kr_url = "http://kr.battle.net/api/wow/item/" + str(item_id)
api_eu_url = "http://eu.battle.net/api/wow/item/" + str(item_id)
api_cn_url = "http://www.battlenet.com.cn/api/wow/item/" + str(item_id)

# GET requests
us = requests.get(api_us_url)
tw = requests.get(api_tw_url)
kr = requests.get(api_kr_url)

# Converting to Python dictionary
us_dict = us.json()
tw_dict = tw.json()
kr_dict = kr.json()

# Output
print "US Item ID: " + str(us_dict["id"])
print "TW Item ID: " + str(tw_dict["id"])
print "KR Item ID: " + str(kr_dict["id"])

print "US Icon Value: " + str(us_dict["icon"])
print "TW Icon Value: " + str(tw_dict["icon"])
print "KR Icon Value: " + str(kr_dict["icon"])

print "US Disenchant Skill Rank: " + str(us_dict["disenchantingSkillRank"])
print "TW Disenchant Skill Rank: " + str(tw_dict["disenchantingSkillRank"])
print "KR Disenchant Skill Rank: " + str(kr_dict["disenchantingSkillRank"])

# Conditionals to check if Item ID's match across regions
if ( us_dict["id"] == tw_dict["id"] and us_dict["id"] == kr_dict["id"] and tw_dict["id"] == kr_dict["id"] ):
	item_id_testmsg = "Pass: Item ID's match across regions (US/TW/KR)."
	item_id_pass = 1;
else:
	item_id_testmsg = "Fail: Item ID's do not match across regions (US/TW/KR)."

if ( us_dict["icon"] == tw_dict["icon"] and us_dict["icon"] == kr_dict["icon"] and tw_dict["icon"] == kr_dict["icon"] ):
	item_icon_testmsg = "Pass: Item icon matches across regions (US/TW/KR)."
	item_icon_pass = 1;
else:
	item_icon_testmsg = "Fail: Item icon does not match across regions (US/TW/KR)."

if ( us_dict["disenchantingSkillRank"] == tw_dict["disenchantingSkillRank"] and us_dict["disenchantingSkillRank"] == kr_dict["disenchantingSkillRank"] and tw_dict["disenchantingSkillRank"] == kr_dict["disenchantingSkillRank"] ):
	item_disenchant_testmsg = "Pass: Item Disenchating Skill Rank matches across regions (US/TW/KR)."
	item_disenchant_pass = 1;
else:
	item_disenchant_testmsg = "Fail: Item Disenchating Skill Rank does not match across regions (US/TW/KR)."

# If id, icon and disenchantingSkillRank all pass with same values across regions, then pass test case, else fail and print messages
if ( item_id_pass and item_icon_pass and item_disenchant_pass == 1):
	print "\nTest Case PASSED!"
else:
	print item_id_testmsg
	print item_icon_testmsg
	print item_disenchant_testmsg

# Example Output
# Testing item ID: 18803

# US Item ID: 18803
# TW Item ID: 18803
# KR Item ID: 18803
# US Icon Value: inv_gizmo_02
# TW Icon Value: inv_gizmo_02
# KR Icon Value: inv_gizmo_02
# US Disenchant Skill Rank: 225
# TW Disenchant Skill Rank: 225
# KR Disenchant Skill Rank: 225

# Test Case PASSED!
