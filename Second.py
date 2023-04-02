class Vehicle:
    name = "Vehicle"

    def __init__(self) -> None:
        pass

class Car(Vehicle):
  
    def __init__(self, message="car") -> (None):
        self.carName = message
        super().__init__()



t = Vehicle()
u = Car()
v = Car(message="Toyota")
print(t.name)
print(u.carName + u.name)
print(v.name + v.carName)