init:
	#pip install -r requirements.txt
	bash setup.sh
	source env/bin/activate
test:
	nosetests tests