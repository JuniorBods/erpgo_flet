from flet import *
from views import views_change

def main(page: Page):
    page.drawer = NavigationDrawer(
            controls=[
                Container(height=12),
                Image(src='.\\assets\\okimoveis.jpg', border_radius=border_radius.all(500), height=150),
                Divider(height=50),
                NavigationDrawerDestination(
                    label="DashBoard",
                    icon=icons.DASHBOARD_OUTLINED,
                    selected_icon=icons.DASHBOARD,
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.APP_REGISTRATION_OUTLINED),
                    label="Cadastro de Clientes",
                    selected_icon=icons.APP_REGISTRATION,
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.MONETIZATION_ON_OUTLINED),
                    label="Orçamento",
                    selected_icon=icons.MONETIZATION_ON,
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.DOCUMENT_SCANNER_OUTLINED),
                    label="Protocolo",
                    selected_icon=icons.DOCUMENT_SCANNER,
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.ADD_BOX_OUTLINED),
                    label="Ordem de Serviço",
                    selected_icon=icons.ADD_BOX,
                    
                ),
            ],
            on_change=views_change,
        )
    page.drawer.open = False

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    btn = IconButton(icon=icons.MENU, on_click=show_drawer)
    page.add(btn)

    def route_change(route):
        page.views.clear()
        page.views.append(
           views_change(page)[page.route]
        )


    page.on_route_change = route_change



if __name__ == "__main__":
    app(target = main)