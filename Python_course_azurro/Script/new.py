class Connection:
    __instance= None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("connecting...")
            cls.__instance=super().__new__(cls)
            return cls.__instance
        else:
            print("Warning!! there's already a connection")
            return cls.__instance



    def __init__(self):
        print("Connected to the internet")
        
connection= Connection()
connection2=Connection()

print(connection==connection2)
        
        
