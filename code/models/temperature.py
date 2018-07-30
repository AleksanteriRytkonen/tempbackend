from db import db


class TemperatureModel(db.Model):
    __tablename__ = 'temperatures'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float(precision=2))
    time = db.Column(db.String(80))

    def __init__(self, temperature, time):
        self.temperature = temperature
        self.time = time

    def json(self):
        return {'temperature': self.temperature, 'time': self.time}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
