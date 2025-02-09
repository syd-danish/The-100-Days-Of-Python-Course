class Tenant:
    def __init__(self, name,flat_no,money_owed):
        self.name = name
        self.flat_no = flat_no
        self.money_owed = money_owed
    def __repr__(self):
        return f"{self.name} resides at {self.flat_no} and owes {self.money_owed}" #for developer purposes
    def __str__(self):
        return f"Name:{self.name}, Flat: {self.flat_no}, Money Owed: {self.money_owed}." #for end users and UI
    def __eq__(self,other):
        return self.__dict__==other.__dict__
    def __format__(self, format_spec):
        match format_spec:
            case "Rs":
                return f"{self.money_owed * 23.56:.1f}"
            case "$":
                return f"{self.money_owed * .27:.1f}"
    def __or__(self, other):
        new_name=f"{self.name} & {other.name}"
        new_flat=f"{self.flat_no} & {other.flat_no}"
        new_money_owed= self.money_owed+other.money_owed
        return Tenant(name=new_name,flat_no=new_flat, money_owed=new_money_owed)
    def money_owe(self):
        return self.money_owed.__str__() #returns money owed as a string
    def set_new_money(self,money_owed):
        self.money_owed=money_owed #sets new value for the parameter
        return self.money_owed.__repr__() #you can use __str__ too



tenant1=Tenant("Paddy","G03",100000)
tenant2=Tenant("Paddy","G03",100000)
tenant3=Tenant("Paddy","G03",10000)
tenant4=Tenant("Ilia","303",2000)
print(tenant1==tenant2) #true because of __eq__ method
print(tenant1==tenant3) #false because __dict__ in __eq__ compares every parameter inside the Tenant class
print(tenant1) #uses the __str__ method by default, if not, then it falls back to __repr__
print(repr(tenant1)) #uses __repr__
print(tenant1.money_owe()) #function returns an integer value as string
tenant1.set_new_money(200000) #sets new value and prints it out
print(f"{tenant1:Rs}")
print(f"{tenant1:$}")
combined=tenant1|tenant4 #use __or__ dunder!
print(combined) # it's going to default to the str method to print the or dunder!
