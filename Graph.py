# This creates a mark for every user in the list of users
import igraph as ig
data = []
req = urllib2.Request("out.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.loads(f.read())


# creating node for each user
N=len(data['nodes'])
 
# Connecting links between the user for a mail sent or received
L=len(data['links'])
Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]
G=ig.Graph(Edges, directed=False)
