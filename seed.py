# seed.py
import csv
from app import app
from models import db, Guest

with app.app_context():
    db.session.query(Guest).delete()

    with open("guests.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            guest = Guest(name=row["name"], occupation=row["occupation"])
            db.session.add(guest)
        db.session.commit()
