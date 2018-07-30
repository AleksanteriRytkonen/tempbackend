from flask_restful import Resource, reqparse
from models.sensor import SensorModel

class Sensor(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('temperature', type=float, required=True, help="Temperature is required")
    parser.add_argument('moisture', type=int, required=True, help="Moisture is required")
    parser.add_argument('lightness', type=int, required=True, help="Light value is required")

    def post(self):
        data = Sensor.parser.parse_args()
        sensorData = SensorModel(**data)
        try:
            sensorData.save_to_db()
        except:
            return {"message": "And error occured while saving sensor data."}, 500

        return sensorData.json(), 201

class SensorList(Resource):
    def get(self):
        return {'data': list(map(lambda x: x.json(), SensorModel.query.all()))}
