class Person:
    sample = "sample"

    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager (Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, persent, bonus = 0.10):
        Person.giveRaise(self, persent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dex', pay = 10000)
    tom = Manager('Tom Jones', 50000)

    print(bob.__dict__)
    print(bob.__dict__.keys())
    print(dir(bob))
    print(bob.__class__)
    print(bob.__class__.__name__)
    print(tom.__class__)
    print(tom.__class__.__name__)

    print(list(name for name in dir(bob) if not name.startswith('__')))
