class CedulaVaciaError( Exception ):
    def __init__(self, cedula):
        """
        Para usar esta excepción, debe llamar al constructor indicando la cédula
        """ 
        super().__init__("No se puede utilizar un usuario sin cédula")

class AhorroPensionalAHoyError( Exception ):
    def __init__( self, ahorro_pensional_a_hoy:int ):
        """
        Para usar esta excepción, debe llamar al constructor indicando el ahorro pensional hoy usado
        """ 
        super().__init__( f"El ahorro pensional a hoy el cual es: {ahorro_pensional_a_hoy} debe ser mayor a 0" )

class EdadError( Exception ):
    def __init__( self, edad:int ):
        """
        Para usar esta excepción, debe llamar al constructor indicando la edad usada
        """
        super().__init__( f"Su edad la cual es: {edad} debe ser mayor a 0 y menor a 120" )

class SalarioActualError( Exception ):
    def __init__( self, salario_actual:int ):
        """
        Para usar esta excepción, debe llamar al constructor indicando el salario usado
        """
        super().__init__( f"Su salario el cual es: {salario_actual} debe ser mayor a 0" )

class TasaAdministracionError( Exception ):
    def __init__( self, tasa_administracion:float ):
        """
        Para usar esta excepción, debe llamar al constructor indicando la tasa de administracion usada
        """
        super().__init__( f"La tasa de administración la cual es: {tasa_administracion} debe ser mayor a 0 y menor a 3" )

class SemanasLaboradasError( Exception ):
    def __init__( self, semanas_laboradas:int ):
        """
        Para usar esta excepción, debe llamar al constructor indicando las semanas laboradas usadas
        """
        super().__init__( f"Las semanas laboradas las cuales son: {semanas_laboradas} deben ser mayores a 0" )

def VerificarCedula(cedula):
    if cedula == "":
        raise CedulaVaciaError(cedula)

def VerificarSemanasLaboradas(semanas_laboradas):
    if semanas_laboradas <0 :
        raise SemanasLaboradasError(semanas_laboradas)

def VerificarTasaAdministracion(tasa_administracion):
    if tasa_administracion<0 or tasa_administracion>3:
        raise TasaAdministracionError(tasa_administracion)

def VerificarSalarioActual(salario_actual):
    if salario_actual<0:
        raise SalarioActualError(salario_actual)

def VerificarEdad(edad):
    if edad<=0 or edad>120:
        raise EdadError(edad)

def VerificarAhorroPensional(ahorro_pensional_a_hoy):
    if ahorro_pensional_a_hoy<0:
        raise AhorroPensionalAHoyError(ahorro_pensional_a_hoy)

"""
Fórmula para calcular el Ahorro Pensional Esperado al momento de la jubilación
"""
def calcularAhorroPensionalEsperado(parametros):
    """
    Si el ahorro persional es igual o menor a 0
    """
    VerificarAhorroPensional(parametros.ahorro_pensional_a_hoy)
    """
    Si la edad es igual, menor a 0 o mayor a 120
    """
    VerificarEdad(parametros.edad)
    """
    Si el salario actual es menor a 0
    """
    VerificarSalarioActual(parametros.salario_actual)
    """
    Si la tasa de administracion es menor a 0 o mayor a 3
    """
    VerificarTasaAdministracion(parametros.tasa_administracion)
    """
    Si las semanas laboradas son menores a 0
    """
    VerificarSemanasLaboradas(parametros.semanas_laboradas)
    """
    Calcula el valor del ahorro esperado
    """
    años_para_jubilarse: int = parametros.edad_pension_total - parametros.edad # Número de años que le faltan al afiliado para jubilarse
    #Si el afiliado desea jubilarse en la edad legal
    if años_para_jubilarse < 0:
        años_totales_para_jubilarse: int = 0
    #Si el afiliado desea jubilarse a una edad diferente a la legal
    else:
        años_totales_para_jubilarse: int = años_para_jubilarse

    rentabilidad_promedio = parametros.rentabilidad_promedio/100
    tasa_administracion = parametros.tasa_administracion/100

    if parametros.salario_actual==0:
        return 0
    elif parametros.semanas_laboradas==0:
        return 0
    elif rentabilidad_promedio<=0:
        aportes: float = parametros.salario_actual # Total de aportes realizados por el afiliado
        gastos: float = aportes * tasa_administracion * años_totales_para_jubilarse # Total de gastos por administración del fondo
        AhorroPensionalEsperado: float = parametros.ahorro_pensional_a_hoy + aportes - gastos # Ahorro pensional total al momento de la jubilación
        return AhorroPensionalEsperado

    else:
        aportes: float = parametros.salario_actual # Total de aportes realizados por el afiliado
        rendimientos: float = aportes * ((1 + rentabilidad_promedio)**años_totales_para_jubilarse - 1) / rentabilidad_promedio # Total de rendimientos generados por los aportes
        gastos: float = (aportes + rendimientos) * tasa_administracion * años_totales_para_jubilarse # Total de gastos por administración del fondo
        AhorroPensionalEsperado: float = parametros.ahorro_pensional_a_hoy + aportes + rendimientos - gastos # Ahorro pensional total al momento de la jubilación
        return AhorroPensionalEsperado


    

"""
Calcular el número de meses que se espera recibir la pensión
Calcular el valor presente o esperado de la pensión mensual
"""
def calcPensionEsperada(AhorroPensionalEsperado:float, esperanza_vida:int, edad_pension_total:int, hereda:int, tasa_administracion:float):
    meses: int = (esperanza_vida - edad_pension_total) * 12 # Número de meses que se espera recibir la pensión
    #Si el afiliado no desea heredar su pension
    if hereda==0:
        PensionEsperadaTotal: float = AhorroPensionalEsperado / ((1 + tasa_administracion / 12)**meses) # Valor presente de la pensión mensual
        return PensionEsperadaTotal
    #Si el afiliado desea heredar su pension
    else:
       PensionEsperada: float = AhorroPensionalEsperado / ((1 + tasa_administracion / 12)**meses)
       PensionEsperadaMenos: float = (AhorroPensionalEsperado / ((1 + tasa_administracion / 12)**meses))*0.2 
       PensionEsperadaTotal: float = PensionEsperada - PensionEsperadaMenos # Valor presente de la pensión mensual
       return PensionEsperadaTotal