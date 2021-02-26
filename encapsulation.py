#inherits, extens, overrides
import random

class Customer:
    def __init__(self, name, age, assoc):
        self.name = name
        self.age = age
        self.assoc = assoc
        self._id = random.randint(0,900)
        self._email = None

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email
        return True

    def __str__(self):
        return f'Customer {self.name} is a great customer'

cust1 = Customer('Maggie', 43, 1)
print(cust1)
print(cust1.get_email())
cust1.set_email('abc@gmail.com')
print(cust1.get_email())