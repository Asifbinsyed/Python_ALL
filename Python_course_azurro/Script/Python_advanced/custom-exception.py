class NegativeException(Exception):
    """ Raised if a value is below zero """
    def __init__(self, number: float, error_code: int): 
        self.number = number
        self.error_code = error_code
        super().__init__(f' {self.number} is less than 0 (Error code {self.error_code}, self.number, self.error_code)')
        
    def __str__(self) -> str:
        return f' {self.number} is less than 0 (Error code {self.error_code})'
    
    def custom_method(self): 
        print((self.number, self.error_code), 'were used in custome method')
            
try: 
    raise NegativeException(-5, 999)
except NegativeException as e : 
    print(e) 
    print(e.args)
    print(e.custom_method())
    