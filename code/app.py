from flask import Flask
from flask_restful import Api
from resources.temperature import Temperature, TemperatureList
from resources.sensor import Sensor, SensorList
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
CORS(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Temperature, '/temperatures/')
api.add_resource(TemperatureList, '/temperatures/')
api.add_resource(Sensor, '/sensors/')
api.add_resource(SensorList, '/sensors/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
