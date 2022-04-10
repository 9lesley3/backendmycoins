from sql_alchemy import database


class ModelCoin(database.Model):
    __tablename__ = 'coins'

    coin_id = database.Column(database.Integer, primary_key=True)
    description = database.Column(database.String(100))
    value = database.Column(database.Float(precision=2))
    conservation_state = database.Column(database.String(10))
    country = database.Column(database.String(20))
    year = database.Column(database.Integer)

    def __init__(self, coin_id, description, value, conservation_state, country, year):
        self.coin_id = coin_id
        self.description = description
        self.value = value
        self.conservation_state = conservation_state
        self.country = country
        self.year = year

    def to_json(self):
        return {
            'coin_id': self.coin_id,
            'description': self.description,
            'value': self.value,
            'conservation_state': self.conservation_state,
            'country': self.country,
            'year': self.year,
        }

    @classmethod
    def find_by_id(cls, coin_id):
        coin = cls.query.filter_by(coin_id=coin_id).first()  # SELECT * FROM coins WHERE coin_id = $coin_id limited
        if coin:
            return coin
        return None

    def save_coin(self):
        database.session.add(self)
        database.session.commit()

    def update_coin(self, description, value, conservation_state, country, year):
        self.description = description
        self.value = value
        self.conservation_state = conservation_state
        self.country = country
        self.year = year

    def delete_coin(self):
        database.session.delete(self)
        database.session.commit()
