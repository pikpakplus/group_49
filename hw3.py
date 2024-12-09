class Computer:
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.cpu * self.memory

    def __str__(self):
        return f'Computer (cpu={self.cpu}, memory={self.memory})'

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 0 <= sim_card_number < len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number]
            print(f'Звонок идет на номер {call_to_number} с сим-карты-{sim_card_number + 1} ({sim_card})')
        else:
            print('Неверный номер сим-карты')

    def __str__(self):
        return f'Phone (sim_cards_list={self.sim_cards_list})'


class SmartPhone(Computer, Phone):
    def __init__(self,cpu, memory, __sim_cards_list):
        Computer.__init__(self,cpu, memory)
        Phone.__init__(self, __sim_cards_list)
    def use_gps(self, location):
        print(f'Маршрут построен до {location}')

    def __str__(self):
        return f'SmartPhone (cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})'

computer = Computer(4, 16)
phone = Phone(["Beeline", "MegaCom", "O!"])
smartphone1 = SmartPhone(8, 32, ["Beeline", "O!"])
smartphone2 = SmartPhone(16, 64, ["MegaCom", "O!"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print(computer.make_computations())
phone.call(0, "+996 701 50 00 50")

smartphone1.use_gps("Каракол")
smartphone2.use_gps("Нарын")

print(computer == smartphone1)
print(computer > smartphone2)
