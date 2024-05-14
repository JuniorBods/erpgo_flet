import flet as ft
from components.skils import SkillRing, SkillProgressbar
class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src='.\\assets\\okimoveis.jpg',
                        border_radius=ft.border_radius.all(100),
                        width=130,
                    ),
                    ft.Text(value="OK IMÓVEIS",
                            theme_style=ft.TextThemeStyle.BODY_LARGE,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            ),
                    ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                
            ),
            padding=ft.padding.symmetric(vertical=20, horizontal=40),
            alignment=ft.alignment.center,
        )
        
class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand=True
    def build(self):
        location=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(value="Residencia",theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                            ft.Text(value="Brasil", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(value="Idade",theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                            ft.Text(value="32", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(value="Profissão",theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                            ft.Text(value="Programador Python", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                ]
            )
        
        languages=ft.Row(
            controls=[
                SkillRing(title="Protocolos", value=1),
                SkillRing(title="Financeiro", value=0.5), 
                SkillRing(title="Assinaturas", value=0.2),
            ]
        )
        skills=ft.Column(
            controls=[
                    SkillProgressbar(title="Protocolos", value=1),
                    SkillProgressbar(title="Financeiro", value=0.5), 
                    SkillProgressbar(title="Assinaturas", value=0.2),
                ]
            )
        
        protocolo=ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text("Protocolos", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text("Casas", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text("Financeiro", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text("Ordem de Serviço", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=12),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )
        
        cv=ft.TextButton(
            text="Download CV",
            style=ft.ButtonStyle(color=ft.colors.PRIMARY),
            icon=ft.icons.DOWNLOAD,
            icon_color=ft.colors.PRIMARY,
            url="www.bodsburguer.com.br"
            )
        
        
        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    location,
                    ft.Divider(height=10),
                    languages,
                    ft.Divider(height=10),
                    skills,
                    ft.Divider(height=10),
                    protocolo,
                    ft.Divider(height=10),
                    cv,
                ]
            )
        )


class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Icon(ft.icons.EDIT,color=ft.colors.BLACK),
                        tooltip="Edit",
                        url='www.google.com.br'
                    ),
                    ft.IconButton(
                        content=ft.Icon(ft.icons.SEARCH,color=ft.colors.BLACK),
                        tooltip="Edit",
                        url='www.facebook.com.br'
                    ),
                    ft.IconButton(
                        content=ft.Icon(ft.icons.PAGES,color=ft.colors.BLACK),
                        tooltip="Edit",
                        url='www.instagram.com.br'
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        
class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
        )







# def pagina(page: ft.Page):
#     page.drawer = ft.NavigationDrawer(
#             controls=[
#                 ft.Container(height=12),
#                 ft.NavigationDrawerDestination(
#                     label="DashBoard",
#                     icon=ft.icons.DASHBOARD_OUTLINED,
#                     selected_icon=ft.icons.DASHBOARD,
#                 ),
#                 ft.Divider(thickness=2),
#                 ft.NavigationDrawerDestination(
#                     icon_content=ft.Icon(ft.icons.APP_REGISTRATION_OUTLINED),
#                     label="Cadastro de Clientes",
#                     selected_icon=ft.icons.APP_REGISTRATION,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     icon_content=ft.Icon(ft.icons.MONETIZATION_ON_OUTLINED),
#                     label="Orçamento",
#                     selected_icon=ft.icons.MONETIZATION_ON,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     icon_content=ft.Icon(ft.icons.DOCUMENT_SCANNER_OUTLINED),
#                     label="Protocolo",
#                     selected_icon=ft.icons.DOCUMENT_SCANNER,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     icon_content=ft.Icon(ft.icons.ADD_BOX_OUTLINED),
#                     label="Ordem de Serviço",
#                     selected_icon=ft.icons.ADD_BOX,
                    
#                 ),
#             ],
#             on_change=lambda e: print(e.control.selected_index),
            
            
#         )
#     page.drawer.open = False

#     def show_drawer(e):
#         page.drawer.open = True
#         page.drawer.update()

#     btn = ft.IconButton(icon=ft.icons.MENU, on_click=show_drawer)
#     page.add(btn)
    
# if __name__ == "__main__":
#     ft.app(target = pagina)