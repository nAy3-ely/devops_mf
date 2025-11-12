APP_NAME=nayeapp
STACK_FILE=stack.yml

build:
	docker build -t nayeimg:latest .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml quinto

rm:
	docker stack rm quinto



