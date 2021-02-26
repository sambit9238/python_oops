# customer name, id, age, assoiation(in years) 
customer1 = ['maggie', 12, 45, 4]
customer2 = ['elisia', 14, 26, 4]

class Customer:
    #class attributes
    alias = 'God'
    def __init__(self, name, id, age, assoc):
        #instance attributes
        self.name = name
        self.id = id
        self.age = age
        self.assoc = assoc

cust1 = Customer('maggie', 12, 45, 4)
print(cust1.name)
print(Customer.alias)