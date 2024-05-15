import sys
sys.path.append("src")

from model.Usuario_Parametros import UsuarioParametrosPension
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros

try:
    cedula = input("Ingrese la cédula del usuario que desea actualizar: ")
    salario_nuevo = input("Ingrese el nuevo salario: ")
    ControladorUsuarios_Parametros.ActualizarUsuarioPorCedula(cedula, salario_nuevo)
    print(f"El nuevo salario del usuario con cédula {cedula} es: {salario_nuevo}")
except Exception as err:
    print("Error : " )
    print( str( err ) )