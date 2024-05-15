from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

import Logic.CalculatorLogic as CalculatorLogic
from Logic.CalculatorLogic import *
from Logic.Clase_Parametros import *

class CalculatorApp(App):
    def build(self):
        self.contenedor = BoxLayout(orientation="vertical")

        fila = BoxLayout( orientation="horizontal")
        self.contenedor.add_widget(fila)    

        fila.add_widget( Label() )
        fila.add_widget( Label(text="Calculadora pensional", font_size=50) )
        fila.add_widget( Label() )
                
        fila1 = BoxLayout( orientation="horizontal")
        self.contenedor.add_widget(fila1)

        fila1.add_widget( Label(text="Ingrese su edad") )
        self.edad = TextInput(font_size=30 )
        fila1.add_widget(self.edad)

        fila1.add_widget( Label(text="Ingrese su sexo (M para \n masculino o F para femenino)") )
        self.sexo = TextInput(font_size=30 )
        fila1.add_widget(self.sexo)

        fila1.add_widget( Label(text="Ingrese su estado civil \n (C para casad@ o S para solter@)") )
        self.estado_civil = TextInput(font_size=30 )
        fila1.add_widget(self.estado_civil)

        fila2 = BoxLayout( orientation="horizontal")
        self.contenedor.add_widget(fila2)

        fila2.add_widget( Label(text="Ingrese su salario actual") )
        self.salario_actual = TextInput(font_size=30 )
        fila2.add_widget(self.salario_actual)

        fila2.add_widget( Label(text="Ingrese sus semanas laboradas \n a hoy") )
        self.semanas_laboradas = TextInput(font_size=30 )
        fila2.add_widget(self.semanas_laboradas)

        fila2.add_widget( Label(text="Ingrese su ahorro pensional a hoy") )
        self.ahorro_pensional_a_hoy = TextInput(font_size=30 )
        fila2.add_widget(self.ahorro_pensional_a_hoy)

        fila3 = BoxLayout( orientation="horizontal")
        self.contenedor.add_widget(fila3)

        fila3.add_widget( Label(text="Ingrese la rentabilidad promedio \n del fondo (debe ser mayor a 0 y menor a 3): ", font_size = 10) )
        self.rentabilidad_promedio = TextInput(font_size=30 )
        fila3.add_widget(self.rentabilidad_promedio)

        fila3.add_widget( Label(text="Ingrese la tasa de administracion \n del fondo (debe ser mayor a 0 y menor a 3): ", font_size = 10) )
        self.tasa_administracion = TextInput(font_size=30 )
        fila3.add_widget(self.tasa_administracion)

        fila3.add_widget( Label(text="Ingrese 'S' si desea pensionarse \n a la edad legal o 'N' si no") )
        self.edad_pension = TextInput(font_size=30 )
        fila3.add_widget(self.edad_pension)

        fila4 = BoxLayout( orientation="horizontal")
        self.contenedor.add_widget(fila4)

        fila4.add_widget( Label(text="Ingrese 'S' si desea heredar \n su pension o 'N' si no") )
        self.hereda_pension = TextInput(font_size=30 )
        fila4.add_widget(self.hereda_pension)

        self.button_calcular_ahorro_pensional = Button(text="Calcular \n ahorro \n pensional", font_size="40")
        self.button_calcular_ahorro_pensional.bind(on_press=self.calcular_ahorro_pensional)
        fila4.add_widget(self.button_calcular_ahorro_pensional)

        self.resultado_ahorro_pensional_esperado = (Label(text = "", font_size=25))
        fila4.add_widget(self.resultado_ahorro_pensional_esperado)

        self.button_calcular_pension_esperada = Button(text="Calcular \n pensión \n esperada", font_size="40")
        self.button_calcular_pension_esperada.bind(on_press=self.calcular_pension_esperada)
        fila4.add_widget(self.button_calcular_pension_esperada)

        self.result_pension_esperada = (Label (text = "", font_size=25))
        fila4.add_widget(self.result_pension_esperada)

        return self.contenedor

    def calcular_ahorro_pensional(self, sender):
        self.validar()
        try:
            edad=int(self.edad.text)
            salario_actual=int(self.salario_actual.text)
            semanas_laboradas=int(self.semanas_laboradas.text)
            ahorro_pensional_a_hoy=int(self.ahorro_pensional_a_hoy.text)
            rentabilidad_promedio=float(self.rentabilidad_promedio.text)
            tasa_administracion=float(self.tasa_administracion.text)
            edad_pension= (self.edad_pension.text).upper()
            if edad_pension=="N":
                edad_pension_total=70
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
            result = calcularAhorroPensionalEsperado(parametros)
            self.resultado_ahorro_pensional_esperado.text= str (round(result,2))
        except Exception as err:
            self.resultado_ahorro_pensional_esperado.text = str ( err )
        
    def calcular_pension_esperada(self,sender):
        self.validar()
        try:
            AhorroPensionalEsperado = float (self.resultado_ahorro_pensional_esperado.text)
            if self.sexo.text.upper() == "M":
                esperanza_vida: int = 80 # Esperanza de vida para hombres en Colombia
            elif self.sexo.text.upper() == "F":
                esperanza_vida: int = 85 # Esperanza de vida para mujeres en Colombia

            esperanza_vida= int(esperanza_vida)
            edad_pension = str(self.edad_pension.text).upper()
            
            if edad_pension=="N":
                edad_pension_total= 70
        
            else:
                edad_pension_total=65
            edad_pension_total = edad_pension_total
            if self.hereda_pension.text.upper()=="S" and self.estado_civil.text.upper()=="C":
                hereda : int =1
            elif self.hereda_pension.text.upper()=="N" or self.estado_civil.text.upper()== "S":
                hereda: int =0
            hereda=hereda
            tasa_administracion = int (self.tasa_administracion.text)
            result = calcPensionEsperada( AhorroPensionalEsperado, esperanza_vida, edad_pension_total, hereda, tasa_administracion )
            self.result_pension_esperada.text= str (round(result,2))
        except Exception as err:
            self.result_pension_esperada.text = str ( err )

    def validar(self):
        if not self.edad.text.isnumeric():
            self.edad.text=str("Debes ingresar tu edad")
        if not self.sexo.text.isalpha():
            self.sexo.text=str("Debes ingresar tu género")
        if not self.estado_civil.text.isalpha():
            self.estado_civil.text=str("Debes ingresar tu estado civil")
        if not self.salario_actual.text.isnumeric():
            self.salario_actual.text=str("Debes ingresar tu salario actual")
        if not self.semanas_laboradas.text.isnumeric():
            self.semanas_laboradas.text=str("Debes ingresar tus semasnas laboradas a hoy")
        if not self.ahorro_pensional_a_hoy.text.isnumeric():
            self.ahorro_pensional_a_hoy.text=str("Debes ingresar tu ahorro pensional a hoy")
        if not self.rentabilidad_promedio.text.isnumeric():
            self.rentabilidad_promedio.text=str("Debes ingresar la rentabilidad promedio del fondo (debe ser mayor a 0 y menor a 3)")
        if not self.tasa_administracion.text.isnumeric():
            self.tasa_administracion.text=str("Debes ingresar la tasa de administración del fondo (debe ser mayor a 0 y menor a 3)")
        if not self.edad_pension.text.isalpha():
            self.edad_pension.text=str("Debes ingresar si desea pensionarse a la edad legal")
        if not self.hereda_pension.text.isalpha():
            self.hereda_pension.text=str("Debes ingresar si desea heredar su pensión")

        # Siempre se retorna el widget que contiene a todos los demás

if __name__ == "__main__":
    CalculatorApp().run()