import sys
sys.path.append("src")

from model.Usuario_Parametros import UsuarioParametrosPension
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros


def main_menu():
    while True:
        print("\n--- Control de Usuarios de Pensión ---")
        print("1. Crear tabla Usuarios_Pension")
        print("2. Eliminar tabla Usuarios_Pension")
        print("3. Insertar un nuevo usuario")
        print("4. Buscar usuario por cédula")
        print("5. Actualizar salario de un usuario")
        print("6. Eliminar usuario por cédula")
        print("7. Salir")
        option = input("Seleccione una opción: ")

        if option == '1':
            ControladorUsuarios_Parametros.CrearTabla()
            print("Tabla creada exitosamente.")
        elif option == '2':
            ControladorUsuarios_Parametros.EliminarTabla()
            print("Tabla eliminada exitosamente.")
        elif option == '3':
            usuario = obtener_datos_usuario()
            ControladorUsuarios_Parametros.InsertarUsuario(usuario)
            print("Usuario insertado exitosamente.")
        elif option == '4':
            cedula = input("Ingrese la cédula del usuario a buscar: ")
            usuario = ControladorUsuarios_Parametros.BuscarUsuarioPorCedula(cedula)
            print("Usuario encontrado:", usuario)
        elif option == '5':
            cedula = input("Ingrese la cédula del usuario a actualizar: ")
            salario_nuevo = input("Ingrese el nuevo salario: ")
            ControladorUsuarios_Parametros.ActualizarUsuarioPorCedula(cedula, salario_nuevo)
            print("Salario actualizado exitosamente.")
        elif option == '6':
            cedula = input("Ingrese la cédula del usuario a eliminar: ")
            ControladorUsuarios_Parametros.EliminarUsuarioPorCedula(cedula)
            print("Usuario eliminado exitosamente.")
        elif option == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")

def obtener_datos_usuario():
    cedula = input("Ingrese la cédula: ")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo: ")
    estado_civil = input("Ingrese el estado civil: ")
    salario_actual = int(input("Ingrese el salario actual: "))
    semanas_laboradas = int(input("Ingrese las semanas laboradas: "))
    ahorro_pensional_a_hoy = int(input("Ingrese el ahorro pensional hasta hoy: "))
    rentabilidad_promedio = float(input("Ingrese la rentabilidad promedio: "))
    tasa_administracion = float(input("Ingrese la tasa de administración: "))
    edad_pension_total = int(input("Ingrese la edad total para la pensión: "))
    hereda_pension = input("¿Hereda pensión? (sí/no): ")
    return UsuarioParametrosPension(cedula, edad, sexo, estado_civil, salario_actual, semanas_laboradas, ahorro_pensional_a_hoy, rentabilidad_promedio, tasa_administracion, edad_pension_total, hereda_pension)

if __name__ == '__main__':
    main_menu()
