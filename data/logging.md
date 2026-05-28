## Logging

### Configuration for rotating files and console

Initial setup:

```python
import logging
logFormatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

# Rotating Log File
fileHandler = handlers.RotatingFileHandler("app.log", maxBytes=(1048576*5), backupCount=7)
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

# Console
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
```

Logging usage:

```Python
logging.info("this is an info message")
logging.debug("this is a debug message")
logging.warning("this is a warning message")
logging.error("this is an error message")
```
**References:** [Logging Handlers](https://docs.python.org/3/library/logging.handlers.html)