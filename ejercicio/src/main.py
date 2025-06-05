import flet as ft #Importacion del framework
#PASO 1. IMPORTAR LAS LIBRERIAS
import requests #peticiones o solicitudes a un servidor

#PASO 2. CONFIGURAR LAS VARIABLES DE CONEXION
TOKENAIRTABLE=''
idBasedatos= ''
nombreTabla='Estudiante'

#PASO 3. CONFIGURAR LA URL DE CONEXION ENDPOINT
url=f"https://api.airtable.com/v0/{idBasedatos}/{nombreTabla}"
#PASO4. CONFIGURAR LA AUTENTIFICACION
HEADERS={
    "Authorization": f"Bearer {TOKENAIRTABLE}"
}

#PASO 5. CREAR LA FUNCION PARA OBTENER LOS DATOS
def obtencionDatos():
    try:
        respuesta=requests.get(url,headers=HEADERS)
        #VERIFICAR SI SE CONECTA CON EL SERVIDOR
        if respuesta.status_code==200:
            registros=respuesta.json().get("records",[])
            return registros
        else:
            print("Error al obtener los datos...")
    except Exception as e:
        print("Error en las credenciales ",e)
        return []

#Funcion principal
def main(page: ft.Page): #ft.Page: Crear una ventana 
    def mostrarDatos():
        datos=obtencionDatos()
        print(datos)
        textoEstudiante=("Lista de Estudiante: ")
        for dato in datos:
            registros=dato.get("Nombre","No tiene nombre"),
            carrera=dato.get("Carrera","Sin carrera"),
            celular=dato.get("Celular","Sin celular"),
            edad=dato.get("Edad","0"),
        
        textoEstudiante+=f"{registros} - {carrera} - Edad: {edad} - Celular: {celular}"
        page.update()
    
   
    page.title="Prueba"
    page.appbar=ft.CupertinoAppBar(
        middle=ft.Text("Titulo Aplicacion", size=20,color=ft.Colors.GREEN_900)
    )
    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                label="Opcion 1",
                icon=ft.Icons.READ_MORE_SHARP,
                
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
            ft.Tab(text="Opcion 1",icon=ft.Icons.PRINT,content= ft.CupertinoFilledButton("Mostrar Estudiante",on_click=mostrarDatos)),
            ft.Tab(text="Opcion 2",icon=ft.Icons.DELETE),
            ft.Tab(text="Opcion 3",icon=ft.Icons.APPS),
            ft.Tab(text="Opcion 4",icon=ft.Icons.FACEBOOK)
        ]
    )
    mostrarDatos()

    page.add(  #Metodo add nos permite agregar componentes a la interfaz
      #Componentes basicos
        ft.CupertinoFilledButton("Mostrar Estudiante",on_click=mostrarDatos)
       


    )


ft.app(main) 

