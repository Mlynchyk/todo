class ToDoItem:
    def __init__(self, element, checkbox):  
        self.element = element  
        self.checkbox = checkbox  
      
    def __str__(self, to_file = False) -> str:  
        if to_file:
            return f'{self.checkbox}{self.element}'  
        else:  
            return f'[{self.checkbox}] {self.element}'  
    