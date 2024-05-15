import sys
sys.path.append("src")

from model.Usuario_Parametros import UsuarioParametrosPension
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros

try:
    cedula = input("Ingrese la cédula del usuario que desea borrar: ")
    ControladorUsuarios_Parametros.EliminarUsuarioPorCedula( cedula )
    print(  f"El usuario con cédula {cedula} ha sido eliminado correctamente" )
except Exception as err:
    print("Error : " )
    print( str( err ) )