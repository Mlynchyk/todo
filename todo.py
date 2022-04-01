from curses import wrapper 
import sys 
 
class ToDoItem: 
    def __init__(self, element, checkbox): 
        self.element = element 
        self.checkbox = checkbox 
     
    def __str__(self) -> str: 
        return f'[{self.checkbox}] {self.element}' 
 
def read_file(file):         
    our_list = [] 
    filename = open(file, 'r') 
    for line in filename.readlines(): 
        our_list.append(ToDoItem(line[1:-1], line[0]))     
    filename.close() 
    return our_list 
 
def write_file(file, list): 
    # open file, convert list of ToDoItem to list of strings, append to file 
    return 
 
def show_list(stdscr, list): 
    y = 0 
    stdscr.clear() 
    for el in list: 
        stdscr.addstr(y, 0, el.__str__()) 
        y += 1 
    stdscr.refresh() 
    stdscr.getkey() 
 
def parse_args(args): 
    if args[1] == '--add': 
        print('add') 
        return 
    elif args[1] == '--del': 
        print('del') 
        return 
     
def main(stdscr): 
    if len(sys.argv) < 2: 
        show_list(stdscr, read_file('todo.txt')) 
        return 
 
    parse_args(sys.argv) 
 
wrapper(main)