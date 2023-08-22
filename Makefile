LOCALES_PATH := ./data/locales

run: 
	./bin/entrypoint.sh
compose: 
	docker-compose up -d
logs: 
	docker-compose logs -f app
rebuild: 
	docker-compose up -d --no-deps --force-recreate --build app
mongosh: 
	docker-compose exec mongo mongosh
pybabel_extract: 
	pybabel extract --input-dirs=. -o $(LOCALES_PATH)/bot.pot
pybabel_init: 
	pybabel init -i $(LOCALES_PATH)/bot.pot -d $(LOCALES_PATH) -D bot -l en && \
	pybabel init -i $(LOCALES_PATH)/bot.pot -d $(LOCALES_PATH) -D bot -l ru && \
	pybabel init -i $(LOCALES_PATH)/bot.pot -d $(LOCALES_PATH) -D bot -l uk
pybabel_update: 
	pybabel update -i $(LOCALES_PATH)/bot.pot -d ./data/locales -D bot
pybabel_compile: 
	pybabel compile -d $(LOCALES_PATH) -D bot