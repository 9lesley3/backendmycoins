from flask_restful import reqparse


def get_data_coin():
    args = reqparse.RequestParser()

    args.add_argument('description', type=str, required=True,
                      help="The field 'description' cannot be left blank")
    args.add_argument('value', type=float, required=True,
                      help="The field 'value' cannot be left blank")
    args.add_argument('conservation_state', type=str, required=True,
                      help="The field 'conservation_state' cannot be left blank")
    args.add_argument('country', type=str, required=True,
                      help="The field 'country' cannot be left blank")
    args.add_argument('year', type=int, required=True,
                      help="The field 'year' cannot be left blank")

    return args.parse_args()