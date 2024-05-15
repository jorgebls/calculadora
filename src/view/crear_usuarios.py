import sys
sys.path.append("src")

from model.Usuario_Parametros import UsuarioParametrosPension
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros

try:
    print("Por favor ingrese los datos del usuario que desea insertar")

    usuario = UsuarioParametrosPension(
        cedula="", edad="", sexo="", estado_civil="", salario_actual="",
        semanas_laboradas="", ahorro_pensional_a_hoy="", rentabilidad_promedio="",
        tasa_administracion="", edad_pension_total="", hereda_pension=""
    )

    usuario.cedula = input("Cédula: ")
    if not usuario.cedula:
        raise ValueError("Debe ingresar la cédula del usuario.")
    
    usuario.edad = input("Edad: ")
    if not usuario.edad:
        raise ValueError("Debe ingresar la edad del usuario.")
    
    usuario.sexo = input("Sexo (M para masculino o F para femenino): ").upper()
    if usuario.sexo not in {'M', 'F'}:
        raise ValueError("Debe ingresar 'M' o 'F' para el sexo.")
    
    usuario.estado_civil = input("Estado civil (C para casado/a o S para soltero/a): ").upper()
    if usuario.estado_civil not in {'C', 'S'}:
        raise ValueError("Debe ingresar 'C' o 'S' para el estado civil.")
    
    usuario.salario_actual = input("Salario actual: ")
    if not usuario.salario_actual:
        raise ValueError("Debe ingresar el salario actual del usuario.")
    
    usuario.semanas_laboradas = input("Semanas laboradas: ")
    if not usuario.semanas_laboradas:
        raise ValueError("Debe ingresar las semanas laboradas del usuario.")
    
    usuario.ahorro_pensional_a_hoy = input("Ahorro pensional a hoy: ")
    if not usuario.ahorro_pensional_a_hoy:
        raise ValueError("Debe ingresar el ahorro pensional a la fecha de hoy del usuario.")
    
    usuario.rentabilidad_promedio = input("Rentabilidad promedio del fondo (debe ser mayor a 0 y menor a 3): ")
    if not usuario.rentabilidad_promedio:
        raise ValueError("Debe ingresar la rentabilidad promedio del fondo.")
    
    rentabilidad_promedio = float(usuario.rentabilidad_promedio)
    if rentabilidad_promedio <= 0 or rentabilidad_promedio >= 3:
        raise ValueError("La rentabilidad promedio debe ser mayor a 0 y menor a 3.")
    
    usuario.tasa_administracion = input("Tasa de administración del fondo (debe ser mayor a 0 y menor a 3): ")
    if not usuario.tasa_administracion:
        raise ValueError("Debe ingresar la tasa de administración del fondo.")
    
    tasa_administracion = float(usuario.tasa_administracion)
    if tasa_administracion <= 0 or tasa_administracion >= 3:
        raise ValueError("La tasa de administración del fondo debe ser mayor a 0 y menor a 3.")
    
    usuario.edad_pension_total = input("Edad pensión total: ")
    if not usuario.edad_pension_total:
        raise ValueError("Debe ingresar la edad de pensión total del usuario.")
    
    usuario.hereda_pension = str(input("Ingrese 'S' si desea heredar su pensión o 'N' si no: ")).upper()
    if usuario.hereda_pension not in {'S', 'N'}:
        raise ValueError("Debe ingresar 'S' o 'N' para la herencia de pensión.")

    ControladorUsuarios_Parametros.InsertarUsuario(usuario)

    print(f"El usuario con cédula {usuario.cedula} ha sido insertado correctamente!")

except ValueError as ve:
    print("Error:", ve)

except Exception as err:
    print("Error:", err)