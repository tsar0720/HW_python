"""
Написать класс router.
Должен иметь методы добавить/удалить/вывести список ip address.
Должен иметь методы добавить/удалить/вывести список ip routes.

Есть маршруты к непосредственно-подключенным сетям:
если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
значит у него должен быть маршрут:
к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.

Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
то надо проверять доступен ли gateway.

Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.

Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
до которого у нас пока еще нет маршрута, то должен вылетать exception.

Например:
Добавляем ip-address 192.168.5.14/24 eth1.
Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.

Итого - 1 интерфейс и 3 маршрута в таблице.
"""
import ipaddress


class Router:

    def __init__(self):
        self.interface_brief = {'eth1': None, 'eth2': None, 'eth3': None, 'eth4': None}
        self.routing_table = {}
        # routing_table = {ip_adress: set(list)}
        # за одним айпишником ( маршрутизатором ) может быть много сетей, чтобы добавить уникальных нужно сет .add()

    def set_ip_address(self, ip_address, on_interface):
        """
        Метод позволяет установить IP адрес на интерфейс

        Note:
            Если интерфейс не занят можно его использовать
            иначе ошибка "Выберите другой интерфейс"
            добавить в словарь соответствие {ключ - интерфейс : значение - айпишник}
        """
        if self.interface_brief[on_interface] == None:
            self.interface_brief[on_interface] = ip_address
        else:
            print("Порт занят, выберите другой или удалите ip address с порта.")

    def remove_ip_address(self, on_interface):
        """
        Метод позволяет удалить IP адрес с интерфейса
        Note:
            если интерефейс с таким именем есть в interface_brief
            и на нем не установлен IP тогда
            устанавливаем IP в None.
        :param on_interface: С какого интерфеса хотим удалить IP адрес
        :return:
        """
        if on_interface in self.interface_brief and self.interface_brief[on_interface] is not None:
            ip_adress = self.interface_brief[on_interface]
            self.interface_brief[on_interface] = None
            print(f"IP address успешно удален с интерфейса {on_interface} имевший ip address {ip_adress}.")
        else:
            print("На интерфейсе нет IP адреса или интерфейса с таким именем нет.")

    def show_interface_table(self):
        """
        Метод выводит имена интерфейсов и привязанные к ним IP адреса.
        :return:
        """
        print("____________Интерфейсы__________________")
        for key, value in self.interface_brief.items():
            # if value == None:
            #     continue
            print(f"Интерфейс: {key} имеет IP address: {value if value is not None else 'Не установлен'}")

    def set_ip_route(self, through_ip_address, ip_network_destination):
        """
        Метод позволяет установить IP адрес на интерфейс.

        Если IP из одной сетки добавляем в таблицу роутинга

        :param through_ip_address: Через какой IP адрес
        :param ip_network_destination: Какая сеть будет доступна
        :return:
        """
        network = ipaddress.ip_interface(through_ip_address).network
        #print(network)
        # проходимся по всем значениям (IP адрес) interface_brief и сравниваю сетку.
        try:
            for value in self.interface_brief.values():
                if value is None:
                    continue
                elif network == ipaddress.ip_interface(value).network:
                    # добавить в таблицу роутинга если адреса из одной подсети
                    self.routing_table[through_ip_address] = ip_network_destination
                else:
                    raise Exception
        except:
            print(f"Невозможно добавить маршрут к {ip_network_destination} так как нет линка к {through_ip_address}")

        #print(self.routing_table)

    def del_ip_route(self, through_ip_address):
        """
         Метод позволяет удалить из таблицы роутинга маршрут
        # взять ключ ( через какой интерфейс) значение ( какая сеть доступна) и удалить из роутинга
        :param self:
        :param through_ip_address:
        :return:
        """
        if through_ip_address in self.routing_table:
            del self.routing_table[through_ip_address]
            print("Успешно удалён.")
        else:
            print("Нет такого маршрута.")

        print(self.routing_table)

    def show_ip_route(self):
        print("Routing Table:")
        if not self.routing_table:
            print("Таблица маршрутизации пуста.")
        for key, value in self.routing_table.items():
            print(f" {value} доступен через {key}")


r = Router()
print(r.set_ip_address('192.168.1.1/24', 'eth1'))
print(r.interface_brief)
r.set_ip_address('192.168.1.1/24', 'eth1')
r.remove_ip_address('eth2')
r.show_interface_table()
print("__________________________________________")
r.set_ip_route('192.168.1.2/24', '172.16.0.0/16')
r.del_ip_route("192.168.2.2/24")
r.set_ip_route('192.168.8.2/24', '172.16.0.0/16')
# r.show_ip_route()
# r.del_ip_route('192.168.1.2/24')
r.show_ip_route()
