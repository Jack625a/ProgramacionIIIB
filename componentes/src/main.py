import flet as ft #IMPORTACION DE FLET

#funcion para animacion
def animar():
    pass

numero=input("")

class dATOS:
    pass

def main(page: ft.Page): #FUNCION PRINCIPAL
    #LOS COMPONENTES QUE SE AGREGAN
    page.add(  
       ft.CupertinoFilledButton("Boton de Prueba"),
       ft.ElevatedButton("Boton 2"),
       ft.FilledButton("Boton 3"),
       ft.IconButton(icon=ft.icons.FACE),
       ft.Text(value="1rueba",size=30,weight=ft.FontWeight.BOLD),
       #LECTURA DE DATOS
       ft.TextField(label="Ingrese su nombre: "),
       ft.TextField(label="Ingrese su celular: ",icon=ft.Icons.PHONE_ANDROID, keyboard_type=ft.KeyboardType.PHONE),
       ft.TextField(label="Ingrese su contraseña: ", password=True, icon=ft.Icons.PASSWORD, can_reveal_password=True),
       ft.TextField(label="Ingrese su correo",align_label_with_hint=ft.alignment.center, label_style=ft.TextStyle(
           size=5,
           weight=ft.FontWeight.BOLD,
           
           
       )),
       #Casillas de verificacion
        ft.Checkbox(label="Verificar",check_color=ft.Colors.PINK_ACCENT_400),
        ft.CupertinoCheckbox(label="Verificar iOS"),
        #Radios de seleccion
        ft.Radio(label="Opcion 1",),
        ft.Radio(label="Opcion2"),
        ft.Radio(label="Opcion3"),
        ft.CupertinoRadio(label="Opcion4"),
        numero,

        dATOS()
        
    
    ) 
ft.app(main)
