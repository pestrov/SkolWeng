import json
json_data=open('uniques.json')

data = json.load(json_data)
print data.keys()

numberOfGreatPosts = 0
print len(data)
for key, value in data.iteritems():
    if len(value["tag"]) > 1 and value["likes"] >= 5:
        print value["tag"]
        numberOfGreatPosts = numberOfGreatPosts + 1

print numberOfGreatPosts