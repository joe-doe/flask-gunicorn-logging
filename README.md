# flask-gunicorn-logging
Cookbook for logging with flask and gunicorn

## Precautions 
`WARNING`

import provided logger module before you create flask app

## Run
### Clone
```bash
git clone git@github.com:joe-doe/flask-gunicorn-logging.git
```

### Create virtual environment
```bash
virtualenv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -U -r requirements.txt 
```

### Execute (while in virtual environment)
```bash
gunicorn --bind 0.0.0.0:5000 --log-level debug --preload main:app
```


## Details
I use `default` logger to log all messages from libraries and logger `my.package`
to load application messages

In `loggers` section you will see different handlers for `default` and `my.package`
loggers. For `default` logger write in file `logs/info.log` and `logs/error.log`
and for `my.package` logger write to `logs/my.info.log` and `logs/my.error.log`


## Usage
In every module you want to use logger, just call
```python
default_logger = logging.getLogger()
my_logger = logging.getLogger('my.package')
```
just after imports, and use it like

```python
my_logger.error('Error message')
```
