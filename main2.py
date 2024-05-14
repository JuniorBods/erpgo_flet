import flet as ft
from pages.login import login

def main(page:ft.Page):
    def muda_pagina(e):
        match e.control.selected_index:
            case 0:
                page.go('/app')
            case 1:
                print('index 1')
            case 2:
                print('index 2')
            case 3:
                print('index 3')
            case 4:
                print('index 4')
                
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text("Imobiliaria Ok Imóveis"),
                    bgcolor=ft.colors.SURFACE_VARIANT,    
                ),

                scroll=ft.ScrollMode.AUTO,
                auto_scroll=False,
                drawer = ft.NavigationDrawer(
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
            )
        )
        
        if page.route == '/app':
            page.views.append(
                ft.View(
                    route="/app",
                    appbar=ft.AppBar(
                        title=ft.Text("login"),
                        bgcolor=ft.colors.SURFACE_VARIANT,    
                    ),
                    controls=[
                        login()
                    ]
                )
            )
        elif page.route == '/loja':
            page.views.append(
                ft.View(
                    route="/loja",
                    appbar=ft.AppBar(
                        title=ft.Text("Loja"),
                        bgcolor=ft.colors.SURFACE_VARIANT,    
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para Pagina Inicial",
                            on_click= lambda _: page.go('/')
                        ),
                        ft.ElevatedButton(
                            text="Ir para App",
                            on_click= lambda _: page.go('/app')
                        )
                    ]
                )
            )
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
                    
            
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target = main, assets_dir="assets")