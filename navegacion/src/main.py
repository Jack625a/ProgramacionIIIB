import flet as ft
#MODIFICACIONES

def main(page: ft.Page):



    page.title="Navegacion"
    #APP BAR CABECERAS
    page.appbar=ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.MENU),
        middle=ft.Text("Navegaciones"),
        bgcolor=ft.Colors.RED_400
    )

    #NAVEGACION
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Inicio",icon=ft.Icons.HOME),
            ft.NavigationBarDestination(label="Ajustes",icon=ft.Icons.SETTINGS),
            ft.NavigationBarDestination(label="Perfil",icon=ft.Icons.PERSON),
            ft.NavigationBarDestination(label="Servicios", icon=ft.Icons.ROOM_SERVICE)
        ],bgcolor=ft.Colors.RED_800, indicator_color=ft.Colors.WHITE
    )


    def cerrar(e):
        page.close(navegacionLateral)

    
    #NAVEGACION LATERAL 
    navegacionLateral=ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                label="Opcion1",
                icon=ft.Icon(ft.Icons.HOME_MAX)
            ),
            ft.Divider(height=1),
            ft.NavigationDrawerDestination(
                label="Opcion2",
                icon=ft.Icon(ft.Icons.AC_UNIT_OUTLINED) 
            )
        ],
        position=ft.NavigationDrawerPosition.END,
        on_change=cerrar,
    )

    #page.open(navegacionLateral)
   
    page.add(
       
        ft.CupertinoButton(text="PRUEBA",on_click=lambda e: page.open(navegacionLateral))
    )


ft.app(main)
