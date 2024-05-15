import sys
sys.path.append("src")

import Logic.CalculatorLogic as CalculatorLogic
from Logic.CalculatorLogic import *
from Logic.Clase_Parametros import *

try:
    # Obtener los datos de entrada  
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Debe ingresar un valor numérico para la edad.")
    sys.exit(1)

try:
    sexo = str(input("Ingrese su sexo (M para masculino o F para femenino): ")).upper()
    if sexo not in ['M', 'F']:
        raise ValueError("Debe ingresar 'M' para masculino o 'F' para femenino.")
except ValueError as e:
    print(e)
    sys.exit(1)

try:
    estado_civil = str(input("Ingrese su estado civil (C para casad@ o S para solter@): ")).upper()
    if estado_civil not in ['C', 'S']:
        raise ValueError("Debe ingresar 'C' para casad@ o 'S' para solter@.")
except ValueError as e:
    print(e)
    sys.exit(1)

try:
    salario_actual = int(input("Ingrese su salario actual: "))
except ValueError:
    print("Debe ingresar un valor numérico para el salario actual.")
    sys.exit(1)

try:
    semanas_laboradas = int(input("Ingrese sus semanas laboradas a hoy: "))
except ValueError:
    print("Debe ingresar un valor numérico para las semanas laboradas.")
    sys.exit(1)

try:
    ahorro_pensional_a_hoy = int(input("Ingrese su ahorro pensional a hoy: "))
except ValueError:
    print("Debe ingresar un valor numérico para el ahorro pensional a hoy.")
    sys.exit(1)

try:
    rentabilidad_promedio = float(input("Ingrese la rentabilidad promedio del fondo (debe ser mayor a 0 y menor a 3): "))
    if not 0 < rentabilidad_promedio < 3:
        raise ValueError("La rentabilidad promedio debe ser mayor a 0 y menor a 3.")
except ValueError as e:
    print(e)
    sys.exit(1)

try:
    tasa_administracion = float(input("Ingrese la tasa de administracion del fondo (debe ser mayor a 0 y menor a 3): "))
    if not 0 < tasa_administracion < 3:
        raise ValueError("La tasa de administración debe ser mayor a 0 y menor a 3.")
except ValueError as e:
    print(e)
    sys.exit(1)

try:
    edad_pension = str(input("Ingrese 'S' si desea pensionarse a la edad legal o 'N' si no: ")).upper()
    if edad_pension not in ['S', 'N']:
        raise ValueError("Debe ingresar 'S' si desea pensionarse a la edad legal o 'N' si no.")
except ValueError as e:
    print(e)
    sys.exit(1)

if edad_pension=="N":
    try:
        edad_pension_total=int(input("Ingrese la edad a la que desea pensionarse: "))
    except ValueError:
        print("Debe ingresar un valor numérico para la edad a la que desea pensionarse.")
        sys.exit(1)
else:
    edad_pension_total=65

parametros = ParametrosPension()
parametros.edad = edad
parametros.salario_actual = salario_actual
parametros.semanas_laboradas = semanas_laboradas
parametros.rentabilidad_promedio = rentabilidad_promedio
parametros.ahorro_pensional_a_hoy = ahorro_pensional_a_hoy
parametros.tasa_administracion = tasa_administracion
parametros.edad_pension_total = edad_pension_total

try:
    hereda_pension = str(input("Ingrese 'S' si desea heredar su pensión o 'N' si no: ")).upper()
    if hereda_pension=="S" and estado_civil=="C":
        hereda = 1
    if hereda_pension=="S" and estado_civil == "S":
        hereda: int = 0
    elif hereda_pension=="N":
        hereda = 0
except ValueError:
    print("Debe ingresar 'S' si desea heredar su pensión o 'N' si no.")
    sys.exit(1)

try:   
    AhorroPensionalEsperado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)

    print(f"El ahorro pensional esperado es: {AhorroPensionalEsperado}")

    if AhorroPensionalEsperado:
        if sexo == "M":
            esperanza_vida = 80  # Esperanza de vida para hombres en Colombia
        elif sexo == "F":
            esperanza_vida = 85  # Esperanza de vida para mujeres en Colombia

        PensionEsperadaTotal = (CalculatorLogic.calcPensionEsperada(AhorroPensionalEsperado, esperanza_vida, edad_pension_total, hereda, tasa_administracion))

        print(f"La pensión esperada es: {PensionEsperadaTotal}")

except ValueError as the_error:
    print(f"El valor ingresado es incorrecto: {the_error}")
except Exception as the_exception:
    # Maneja las excepciones controladas
    print(f"No puede continuar, ocurrió un problema: {the_exception}")
