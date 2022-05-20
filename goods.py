
class Goods:

    def __init__(self, id: int, name: str, price: float, unit: str, volume: int, rating: int):
        if not isinstance(id, int):
            raise TypeError('Не верный тип данных для Кода товара')
        self.id = id
        if not isinstance(name, str):
            raise TypeError('Не верный тип данных для Названия товара')
        self.name = name
        if not isinstance(price, float):
            raise TypeError('Не верный тип данных для Цены')
        self.price = price
        if not isinstance(volume, int):
            raise TypeError('Не верный тип данных для Объема')
        self.volume = volume
        if not isinstance(unit, str):
            raise TypeError('Не верный тип данных для Ед.измерения')
        self.unit = unit
        if not isinstance(rating, int):
            raise TypeError('Не верный тип данных для Рейтинга')
        self.rating = rating

