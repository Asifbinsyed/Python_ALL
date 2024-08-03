class Vehicle:
    def __new__(cls, wheels:int):
        if wheels==2:
            return Motorbike()
        elif wheels==4:
            return Car()
        else:
            return super().__new__(cls)
        
    def __init__(self, wheels) -> None:
        self.wheels= wheels
        print(f"initializing vehicles with {self.wheels} ")
        
class Motorbike():
    def __init__(self) -> None:
        print("Initializing Motorbike")
    
class Car:
    def __init__(self) -> None:
        print("Initializing car")
        
        
mb=Vehicle(2)   