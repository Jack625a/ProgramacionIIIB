import flet as ft

#PARA TRAER CONTENIDO MODULAR
#DEBEMOS IMPORTAR 
from pantalla1 import pantalla1Contenido
from pantalla2 import pantalla2Contenido
from pantalla3 import pantalla3Contenido
from pantalla4 import pantalla4Contenido


def main(page: ft.Page):
    #variable para las secciones modulares
    secciones=ft.Tabs(
        selected_index=0,
        animation_duration=500,
        tabs=[
            ft.Tab(
                text="Pantalla 1",
                icon=ft.Icons.LAYERS,
                content=pantalla1Contenido()
            ),
            ft.Tab(
                text="Pantalla 2",
                icon=ft.Icons.REMOVE,
                content=pantalla2Contenido()
            ),
            ft.Tab(
                text="Pantalla 3",
                icon=ft.Icons.NEARBY_ERROR_SHARP,
                content=pantalla3Contenido()
            ),
            ft.Tab(
                text="Pantalla 4",
                icon=ft.Icons.TEXTURE,
                content=pantalla4Contenido()
            )
        ],expand=1
        
        )
    
    #Añadir el contenido a la pantalla principal
    page.add(
        secciones  
    )


ft.app(main)
