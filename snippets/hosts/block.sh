cd src
cat hosts.bak > hosts
python hosts.py >> hosts
cp hosts /etc/hosts
cd ..
