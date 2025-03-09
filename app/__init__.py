from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object(Config)

bootstrap = Bootstrap5(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Войдите в аккаунт для получения доступа'

from app.controllers import theme_controller, home_controller, auth_controller, client_controller, supplier_controller, products_controller, employee_controller, order_controller, userpage_controller
from app.models import suppliers, client, employees, orders, product, user, qa, support