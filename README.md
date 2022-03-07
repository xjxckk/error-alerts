### error-alerts
Python error alerts via Telegram

Installation:
`pip install error-alerts`

Options:

`full_error` (False by default): Send full traceback with line of code where error occurred (see sample below).

`raise_error` (False by default): Raise error and exit code when there is an error. If this is not set to True an alert will be sent and the code will continue running.

Usage:
```
import alerts

alerts = alerts.setup(telegram_token='TELEGRAM_TOKEN', telegram_channel=TELEGRAM_CHANNEL_ID, full_error=True, raise_error=True)

try:
    1 / 0
except Exception as error:
    alerts.send(title='Test', exception=error)
```

Output:
```
Test: Traceback (most recent call last):
  File "A:\Code\Python\packages\handler\test.py", line 6, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

Prints that in console and sends a Telegram alert to the channel you specified
