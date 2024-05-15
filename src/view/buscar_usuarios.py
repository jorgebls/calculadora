import sys
sys.path.append("src")

from model.Usuario_Parametros import UsuarioParametrosPension
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros

try:
    cedula = input("Ingrese la cédula del usuario que desea buscar: ")
    usuario_buscado = ControladorUsuarios_Parametros.BuscarUsuarioPorCedula( cedula )
    print(  f"""El usuario con cédula {cedula} ha sido encontrado, salario: {usuario_buscado.salario_actual}, semanas laboradas: {usuario_buscado.semanas_laboradas}, ahorro pensional a hoy: {usuario_buscado.ahorro_pensional_a_hoy}""" )
except Exception as err:
    print("Error : " )
    print( str( err ) )