from flask import Flask
from flask_jwt_extended import JWTManager
from app.controllers.user_management_route import user_routes
import os

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('super-secret-key')
jwt = JWTManager(app)

app.register_blueprint(user_routes)

@app.route('/')
def my_app():
    return 'Hello World!'