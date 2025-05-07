import flet as ft


def main(page: ft.Page):
    page.title="Navegacion"
    #APP BAR CABECERAS
    page.appbar=ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.MENU),
        middle=ft.Text("Navegaciones"),
        bgcolor=ft.Colors.RED_400
    )

    #NAVEGACION
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Inicio",icon=ft.icons.HOME),
            ft.NavigationBarDestination(label="Ajustes",icon=ft.icons.SETTINGS),
            ft.NavigationBarDestination(label="Perfil",icon=ft.icons.PERSON),
            ft.NavigationBarDestination(label="Servicios", icon=ft.icons.ROOM_SERVICE)
        ],bgcolor=ft.colors.RED_800, indicator_color=ft.colors.WHITE
    )

   
    page.add(
        
    )


ft.app(main)
