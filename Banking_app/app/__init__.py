from flask import Flask
from flask_jwt_extended import JWTManager
from app.controllers.user_management_route import user_routes
from app.controllers.account_management_route import account_routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

app.register_blueprint(user_routes)
app.register_blueprint(account_routes)

@app.route('/')
def my_app():
    return 'Hello World!'