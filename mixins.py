import json
from venv import create
from pprint import pprint
from utils import Id



class CreateMixin:

    def type_(self):
            print("""
            Выберите тип кузова(укажите цифру): 
            1. Седан 
            2. Универсал
            3. Купе
            4. Хэтчбек
            5. Минивен
            6. Внедорожник
            7. Пикап
            """)
            choice = int(input('Укажите цифру: '))
            types = ['None', 'Седан', 'Универсал', 'Купе', 'Хэтчбек', 'Минивен', 'Внедорожник', 'Пикап']
            res = types[choice]
            return res

    def create(self):
        brand = input('Введите марку ')
        model = input('Введите модель ')
        year = int(input('Введите год выпуска '))
        volume = float(input('Введите объем двигателя '))
        color = input('Введите цвет автомобиля ')
        type = self.type_()
        mileage = int(input('Введите пробег автомобиля '))
        price = int(input('Введите цену '))
        a = {
            'id': Id().id_,
            'brand':brand, 
            'model': model, 
            'year': year, 
            'volume': volume, 
            'color': color, 
            'type': type, 
            'mileage': f'{mileage}км', 
            'price': f'{price}$'}

        def opener_json():
            with open('db.json') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {'cars': []}
        b = opener_json()
        b['cars'].append(a)
        with open('db.json', 'w') as file:
            json.dump(b, file, indent=4, ensure_ascii=False)
        print("Данные удачно записаны!")
        return a






class ListingMixin:
    def get_db_content(self):
        with open('db.json', 'r') as file:
            return json.load(file)


class RetrieveMixin:
    def get_car_by_id(self):
        car_id = input('Введите id ')
        data = self.get_db_content()
        cars = data['cars']
        for k in cars:
            if car_id == k['id']:
                res = k
                pprint(res if res else 'Не найдено', sort_dicts=False)
                return res if res else None
    

class UpdateMixin():
    def update(self):
        data = self.get_db_content()
        car_ud = self.get_car_by_id()
       
        if car_ud is not None:
            data['cars'].remove(car_ud)
            print('Введите новые данные: ')
            car_ud['id'] = car_ud['id']
            car_ud['brand'] = input('Обновите марку или нажмите Enter: ') or car_ud['brand']
            car_ud['model'] = input('Обновите модель или нажмите Enter: ') or car_ud['model']
            car_ud['year'] = int(input('Обновите год выпуска или нажмите Enter: ')) or car_ud['year']
            car_ud['volume'] = float(input('Обновите объем или нажмите Enter: ')) or car_ud['volume']
            car_ud['color'] = input('Обновите цвет или нажмите Enter: ') or car_ud['color']
            car_ud['type'] = self.type_() or car_ud['type']
            car_ud['mileage'] = int(input('Обновите побег или нажмите Enter: ')) or car_ud['mileage']
            car_ud['price'] = int(input('Обновите цену или нажмите Enter: ')) or car_ud['price']
            print('Успешно обновлено!')
            updated = {
                'id': car_ud['id'],
                'brand': car_ud['brand'], 
                'model': car_ud['model'], 
                'year': car_ud['year'], 
                'volume': car_ud['volume'], 
                'color': car_ud['color'], 
                'type': car_ud['type'], 
                'mileage': car_ud['mileage'], 
                'price': car_ud['price']
                }
            pprint(updated)
            data['cars'].append(updated)
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        else:
            print('Не найдено! ')


class DeleteMixin:
    def delete(self):
        data = self.get_db_content()
        car = self.get_car_by_id()
        if car is not None:
            data['cars'].remove(car)
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print('Успешно удаленo!')
        
        else:
            print('Не найдено!')