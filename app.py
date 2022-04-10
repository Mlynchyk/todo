import common
from file import File
from todo_item import ToDoItem

class App:
    @staticmethod
    def show_list(list):
        if len(list) < 1:
            return
        y = 0  
        common.scr.clear()
        for el in list:  
            common.scr.addstr(y, 0, el.__str__())
            y += 1
        common.scr.refresh()

    @staticmethod
    def print_msg(msg, x = 0, y = 0):
        common.scr.clear()  
        common.scr.addstr(y, 0, msg)
        common.scr.refresh()
        
    @staticmethod
    def add_item(el: str):
        list = File.read_file(common.FILE_NAME)  
        list.append(ToDoItem(el, " "))
        File.write_file(common.FILE_NAME, list)  
         
    @staticmethod
    def del_item(index: int) :  
        list = File.read_file(common.FILE_NAME)  
        if not App.check_index(index, list):
            return
        list.pop(index)  
        File.write_file(common.FILE_NAME, list)   

    @staticmethod
    def check_item(index: int):
        list = File.read_file(common.FILE_NAME)
        if not App.check_index(index, list):
            return

        el = list[index]
        if el.checkbox == "v": 
            el.checkbox = " "  
        else: 
            el.checkbox = "v"  
        File.write_file(common.FILE_NAME, list)    
    
    @staticmethod
    def check_index(index, list) -> bool:
        if index < 0:
            App.print_msg(f"The index is too small. You may use indexes from 0 to {len(list) - 1}")
            return False
        if index >= len(list):
            App.print_msg(f"The index is too big. Max index is {len(list) - 1}")
            return False
        else: 
            return True