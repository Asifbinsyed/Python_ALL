from typing import Protocol

class Printable(Protocol):
    pages:int

    def print(self):
        pass
    
    def recyclable(self):
        pass
    
    
class Book:
    pages:int
    
    def __init__(self, title:str) -> None:
        self.title= title
        
    def print(self):
        print(f"this is the {self.title}")
    
    def recyclable(self):
        pass

def print_item(printable:Printable):
    printable.print()
    
book:Printable= Book('python')
print_item(book)