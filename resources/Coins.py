from flask_restful import Resource
import sqlite3
from Filters.CoinsFilter import get_data_coins, normalize_path, get_query, result_to_json


class Coins(Resource):
    @classmethod
    def get(cls):
        connection = sqlite3.connect('coin_database.db')
        cursor = connection.cursor()

        data = get_data_coins()
        # get only data valide
        data_valide = {key: data[key] for key in data if data[key] is not None}
        params = normalize_path(**data_valide)
        query = get_query(params)
        tuple_params = tuple([params[key] for key in params])
        query_result = cursor.execute(query, tuple_params)
        result = result_to_json(result=query_result)

        return result
