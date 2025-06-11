import flet as ft
from pantalla1 import Contenidopantalla1


def main(page: ft.Page):
    #Cabecera
    page.appbar=ft.CupertinoAppBar(middle=ft.Text("Proyecto Final"),leading=ft.IconButton(ft.icons.MENU))
    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Adopciones",icon=ft.icons.PETS),
            ft.NavigationBarDestination(label="Voluntarios",icon=ft.icons.VOLUNTEER_ACTIVISM),
            ft.NavigationBarDestination(label="Perdidos",icon=ft.icons.SOS),
            ft.NavigationBarDestination(label="Perfil",icon=ft.icons.PERSON)
        ]
    )

    navegacionTabs=ft.Tabs(tabs=[
        ft.Tab(text="Opcion1",icon=ft.icons.MONITOR_WEIGHT,content=ft.Text("Contenido pantalla1")),
        ft.Tab(text="Opcion2",icon=ft.icons.MONITOR_WEIGHT,content=ft.Text("Contenido pantalla2")),
        ft.Tab(text="Opcion3",icon=ft.icons.MONITOR_WEIGHT),
        ft.Tab(text="Opcion4",icon=ft.icons.MONITOR_WEIGHT),
        ft.Tab(text="Opcion5",icon=ft.icons.MONITOR_WEIGHT)
    ])
    


    page.add(
        navegacionTabs
    )


ft.app(main)
