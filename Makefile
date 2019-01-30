init:
	#pip install -r requirements.txt
	bash setup.sh
	source env/bin/activate
test:
	nosetests tests
deploy-prod:
	serverless deploy --stage prod --alias prod
	sls s3deploy --stage prod