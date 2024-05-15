import sys
sys.path.append("src")

import Logic.CalculatorLogic as CalculatorLogic
from Logic.CalculatorLogic import *
from Logic.Clase_Parametros import *
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros

try:
    #Obtener los datos de entrada
    cedula = input("Ingrese la cédula del usuario que desea buscar: ")
    usuario_buscado = ControladorUsuarios_Parametros.BuscarUsuarioPorCedula( cedula )
    edad=usuario_buscado.edad
    salario_actual=usuario_buscado.salario_actual
    semanas_laboradas=usuario_buscado.semanas_laboradas
    rentabilidad_promedio=usuario_buscado.rentabilidad_promedio
    ahorro_pensional_a_hoy=usuario_buscado.ahorro_pensional_a_hoy
    tasa_administracion=usuario_buscado.tasa_administracion
    hereda_pension=usuario_buscado.hereda_pension
    edad_pension_total = usuario_buscado.edad_pension_total
    sexo = usuario_buscado.sexo
    estado_civil = usuario_buscado.estado_civil

    parametros = ParametrosPension()
    parametros.edad = edad
    parametros.salario_actual = salario_actual
    parametros.semanas_laboradas = semanas_laboradas
    parametros.rentabilidad_promedio = rentabilidad_promedio
    parametros.ahorro_pensional_a_hoy = ahorro_pensional_a_hoy
    parametros.tasa_administracion = tasa_administracion
    parametros.edad_pension_total = edad_pension_total
    
    if hereda_pension=="S" and estado_civil=="C":
        hereda : int =1
    if hereda_pension=="S" and estado_civil == "S":
        hereda: int = 0
    elif hereda_pension=="N":
        hereda: int =0
        
    AhorroPensionalEsperado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)

    print(f"El ahorro pensional esperado es: {AhorroPensionalEsperado}")

    if AhorroPensionalEsperado:
        if sexo == "M":
            esperanza_vida: int = 80 # Esperanza de vida para hombres en Colombia
        elif sexo == "F":
            esperanza_vida: int = 85 # Esperanza de vida para mujeres en Colombia

        PensionEsperadaTotal = (CalculatorLogic.calcPensionEsperada(AhorroPensionalEsperado, esperanza_vida, edad_pension_total, hereda, tasa_administracion))

        print(f"La pensión esperada es: {PensionEsperadaTotal}")

except ValueError as the_error:
    print(f"El valor ingresado es incorrecto : {the_error}")
except Exception as err:
    #Maneja las excepciones controladas
    print("No puede continuar, ocurrió un error : " )
    print(str(err))