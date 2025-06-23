# app.py

from flask import Flask
from flask_migrate import Migrate
from models import db
from config import Config  # <-- notice this is now from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # <-- and this uses the Config class

# Debug print
print("Loaded DB URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
