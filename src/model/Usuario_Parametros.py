class UsuarioParametrosPension:
    def __init__(self, cedula, edad, sexo, estado_civil, salario_actual, semanas_laboradas, ahorro_pensional_a_hoy, rentabilidad_promedio, tasa_administracion, edad_pension_total, hereda_pension):
        self.cedula = cedula
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.salario_actual= salario_actual
        self.semanas_laboradas= semanas_laboradas
        self.ahorro_pensional_a_hoy = ahorro_pensional_a_hoy
        self.rentabilidad_promedio = rentabilidad_promedio
        self.tasa_administracion = tasa_administracion
        self.edad_pension_total = edad_pension_total
        self.hereda_pension = hereda_pension
        

    def esIgual(self, comparar_con):
        assert(self.cedula == comparar_con.cedula)
        assert(self.edad == comparar_con.edad)
        assert(self.sexo == comparar_con.sexo)
        assert(self.estado_civil == comparar_con.estado_civil)
        assert(self.salario_actual == comparar_con.salario_actual)
        assert(self.semanas_laboradas == comparar_con.semanas_laboradas)
        assert(self.ahorro_pensional_a_hoy == comparar_con.ahorro_pensional_a_hoy)
        assert(self.rentabilidad_promedio == comparar_con.rentabilidad_promedio)
        assert(self.tasa_administracion == comparar_con.tasa_administracion)
        assert(self.edad_pension_total == comparar_con.edad_pension_total)
        assert(self.hereda_pension == comparar_con.hereda_pension)