import unittest

import sys
sys.path.append("src")

from model.Usuario_Parametros import UsuarioParametrosPension
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros
import Logic.CalculatorLogic as CalculatorLogic
from Logic.CalculatorLogic import *

import psycopg2

class ControllerTest(unittest.TestCase):

    # Test Fixture
    def setUpClass():
        # Llamar a la clase Controlador para que cree la tabla
        ControladorUsuarios_Parametros.EliminarTabla()
        ControladorUsuarios_Parametros.CrearTabla()

    def testInsertAndSelect_First( self ):
        # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="1027803999", edad="70", sexo="M", estado_civil="S", salario_actual="20000000", semanas_laboradas="2000",
        ahorro_pensional_a_hoy="10000000", rentabilidad_promedio="2", tasa_administracion="1", edad_pension_total="65", hereda_pension="N" )
        ControladorUsuarios_Parametros.InsertarUsuario( usuario_prueba )
        cedula_usuario_prueba = usuario_prueba.cedula

        # Verificar si la tabla quedo creada correctamente
        usuario_buscado = ControladorUsuarios_Parametros.BuscarUsuarioPorCedula( cedula_usuario_prueba )

        # Comparar si el usuario que se insertó, contiene la misma información, que el retornado
        self.assertTrue(usuario_prueba, usuario_buscado)

    def testInsertAndSelect_CedulaVacia( self ):
        # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="", edad="89", sexo="F", estado_civil="S", salario_actual="30000000", semanas_laboradas="1500",
        ahorro_pensional_a_hoy="300000000", rentabilidad_promedio="1", tasa_administracion="1", edad_pension_total="65", hereda_pension="N" )

        self.assertRaises(CalculatorLogic.CedulaVaciaError, ControladorUsuarios_Parametros.InsertarUsuario, usuario_prueba)

    def testPrimaryKey_First(self):
        # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="1027801222", edad="99", sexo="M", estado_civil="S", salario_actual="30000000", semanas_laboradas="1000",
        ahorro_pensional_a_hoy="20000000", rentabilidad_promedio="2", tasa_administracion="2", edad_pension_total="65", hereda_pension="N" )
        ControladorUsuarios_Parametros.InsertarUsuario( usuario_prueba )

        # Insertar un Usuario en la tabla
        usuario_prueba_comparacion  = UsuarioParametrosPension( cedula="1027801222", edad="95", sexo="F", estado_civil="S", salario_actual="2000000", semanas_laboradas="1300",
        ahorro_pensional_a_hoy="19000000", rentabilidad_promedio="1", tasa_administracion="1", edad_pension_total="65", hereda_pension="N" )
        
        self.assertRaises( Exception, ControladorUsuarios_Parametros.InsertarUsuario, usuario_prueba_comparacion )

    def testPrimaryKey_Second(self):
    # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="1027800000", edad="90", sexo="F", estado_civil="S", salario_actual="43000000", semanas_laboradas="900",
        ahorro_pensional_a_hoy="100000000", rentabilidad_promedio="1", tasa_administracion="2", edad_pension_total="65", hereda_pension="N" )
        ControladorUsuarios_Parametros.InsertarUsuario( usuario_prueba )

        # Insertar un Usuario en la tabla
        usuario_prueba_comparacion  = UsuarioParametrosPension( cedula="1027800000", edad="66", sexo="M", estado_civil="S", salario_actual="22000000", semanas_laboradas="1100",
        ahorro_pensional_a_hoy="23000000", rentabilidad_promedio="2", tasa_administracion="1", edad_pension_total="65", hereda_pension="N" )
        
        self.assertRaises( Exception, ControladorUsuarios_Parametros.InsertarUsuario, usuario_prueba_comparacion )

    def testSelect_error_cedula(self):
        # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="", edad="83", sexo="F", estado_civil="S", salario_actual="6000000", semanas_laboradas="1140",
        ahorro_pensional_a_hoy="16400000", rentabilidad_promedio="1", tasa_administracion="2", edad_pension_total="65", hereda_pension="N" )
        #Cedula del usuario que vamos a buscar
        cedula_usuario_prueba_seleccionar = usuario_prueba.cedula
        self.assertRaises(CalculatorLogic.CedulaVaciaError, ControladorUsuarios_Parametros.BuscarUsuarioPorCedula, cedula_usuario_prueba_seleccionar)

    def testDelete_First(self):
    # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="1028803999", edad="71", sexo="M", estado_civil="S", salario_actual="9000000", semanas_laboradas="1800",
        ahorro_pensional_a_hoy="28000000", rentabilidad_promedio="2", tasa_administracion="1", edad_pension_total="65", hereda_pension="N" )
        ControladorUsuarios_Parametros.InsertarUsuario( usuario_prueba )
	#Cédula del usuario que vamos a eliminar
        cedula_usuario_prueba_eliminar= usuario_prueba.cedula
        ControladorUsuarios_Parametros.EliminarUsuarioPorCedula( cedula_usuario_prueba_eliminar )

    def testDelete_Cedula_Vacia(self):
    # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="", edad="67", sexo="F", estado_civil="S", salario_actual="8000000", semanas_laboradas="1700",
        ahorro_pensional_a_hoy="4100000", rentabilidad_promedio="2", tasa_administracion="1", edad_pension_total="65", hereda_pension="N" )
	#Cédula del usuario que vamos a eliminar
        cedula_usuario_prueba_eliminar= usuario_prueba.cedula
        self.assertRaises(CalculatorLogic.CedulaVaciaError, ControladorUsuarios_Parametros.EliminarUsuarioPorCedula, cedula_usuario_prueba_eliminar)

    def testUpdate_First(self):
    # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="1023934984", edad="66", sexo="M", estado_civil="S", salario_actual="3000000", semanas_laboradas="1200",
        ahorro_pensional_a_hoy="5400000", rentabilidad_promedio="1", tasa_administracion="1", edad_pension_total="65", hereda_pension="N" )
        ControladorUsuarios_Parametros.InsertarUsuario( usuario_prueba )
	#Cedula del usuario que vamos a cambiar
        cedula_usuario_prueba_cambiar = usuario_prueba.cedula
        salario_nuevo_usuario_prueba = "7100000"
        ControladorUsuarios_Parametros.ActualizarUsuarioPorCedula( cedula_usuario_prueba_cambiar, salario_nuevo_usuario_prueba )

    def testUpdate_CedulaVacia(self):
    # Insertar un Usuario en la tabla
        usuario_prueba  = UsuarioParametrosPension( cedula="", edad="83", sexo="F", estado_civil="S", salario_actual="6000000", semanas_laboradas="1140",
        ahorro_pensional_a_hoy="16400000", rentabilidad_promedio="1", tasa_administracion="2", edad_pension_total="65", hereda_pension="N" )
	#Cedula del usuario que vamos a cambiar
        cedula_usuario_prueba_cambiar = usuario_prueba.cedula
        salario_nuevo_usuario_prueba = "11100000"
        self.assertRaises(CalculatorLogic.CedulaVaciaError, ControladorUsuarios_Parametros.ActualizarUsuarioPorCedula, cedula_usuario_prueba_cambiar, salario_nuevo_usuario_prueba)

if __name__ == '__main__':
    # print( Payment.calcPayment.__doc__)
    unittest.main()
