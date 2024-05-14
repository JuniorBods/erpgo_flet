import flet as ft
import pages.login as log

def pagina(page: ft.Page):
    page.drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.Image(src='.\\assets\\okimoveis.jpg', border_radius=ft.border_radius.all(500), height=150),
                ft.Divider(height=50),
                ft.NavigationDrawerDestination(
                    label="DashBoard",
                    icon=ft.icons.DASHBOARD_OUTLINED,
                    selected_icon=ft.icons.DASHBOARD,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.APP_REGISTRATION_OUTLINED),
                    label="Cadastro de Clientes",
                    selected_icon=ft.icons.APP_REGISTRATION,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.MONETIZATION_ON_OUTLINED),
                    label="Orçamento",
                    selected_icon=ft.icons.MONETIZATION_ON,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.DOCUMENT_SCANNER_OUTLINED),
                    label="Protocolo",
                    selected_icon=ft.icons.DOCUMENT_SCANNER,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.ADD_BOX_OUTLINED),
                    label="Ordem de Serviço",
                    selected_icon=ft.icons.ADD_BOX,
                    
                ),
            ],
            
            on_change=lambda e: muda_pagina(e),
        )
    def muda_pagina(e):
        match e.control.selected_index:
            case 0:
                page.go('/login')
            case 1:
                print('index 1')
            case 2:
                print('index 2')
            case 3:
                print('index 3')
            case 4:
                print('index 4')
    
    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    btn = ft.IconButton(icon=ft.icons.MENU, on_click=show_drawer)
    page.add(btn)
                
    
if __name__ == "__main__":
    ft.app(target = pagina)