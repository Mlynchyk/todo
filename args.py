import sys
from app import App

class Args: 
    @staticmethod
    def check_args(args, cmd):
        if len(args) < 3:
            App.print_msg("You have to enter the second argument")
            return False
        
        map = {'--add': False, '--del': True, '--check': True}
        if not cmd in map:
            App.print_msg("Invalid command")
            return False
        
        if map[cmd] and not args[2].isnumeric():
            App.print_msg("Argument should be a number")
            return False
        
        return True
    
    @staticmethod
    def parse_args(args):  
        if not Args.check_args(args, args[1]):
            return

        if args[1] == '--add':
            App.add_item(args[2])
        elif args[1] == '--del':
            App.del_item(int(args[2]))
        elif args[1] == '--check':
            App.check_item(int(args[2]))
            
    @staticmethod
    def enough_args() -> bool:
        return len(sys.argv) >= 2