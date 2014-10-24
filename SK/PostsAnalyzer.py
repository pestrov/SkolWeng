import json
users = [1823975091, 1650111241, 1859586112, 1784473157, 1850988623, 2286908003, 1191965271, 1986926181, 3288976495, 2230312052, 1751714412, 2217035934, 1814040741, 1796445350,1904769205, 1771925961, 2000961721, 2100623570, 2089800791, 1644489953, 1225314032, 5120783603, 1823887605, 1729332983, 2098122492, 2243807243, 1853472775, 1626443785, 2165090317, 3235040884, 1642482194,1682207150, 2847927727,3034112034, 1651428902, 2011075080, 1649159940, 1873625985, 3763936545, 2737798435, 3830136640, 1663414103, 1663937380, 1256947091, 1642634100, 3446047612, 5016338752, 3237705130, 1642632622, 2418433987, 2410528240]
uniques_file=open('uniques.json')
uniques = json.load(uniques_file)
greatUsers = []
for key, value in uniques.iteritems():
    if value["userId"] in users:
        greatUsers.append({"userId":value["userId"],
                           "retweets":value["retweets"],
                           "likes":value["likes"]})

with open('userPostsInfos.json','w') as outfile:
    json.dump(greatUsers,outfile)

json_data=open('userPostsInfos.json')
data = json.load(json_data)

postsByUserId = {}

for post in data:
    if str(post["userId"]) in postsByUserId:
        postsByUserId[str(post["userId"])].append({"retweets":post["retweets"], "likes":post["likes"]})
    else:
        postsByUserId[str(post["userId"])] = [{"retweets":post["retweets"], "likes":post["likes"]}]

print postsByUserId
print len(postsByUserId)


for key, value in postsByUserId.iteritems():
       print len(value)
#for key, value in data.iteritems():
#        greatUsers.append({"userId":value["userId"],
#                           "retweets":value["retweets"],
#                           "likes":value["likes"]})