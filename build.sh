#!/bin/sh
pip3 install -r requirements.txt --user

for i in $(cat env); do
	export $i
done

cd src/static
npm install
cd ../
python3 app.py