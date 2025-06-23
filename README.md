# Late Show API

This is a Flask-based RESTful API for managing episodes, guests, and their appearances on a fictional "Late Show". It supports full CRUD operations for appearances and allows querying episodes and guests using specified endpoints.

## 📁 Project Structure

lateshow-your-name/
├── app.py
├── config.py
├── models.py
├── seed.py
├── guests.csv
├── challenge-4-lateshow.postman_collection.json
├── migrations/
└── README.md


---

## 📋 Requirements

- Python 3.10+
- Flask
- Flask-Migrate
- Flask-SQLAlchemy
- SQLAlchemy-Serializer
- CSV for seeding data

Install requirements with:

pip install -r requirements.txt

🧠 Models Overview
Episode
id: integer, primary key

date: string

number: integer

Guest
id: integer, primary key

name: string

occupation: string

Appearance
id: integer, primary key

rating: integer (1–5)

episode_id: foreign key

guest_id: foreign key

Relationships:

An Episode has many Guests through Appearance

A Guest has many Episodes through Appearance

Appearances are deleted if their Episode or Guest is deleted (cascade)

✅ Validations
Appearance.rating must be between 1 and 5 (inclusive)

🌐 API Endpoints
GET /episodes
Returns a list of all episodes.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  ...
]
GET /episodes/<id>
Returns a single episode by ID with its appearances.

Response (if found):

json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
If not found:

json
{
  "error": "Episode not found"
}
GET /guests
Returns a list of all guests.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  ...
]
POST /appearances
Creates a new appearance.

Request body:

json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
Success response:

json
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
Failure response (invalid data):

json
{
  "errors": ["validation errors"]
}
🧪 Running the App
flask run
Ensure the following is set:
export FLASK_APP=app

🗂️ Database Setup
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

🌱 Seeding the Database
You can seed data from the provided guests.csv using:
python seed.py

📮 Testing with Postman
Use the provided challenge-4-lateshow.postman_collection.json

Open Postman → Import → Upload the JSON file

Use it to test all endpoints

🧾 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this code with attribution and without warranty.

✍️ Author

GitHub Profile
Samita-she









