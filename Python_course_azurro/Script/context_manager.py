# Context manager help you to open the file and close the file automatically 

class File: 
    def __init__(self, name: str): 
        self.name = name 
        
    def __enter__(self): 
        print(f'Opening the file {self.name}')
        return self 
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        print(f'Closing file name {self.name}')
        
if __name__=='__main__': 
    with File("context_manager.py") as file: 
        print(file.name)
        
    print("Done")