<<<<<<< HEAD
import traceback, telegram

class setup:
    def __init__(self, telegram_token, telegram_channel, full_error=False, raise_error=False):
        self.bot = telegram.Bot(token=telegram_token)
        self.channel = telegram_channel
        self.full_error = full_error
        self.raise_error = raise_error
    def send(self, title, exception):
        error = str(exception)
        if self.full_error:
            error = traceback.format_exc()
        message = f'{title}: {error}'
        self.bot.send_message(self.channel, message)
        print(message)
        print()
        if self.raise_error:
=======
import traceback, telegram

class setup:
    def __init__(self, telegram_token, telegram_channel, full_error=False, raise_error=False):
        self.bot = telegram.Bot(token=telegram_token)
        self.channel = telegram_channel
        self.full_error = full_error
        self.raise_error = raise_error
    def send(self, title, exception):
        error = str(exception)
        if self.full_error:
            error = traceback.format_exc()
        message = f'{title}: {error}'
        self.bot.send_message(self.channel, message)
        print(message)
        print()
        if self.raise_error:
>>>>>>> 8b495d93b88c3bead1b5685a1069d23dfc62037b
            raise Exception('Raiser') from exception