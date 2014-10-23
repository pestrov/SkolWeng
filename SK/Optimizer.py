import os, json

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
print graph

maxLen = 0
for key, value in graph.iteritems():
    if len(value) >= maxLen:
        maxLen = len(value)
        print maxLen
