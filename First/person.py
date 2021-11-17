from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Создает и обрабатывает записи о людях
    """
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
#        self.sample = 'Sample'


    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

#    def __repr__(self):
#        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager (Person):
    """
    Настроенная версия Person co специальными требованиями
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, persent, bonus = 0.10):
        Person.giveRaise(self, persent + bonus)


if __name__ == '__main__':

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dex', pay = 100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

#    print(bob.__dict__)
#    print(tom.__dict__)
# просмотр классов и объектов
