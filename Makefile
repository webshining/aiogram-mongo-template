run: python app.py
compose: docker-compose up -d
logs: docker-compose logs -f app
rebuild: docker-compose up -d --build --no-deps --force-recreate
mongosh: docker-compose exec mongo mongosh
pybabel_extract: pybabel extract --input-dirs=. -o ./data/locales/bot.pot
pybabel_init: pybabel init -i data/locales/bot.pot -d data/locales -D bot -l en && \
			  pybabel init -i data/locales/bot.pot -d data/locales -D bot -l ru && \
			  pybabel init -i data/locales/bot.pot -d data/locales -D bot -l uk
pybabel_update: pybabel update -i ./data/locales/bot.pot -d ./data/locales -D bot
pybabel_compile: pybabel compile -d ./data/locales -D bot