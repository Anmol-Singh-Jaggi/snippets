cat src/hosts.bak > src/hosts
python src/hosts.py >> src/hosts
cp src/hosts /etc/hosts
