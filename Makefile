LOCALES_PATH := ./data/locales

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