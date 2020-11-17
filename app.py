from flask_mongoengine import MongoEngine
from config import JWT_SECRET_KEY, MONGODB_DB, MONGODB_URI
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': MONGODB_DB,
    'host': MONGODB_URI
}
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

CORS(app, resources={r"*": {"origins": "*", "supports_credentials": True}})


db = MongoEngine(app)
jwt = JWTManager(app)
