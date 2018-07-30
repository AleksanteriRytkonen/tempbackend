from db import db
from datetime import datetime

class SensorModel(db.Model):
    __tablename__ = 'sensordata'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float(precision=2))
    moisture = db.Column(db.Integer)
    lightness = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, temperature, moisture, lightness):
        self.temperature = temperature
        self.moisture = moisture
        self.lightness = lightness
        self.date = datetime.now()

    def json(self):
        return {'temperature': self.temperature, 'moisture': self.moisture, 'lightness': self.lightness, 'date': self.date.isoformat()}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()