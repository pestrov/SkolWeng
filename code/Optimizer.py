"import os, json
import math

def addNodesFromFile(filename, influencerUid, graph):
    json_data=open('xFiles/' + filename)
    data = json.load(json_data)
    for user in data:
        if str(user["userId"]) in graph:
            graph[str(user["userId"])].append(influencerUid)
        else:
            graph[str(user["userId"])] = [influencerUid]


graph = {}
for fileName in os.listdir('xFiles/'):
    influencerUid = fileName.split('.')[0]
    addNodesFromFile(fileName, influencerUid, graph)
#print graph

maxLen = 0
for key, value in graph.iteritems():
    if len(value) >=5:
        print "hey"
        print value
        print key
connectedGraph = {}

for key, value in graph.iteritems():
    if len(value) >2:
        connectedGraph[key] = value
print connectedGraph
#Impact Calculation
users = [1823975091, 1650111241, 1859586112, 1784473157, 1850988623, 2286908003, 1191965271, 1986926181, 3288976495, 2230312052, 1751714412, 2217035934, 1814040741, 1796445350,1904769205, 1771925961, 2000961721, 2100623570, 2089800791, 1644489953, 1225314032, 5120783603, 1823887605, 1729332983, 2098122492, 2243807243, 1853472775, 1626443785, 2165090317, 3235040884, 1642482194,1682207150, 2847927727,3034112034, 1651428902, 2011075080, 1649159940, 1873625985, 3763936545, 2737798435, 3830136640, 1663414103, 1663937380, 1256947091, 1642634100, 3446047612, 5016338752, 3237705130, 1642632622, 2418433987, 2410528240]

#Posts Impact
postsDictFile=open('userPostsByUserId.json')
postsDict = json.load(postsDictFile)

likesImpact = {}
retweetsImpact = {}
for key, userPosts in postsDict.iteritems():
    likes = 0
    retweets = 0
    postsNumber = len(userPosts)
    for postInfo in userPosts:
        likes+=postInfo["likes"]
        retweets+=postInfo["retweets"]
    impact = float(likes)/postsNumber+float(retweets)/postsNumber
    likesImpact[key] = float(likes)/postsNumber
    retweetsImpact[key] = float(retweets)/postsNumber
sortedUids = likesImpact.keys()
sortedUids.sort()

#FolowersImpact
statsFile=open('userStats.json')
userStats = json.load(statsFile)

statsImpact = {}
for userInfo in userStats:
    statsImpact[str(userInfo["id"])] = math.log(userInfo["followers_count"])
    #print statsImpact[str(userInfo["id"])]


with open('impacts.json','w') as outfile:
    json.dump({"likes":likesImpact,"retweets":retweetsImpact,"followers":statsImpact},outfile)

retweetsList = []
likesList = []
followersList = []
for uid in sortedUids:
    retweetsList.append(retweetsImpact[uid])
    likesList.append(likesImpact[uid])
    followersList.append(statsImpact[uid])
print retweetsList
print likesList
print followersList


def addCostsFromFile(filename, influencerUid, costs,infleunce):
    json_data=open('xFiles/' + filename)
    data = json.load(json_data)
    for user in data:
        if str(user["userId"]) in connectedGraph:
            print user
            if str(user["userId"]) in costs:
                costs[str(user["userId"])] = costs[str(user["userId"])] + math.log(user["followers"]+1)/math.log(user["tweets"]+2)
                infleunce[str(user["userId"])] = infleunce[str(user["userId"])] + math.log(user["followers"]+1)
            else:
                costs[str(user["userId"])] = math.log(user["followers"]+1)/math.log(user["tweets"]+2)
                infleunce[str(user["userId"])] =  math.log(user["followers"]+1)


costs = {}
infleunce = {}

for fileName in os.listdir('xFiles/'):
    influencerUid = fileName.split('.')[0]
    addCostsFromFile(fileName, influencerUid,costs, infleunce)
print len(costs)
print len(infleunce)
sortedFacilitiesUids = costs.keys()
sortedFacilitiesUids.sort()

costsList = []
ownInfList = []
for uid in sortedFacilitiesUids:
    costsList.append(costs[uid])
    ownInfList.append(infleunce[uid])

print sortedFacilitiesUids
connections = []
openFacilities = []
for facil in sortedFacilitiesUids:
    conns = []
    for uid in sortedUids:
        if uid in connectedGraph[facil]:
            conns.append(1)
        else:
            conns.append(0)
    connections.append(conns)
#print connections
#print "Connections"
#print connections

# print "Own Influence"
# print ownInfList
# print "Costs"
# print costsList
#
# print "Retweets"
# print retweetsList
# print "Likes"
# print likesList
# print "Followers"
# print followersList
#for facilityId, influencersIds in connectedGraph.iteritems():

#print connectedGraph