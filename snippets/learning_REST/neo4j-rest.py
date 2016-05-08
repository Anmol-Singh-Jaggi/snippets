import requests
import json

url = "http://localhost:7474/db/data/cypher"
data = {"query":"match (n:User) return n.userID limit 5"}

print json.loads(requests.post(url, data=json.dumps(data)).content)["data"]
