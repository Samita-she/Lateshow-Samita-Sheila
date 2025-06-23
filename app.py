# app.py

from flask import Flask
from flask_migrate import Migrate
from models import db
from config import Config  # <-- notice this is now from config import Config
from models import db, Guest, Episode, Appearance
from flask import Flask, request, jsonify


app = Flask(__name__)
app.config.from_object(Config)  # <-- and this uses the Config class

# Debug print
print("Loaded DB URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict(only=('id', 'date', 'number')) for e in episodes]), 200

@app.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict(rules=('appearances',))), 200

@app.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict(only=('id', 'name', 'occupation')) for g in guests]), 200

@app.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data["rating"],
            guest_id=data["guest_id"],
            episode_id=data["episode_id"]
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict(rules=('episode', 'guest'))), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == "__main__":
    app.run(debug=True)
