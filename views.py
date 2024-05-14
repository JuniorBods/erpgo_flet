from flet import *
from pages.cadastro_clientes import cadastro_cliente

def views_change(e):
    match e.control.selected_index:
            case 0:
                pass
            case 1:
                cadastro_cliente(page)
            case 2:
                print('index 2')
            case 3:
                print('index 3')
            case 4:
                print('index 4')
    
if __name__ == "__main__":
    app(target = views_change)