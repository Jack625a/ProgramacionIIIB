import flet as ft #Importacion del framework

def obtencionDatos():
    pass

#Funcion principal
def main(page: ft.Page): #ft.Page: Crear una ventana 

    page.title="Prueba"
    page.appbar=ft.CupertinoAppBar(
        middle=ft.Text("Titulo Aplicacion", size=20,color=ft.Colors.GREEN_900)
    )
    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                label="Opcion 1",
                icon=ft.Icons.READ_MORE_SHARP
            ),
            ft.NavigationBarDestination(
                label="Opcion 2",
                icon=ft.Icons.FACEBOOK
            ),
            ft.NavigationBarDestination(
                label="Opcion 3",
                icon=ft.Icons.ADD
            )
        ]
    )

    imagen=ft.Image(
        src=f"https://pythonlife.in/images/pythonlogo.png", 
        width=150, 
        height=150
    )

    #Componentes separados
    menu=ft.Tabs(
        tabs=[
            ft.Tab(text="Opcion 1",icon=ft.Icons.PRINT,content=ft.Text("Pantalla opcion 1")),
            ft.Tab(text="Opcion 2",icon=ft.Icons.DELETE),
            ft.Tab(text="Opcion 3",icon=ft.Icons.APPS),
            ft.Tab(text="Opcion 4",icon=ft.Icons.FACEBOOK)
        ]
    )


    page.add(  #Metodo add nos permite agregar componentes a la interfaz
      #Componentes basicos
      menu,
      ft.Text(value="Componentes"),
      ft.CupertinoFilledButton("Boton1"),
      imagen,


    )


ft.app(main) 



lista=[1,3,4,6]