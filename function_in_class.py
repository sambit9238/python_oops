# customer name, id, age, assoiation(in years) 
class Customer:
    #class attributes
    alias = 'God'
    def __init__(self, name, id, age, assoc):
        #instance attributes
        self.name = name
        self.id = id
        self.age = age
        self.assoc = assoc
    #instance method
    def get_cust_info(self):
        return f'Customer {self.name} is {self.age} years old'

    def get_cust_loc(self, loc):
        return f'Customer {self.name} is in {loc} now'

    def __str__(self):
        return f'Customer {self.id}:{self.name}'

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False
    
    @staticmethod
    def entry_cupon(age):
        if age > 50:
            return 5000
        else:
            return 10000

cust1 = Customer('Maggie', 12, 45, 4)
cust2 = Customer('Elisia', 14, 26, 4)
print(Customer.alias)
print(cust1.get_cust_info())
print(cust1.get_cust_loc('Delhi'))
print(cust1)
print(cust1 == cust1, cust1 == cust2)
print(Customer.entry_cupon(42))