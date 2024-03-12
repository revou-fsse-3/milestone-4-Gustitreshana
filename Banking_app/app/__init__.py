from flask import Flask
from flask_jwt_extended import JWTManager
from app.controllers.user_management_route import user_routes
from app.controllers.account_management_route import account_routes
from app.controllers.transaction_management_route import transaction_routes
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Set the JWT secret key
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Register the blueprints
app.register_blueprint(user_routes)
app.register_blueprint(account_routes)
app.register_blueprint(transaction_routes)

# Add the root route
@app.route('/')
def my_app():
    return 'Hello World!'