from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import logging

# logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(levelname)s -[%(threadName)s] %(filename)s:%(lineno)d -:%(message)s')
# logger.setLevel(logging.INFO)

# file_handler = logging.FileHandler('sample.log')
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)

def extendable_logger(log_name, file_name,level=logging.INFO):
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    specified_logger = logging.getLogger(log_name)
    specified_logger.setLevel(level)
    specified_logger.addHandler(handler)
    return specified_logger

basicLogger = extendable_logger('commonlog', 'common_logs.log')
auditLogger = extendable_logger('auditlog', 'audit_log.log')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.app_context().push()

from FlaskLogin import routes