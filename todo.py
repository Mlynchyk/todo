# Available arguments:   
#   --add   - add todo element. Format: --add "item name"   
#   --del   - remove element by index. Format: --del X   
#   --check - check\uncheck el.by index. Format: --check X   
#  
from curses import wrapper   
import sys   
import os  
   
FILE_NAME = "todo.txt"  
scr = None 
class ToDoItem: 
    def __init__(self, element, checkbox):   
        self.element = element   
        self.checkbox = checkbox   
       
    def __str__(self, to_file = False) -> str:   
        if to_file: 
            return f'{self.checkbox}{self.element}'   
        else:   
            return f'[{self.checkbox}] {self.element}'   
   
def check_file(): 
    if os.path.exists(FILE_NAME):  
        return open(FILE_NAME, "r")  
    else: 
        print_msg(f'File {FILE_NAME} is empty') 
        file = open(FILE_NAME, "w") 
        file.close(); 
        return open(FILE_NAME, "r") 
          
def read_file(filename):   
    file = check_file()  
    list = [] 
    for line in file.readlines(): 
        if line.strip() == "":  
            continue 
        if line[0] != "v" and line[0] != " ": 
            print_msg(f'Invalid line: "{line}". First character should be " " or "v"')  
        list.append(ToDoItem(line[1:-1], line[0]))   
    file.close() 
    return list   
   
def write_file(filename, list):   
    f = open(filename, "w")   
    for item in list:   
        f.write(item.__str__(True) + '\n')   
    f.close()   
   
def show_list(list): 
    if len(list) < 1: 
        return 
    y = 0   
    scr.clear() 
    for el in list:   
        scr.addstr(y, 0, el.__str__()) 
        y += 1 
    scr.refresh() 
 
def print_msg(msg, x = 0, y = 0): 
    scr.clear()   
    scr.addstr(y, 0, msg) 
    scr.refresh() 
 
def add_item(el: str): 
    list = read_file(FILE_NAME)   
    list.append(ToDoItem(el, " ")) 
    write_file(FILE_NAME, list)    
      
  
def del_item(index: int) :   
    list = read_file(FILE_NAME)   
    list.pop(index)   
    write_file(FILE_NAME, list)    
  
  
def check_item(index: int): 
    list = read_file(FILE_NAME) 
    if index < 0: 
        print_msg(f"The index is too small. You may use indexes from 0 to {len(list) - 1}") 
        return 
    if index >= len(list): 
        print_msg(f"The index is too big. Max index is {len(list) - 1}") 
        return 
 
    el = list[index] 
    if el.checkbox == "v":  
        el.checkbox = " "   
    else:  
        el.checkbox = "v"   
    write_file(FILE_NAME, list)     
      
def check_args(args, cmd): 
    if len(args) < 3: 
        print_msg("You have to enter the second argument") 
        return False 
     
    map = {'--add': False, '--del': True, '--check': True} 
    if not cmd in map: 
        print_msg("Invalid command") 
        return False 
     
    if map[cmd] and not args[2].isnumeric(): 
        print_msg("Argument should be a number") 
        return False 
     
    return True 
     
def parse_args(args):   
    if not check_args(args, args[1]): 
        return 
 
    if args[1] == '--add': 
        add_item(args[2]) 
    elif args[1] == '--del': 
        del_item(int(args[2])) 
    elif args[1] == '--check': 
        check_item(int(args[2])) 
 
def main(stdscr):  
    global scr 
    scr = stdscr 
    if len(sys.argv) < 2: 
        show_list(read_file(FILE_NAME)) 
        scr.getkey() 
        return   
   
    parse_args(sys.argv) 
    scr.getkey() 
       
wrapper(main)
