import traceback, telegram

class setup:
    def __init__(self, telegram_token, telegram_channel, full_error=False):
        self.bot = telegram.Bot(token=telegram_token)
        self.channel = telegram_channel
        self.full_error = full_error
    def alert(self, title, exception):
        error = str(exception)
        if self.full_error:
            error = traceback.format_exc()
        message = f'{title}: {error}'
        self.bot.send_message(self.channel, message)
        print(message)
        print()