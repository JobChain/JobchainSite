<<<<<<< HEAD
#!/bin/sh
pip3 install -r requirements.txt --user

for i in $(cat env); do
	export $i
done

=======
pip3 install -r requirements.txt --user
>>>>>>> 15fd1f70cc9d43a264d316d3ad0fb5c22ad098e7
cd src/static
npm install
cd ../
python3 app.py