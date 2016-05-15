cd src
cat hosts.bak > hosts
./hosts.py >> hosts
cp hosts /etc/hosts
cd ..
