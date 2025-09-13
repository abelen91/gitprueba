#creo un diccionario que contiene usuarios y contraseñas (clave-valor) y en donde el prog me va a permitir agregar nuevos registros
usuarios = {
    "usuarionuevo":"2345",
    "ceoBD":"nuevo659",
    "anab":"madryn123"
            }
#Creo la funcion registrar_nuevo que va a permitir ingresar datos nuevos en mi diccionario "usuarios"
def registrar_nuevo():
    print("Registrarse por favor:")
    usuarionuevo = input("Ingrese su nombre de usuario: ")
    while usuarionuevo in usuarios:
        print("Usuario existente, ingrese otro nombre de usuario: ")
        usuarionuevo = input("Ingrese su nombre de usuario: ")

    contraseñanueva = input("Ingrese su contraseña: ")
    usuarios[usuarionuevo]= contraseñanueva
    print("Registrado con éxito.")

#defino mi login de ingreso de datos (usuario y contraseña)

def milogin():
     while True:
         nombre_de_usuario = input("Ingrese su nombre de usuario: ")
         contraseña = input("Ingrese su contraseña: ")

         if nombre_de_usuario in usuarios and contraseña == usuarios[nombre_de_usuario]:
              print("Bienvenidos a mi login: ")
              break
         elif nombre_de_usuario not in usuarios:
              print("Usuario inexistente")
              opcion = input("¿Quiere registrarse? (si/no): ").lower()
              if opcion == "si":
                  registrar_nuevo()
              else:
                  print("Intente nuevamente...")
         else:
               print("Contraseña incorrecta, intente nuevamente")

milogin()


