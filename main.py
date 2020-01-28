from flask import Flask
import logger
import logging

default_logger = logging.getLogger()
my_logger = logging.getLogger('my.package')


app = Flask(__name__)


default_logger.error("Error !!!!")
default_logger.info("Info !!!!")
my_logger.info('Info !!!')
my_logger.error('Error !!!')


@app.route('/')
def index():
    my_logger.info('Visited index')
    return 'OK'
