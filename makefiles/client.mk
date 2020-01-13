### client
# ¯¯¯¯¯¯¯¯¯¯¯

client.start: ## Start client in its docker container
	docker-compose up client

client.stop: ## stop client container
	docker-compose stop

