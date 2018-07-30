from flask_restful import Resource, reqparse
from models.temperature import TemperatureModel

class Temperature(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('temperature',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('time',
                        type=str,
                        required=True,
                        help="Time cant be blank")

    def post(self):
        data =  Temperature.parser.parse_args()

        temperature = TemperatureModel(**data)

        try:
            temperature.save_to_db()
        except:
            return {"message": "An error occured while saving the temperature."}, 500

        return temperature.json(), 201

class TemperatureList(Resource):
    def get(self):
        return {'temperatures': list(map(lambda x: x.json(), TemperatureModel.query.all()))}