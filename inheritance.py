#inherits, extens, overrides
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Customer {self.name} is a great customer'
customer1 = ['maggie', 12, 45, 4]
customer2 = ['elisia', 14, 26, 4]

class ProSub(Customer):
    def __init__(self, name, age, price):
        super().__init__(name, age)
        self.price = price
    
    def get_report(self):
        return f'self.name is 5 months away from goal'

    def __str__(self):
        return f'Customer {self.name} is a Pro customer'

class LiteSub(Customer):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email
cust1 = ProSub('Maggie', 32, 500)
cust2 = LiteSub('Elisia', 42, 'els@gmail.com')
print(cust1,'\n', cust2)