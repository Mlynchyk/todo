# Available arguments:  
#   --add   - add todo element. Format: --add "item name"  
#   --del   - remove element by index. Format: --del X  
#   --check - check\uncheck el.by index. Format: --check X  
# 
import sys
from curses import wrapper  
from file import File
from app import App
from args import Args
import common

def main(stdscr): 
    common.init(stdscr)
    
    if not Args.enough_args():   # < 2
        App.show_list(File.read_file(common.FILE_NAME))
        common.scr.getkey()
        return
  
    Args.parse_args(sys.argv)
    common.scr.getkey()
      
wrapper(main)