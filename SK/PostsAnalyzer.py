import json
json_data=open('uniques.json')

data = json.load(json_data)


greatUsers = []

for key, value in data.iteritems():
    if len(value["tag"]) > 1 and value["likes"] >= 5:

        greatUsers.append(value["userId"])


unique = set(greatUsers)
print unique
print len(unique)
print len(greatUsers)
