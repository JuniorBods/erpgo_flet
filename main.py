import flet as ft

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.RED
        self.page.title = "Meu App"
        self.main()

    def main(self):
        layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                self
            ]
        )

if __name__ == "__main__":
    ft.app(target=App)
