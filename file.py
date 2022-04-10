import os 
import common 
from todo_item import ToDoItem

class File:
    
    @staticmethod
    def check_file():
        if os.path.exists(common.FILE_NAME): 
            return open(common.FILE_NAME, "r") 
        else:
            ToDoItem.print_msg(f'File {common.FILE_NAME} is empty')
            file = open(common.FILE_NAME, "w")
            file.close();
            return open(common.FILE_NAME, "r")
            
    @staticmethod        
    def read_file(filename):  
        file = File.check_file() 
        list = []
        for line in file.readlines():
            if line.strip() == "": 
                continue
            if line[0] != "v" and line[0] != " ":
                ToDoItem.print_msg(f'Invalid line: "{line}". First character should be " " or "v"') 
            list.append(ToDoItem(line[1:-1], line[0]))  
        file.close()
        return list  
    
    @staticmethod
    def write_file(filename, list):  
        f = open(filename, "w")  
        for item in list:  
            f.write(item.__str__(True) + '\n')  
        f.close()