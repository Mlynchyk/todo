# Available arguments: 
#   --add   - добавить todo элемент. Формат: --add "item name" 
#   --del   - удалить элемент по индексу. Формат: --del X 
#   --check - выбрать\отменить элемент по индексу. Формат: --check X 
# 
from curses import wrapper 
import sys 
 
class ToDoItem: 
    def __init__(self, element, checkbox): 
        self.element = element 
        self.checkbox = checkbox 
     
    def __str__(self, to_file = False) -> str: 
        if to_file: 
            return f'{self.checkbox}{self.element}' 
        else: 
            return f'[{self.checkbox}] {self.element}' 
 
def read_file(filename): 
    list = [] 
    file = open(filename, 'r') 
    for line in file.readlines(): 
        list.append(ToDoItem(line[1:-1], line[0])) 
    file.close() 
    return list 
 
def write_file(filename, list): 
    f = open(filename, "w") 
    for item in list: 
        f.write(item.__str__(True) + '\n') 
    f.close() 
 
def show_list(stdscr, list): 
    y = 0 
    stdscr.clear() 
    for el in list: 
        stdscr.addstr(y, 0, el.__str__()) 
        y += 1 
    stdscr.refresh() 
    stdscr.getkey() 
 
#def add_item(args): 
     
def parse_args(args): 
    FILE_NAME = "todo.txt" 
    # TODO: move this code to separate function 
    if args[1] == '--add': 
        #add_item(args[2]) 
        list = read_file(FILE_NAME) 
        list.append(ToDoItem(args[2], " ")) 
        write_file(FILE_NAME, list)  
        return 
    # elif args[1] == '--del': 
    #     read_file(FILE_NAME) 
    #     list.pop(args[2]) 
    #     write_file(FILE_NAME)  
    #     return 
    # elif args[1] == '--check': 
    #     read_file(FILE_NAME) 
    #     list[args[2]] = 'v'+list[args[2]].__str__() 
    #     write_file(FILE_NAME)   
    #     return 
     
def main(stdscr): 
    if len(sys.argv) < 2: 
        show_list(stdscr, read_file('todo.txt')) 
        return 
 
    parse_args(sys.argv) 
 
wrapper(main)
