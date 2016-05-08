curl -H Accept:application/json -H Content-Type:application/json -d '{"query":"match (n:User) return n.userID limit 5"}' -v http://localhost:7474/db/data/cypher
