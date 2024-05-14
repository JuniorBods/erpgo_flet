from flet import *
from pages.cadastro_clientes import cadastro


def main(page: Page):

    def views_change(e):
        match e.control.selected_index:
            case 0:
                page.go('/dashboard')
            case 1:
                page.go('/cadastro')
            case 2:
                page.go('/orcamento')
            case 3:
                page.go('/protocolo')
            case 4:
                page.go('/ordem_servico')

    menu = NavigationDrawer(
        controls=[
            Container(height=12),
            Image(src='.\\assets\\okimoveis.jpg',
                      border_radius=border_radius.all(500), height=150),
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

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                route="/dashboard",
                appbar=AppBar(title=Text("Dashboard", size=40)),
                drawer=menu,
                controls=[
                    Text("DashBoard", size=40),
                ],
            )
        )
        if page.route == "/cadastro":
            page.views.clear()
            page.views.append(
                View(
                    route="/cadastro",
                    appbar=AppBar(title=Text("cadastro", size=40)),
                    drawer=menu,
                    controls=[
                        cadastro()
                    ],
                    scroll="auto",
                )
            )
        if page.route == "/orcamento":
            page.views.clear()
            page.views.append(
                View(
                    route="/orcamento",
                    appbar=AppBar(title=Text("orcamento", size=40)),
                    drawer=menu,
                    controls=[Text("orcamento", size=40),
                              Text("orcamento", size=40),
                              ],
                )
            )
        if page.route == "/protocolo":
            page.views.clear()
            page.views.append(
                View(
                    route="/protocolo",
                    appbar=AppBar(title=Text("protocolo", size=40)),
                    drawer=menu,
                    controls=[Text("protocolo", size=40),
                              Text("protocolo", size=40),
                              ],
                )
            )
        if page.route == "/ordem_servico":
            page.views.clear()
            page.views.append(
                View(
                    route="/ordem_servico",
                    appbar=AppBar(title=Text("ordem_servico", size=40)),
                    drawer=menu,
                    controls=[Text("ordem_servico", size=40),
                              Text("ordem_servico", size=40),
                              ],
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    app(target=main)
