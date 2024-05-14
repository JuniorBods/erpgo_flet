from flet import *
from pages.login import login

def views_change(e):
    match e.control.selected_index:
            case 0:
                login
            case 1:
                print('index 1')
            case 2:
                print('index 2')
            case 3:
                print('index 3')
            case 4:
                print('index 4')
    
if __name__ == "__main__":
    app(target = views_change)