import csv
from app import app
from models import db, Guest, Episode
from datetime import datetime

with app.app_context():
    # Clear old data (optional)
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()

    with open('guests.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        episode_map = {}  # to avoid duplicate episodes
        for i, row in enumerate(reader, start=1):
            guest_name = row["Raw_Guest_List"].strip()
            occupation = row["GoogleKnowlege_Occupation"].strip()
            show_date_str = row["Show"].strip()

            # Add guest
            guest = Guest(name=guest_name, occupation=occupation)
            db.session.add(guest)

            # Only create a new episode for each unique date
            if show_date_str not in episode_map:
                try:
                    episode = Episode(
                        date=show_date_str,
                        number=i  # or use a counter/ID manually
                    )
                    db.session.add(episode)
                    episode_map[show_date_str] = episode
                except Exception as e:
                    print("Error parsing episode:", e)

        db.session.commit()
        print(f"Seeded {len(episode_map)} episodes and guests.")

