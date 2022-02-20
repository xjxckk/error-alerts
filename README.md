### error-handler
Python error handler with Telegram alerts

`pip install error-handler`

Usage:
```
import handler

handler = handler.setup(telegram_token='TELEGRAM_TOKEN', telegram_channel=TELEGRAM_CHANNEL_ID, full_error=True)

try:
    1 / 0
except Exception as error:
    handler.alert(title='Test', exception=error)
    # raise Exception('Raiser') from exception # If you want to raise the exception rather than continue
```

Output:
```
Test: Traceback (most recent call last):
  File "A:\Code\Python\packages\handler\test.py", line 6, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

Prints that in console and sends a Telegram alert to the channel you specified
