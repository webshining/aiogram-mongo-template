from loader import dp, bot


if __name__ == '__main__':
    import app.handlers
    dp.run_polling(bot)