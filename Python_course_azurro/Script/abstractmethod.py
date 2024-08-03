from abc import ABC, abstractmethod

class Phone(ABC):
    def __init__(self, model:str):
        self.model= model
    
    @property 
    @abstractmethod
    def power(self):
        ...
        
    @abstractmethod
    def call_target(self, person:str):
        ...
        


