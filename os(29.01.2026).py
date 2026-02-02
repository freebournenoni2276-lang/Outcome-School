# def get_unique_item(items):
#     return set(items)

# numbers = [1,1,2,2,2,3,3,4,5,5]
# get_unique_number = get_unique_item(numbers)
# print(get_unique_number)

# class Students:
#     def __init__ (self,name,grade):

#         self.name = name
#         self.grade = grade

# class Car:
#     def __init__ (self, brand, speed):
#         self.brand = brand
#         self.speed = speed


# car1 = Car("Toyota",65)
# car2 = Car("BMW", 150)

# print(car1.brand, car1.speed )
# print(car2.brand,car2.speed)

# class phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery

#     def charge(self):
#         print("Charging......")

# cell_phone = phone("Apple", 50)
# cell_phone.charge()

# print(cell_phone.brand,cell_phone.battery) 

# class Account:
#     def __init__(self,balance):
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#     def withdrawal(self,amount):
#         self.balance -= amount
# acc =Account(1000)
# acc.deposit(500)
# acc.withdrawal(700)
# print(acc.balance)

# class Cart:
#     def __init__(self):
#         self.items = []
#     def add_item(self, item):
#         self.items.append(item)
#     def show_items(self):
#         print(self.items)
    
#     def amount_item(self):
#         return len(self.items)

# cart = Cart()
# cart.add_item("Apple")
# cart.add_item("Banana")
# cart.show_items()
# print(cart.amount_item())