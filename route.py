import flet as ft

def main(page: ft.Page):    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(
                    title=ft.Text("Meu App"),
                    bgcolor=ft.colors.SURFACE_VARIANT,    
                ),
                controls=[
                    ft.ElevatedButton(
                        text="Ver Loja",
                        on_click= lambda _: page.go('/loja')
                    ),
                    ft.ListView(
                        ft.Text(
                            value=f"Item {i}",
                            size=30
                        )
                        for i in range(50)
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                auto_scroll=False
            )
        )
        
        if page.route == '/app':
            page.views.append(
                ft.View(
                    route="/app",
                    appbar=ft.AppBar(
                        title=ft.Text("App"),
                        bgcolor=ft.colors.SURFACE_VARIANT,    
                    ),
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para Pagina Inicial",
                            on_click= lambda _: page.go('/')
                        )
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
    ft.app(target = main, view=ft.WEB_BROWSER)