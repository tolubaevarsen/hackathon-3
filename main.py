from pprint import pprint

from mixins import CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin



class Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):




    def start(self):
        def help(self):
            print(
                """
                create - создание записи
                listing - список записей
                retrieve - получение одной записи
                update - обновление записи
                delete - удаление записи
                help - список записи
                quit - выход
                """
            )
        help(self)
        commands = {
            'create':self.create,
            'listing': self.get_db_content,
            'retrieve': self.get_car_by_id,
            'update': self.update,
            'delete': self.delete,
            'help': help
        }
        while True:
            try:
                command = input('Введите комнаду или help для списка команд ').lower().strip()
                if command in commands:
                    commands[command]()
                elif command == 'quit':
                    print('Выход из программы ')
                    break
                else:
                    print('Такой команды нет, попробуйте еще раз!')
            except:
                print('Неверный формат данных, введите заново!')






car = Cars()
# car.create()
# pprint(car.get_db_content())
# car.get_car_by_id()
# car.update()
# car.delete()
car.start()



