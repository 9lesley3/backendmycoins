from flask_restful import Resource, reqparse
import sqlite3
from Filters.CoinsFilter import normalize_path_coins, get_query


def get_data_coins():
    args = reqparse.RequestParser()
    args.add_argument("value_min", type=float, default=0, location="args")
    args.add_argument("value_max", type=float, default=1000, location="args")
    args.add_argument("conservation_state", type=str, default=None, location="args")
    args.add_argument("country", type=str, default=None, location="args")
    args.add_argument("year_min", type=int, default=0, location="args")
    args.add_argument("year_max", type=int, default=2022, location="args")
    args.add_argument("limit", type=float, default=50, location="args")
    args.add_argument("offset", type=float, default=0, location="args")

    return args.parse_args()


def result_to_json(result):
    coins = []
    for linha in result:
        coins.append({
            'coin_id': linha[0],
            'description': linha[1],
            'value': linha[2],
            'conservation_state': linha[3],
            'country': linha[4],
            'year': linha[5]
        })

    return {'coins': coins}


class Coins(Resource):
    @classmethod
    def get(cls):
        connection = sqlite3.connect('coin_database.db')
        cursor = connection.cursor()

        data = get_data_coins()
        # get only data valide
        data_valide = {key: data[key] for key in data if data[key] is not None}
        params = normalize_path_coins(**data_valide)
        query = get_query(params)
        tuple_params = tuple([params[key] for key in params])
        query_result = cursor.execute(query, tuple_params)
        result = result_to_json(result=query_result)

        return result
