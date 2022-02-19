### error-handler
Python error handler with Telegram alerts

`pip install error-handler`

```import handler

handler = handler.setup(telegram_token='TELEGRAM_TOKEN', telegram_channel=TELEGRAM_CHANNEL_ID, full_error=True)

try:
    1 / 0
except Exception as error:
    handler.alert(title='Test', exception=error)
```

Output:
```
Test: Traceback (most recent call last):
  File "A:\Code\Python\packages\handler\test.py", line 6, in <module>
    1 / 0
ZeroDivisionError: division by zero
```