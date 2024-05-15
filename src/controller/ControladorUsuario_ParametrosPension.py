import sys
sys.path.append( "src" )

import psycopg2

from model.Usuario_Parametros import UsuarioParametrosPension
from model import SecretConfig
import Logic.CalculatorLogic as CalculatorLogic
from Logic.CalculatorLogic import *

class ControladorUsuarios_Parametros:
    
    def CrearTabla():
        """Crear la tabla de Usuarios_Pension en la BD"""
        ejecucion = """create table Usuarios_Pension (
            Cedula varchar (20) PRIMARY KEY NOT NULL,
            Edad int not null,
            Sexo text not null,
            Estado_civil text not null, 
            Salario_actual int not null,
            Semanas_laboradas int not null, 
            Ahorro_pensional_a_hoy int not null, 
            Rentabilidad_promedio float not null,
            Tasa_administracion float not null,
            Edad_pension_total int not null,
            Hereda_pension text not null

        );"""
        cursor = ControladorUsuarios_Parametros.ObtenerCursor()
        cursor.execute(ejecucion)
        cursor.connection.commit()

    def EliminarTabla(): 
        """Borra la tabla de usuarios de la BD"""
        ejecucion = """drop table Usuarios_Pension"""
        cursor = ControladorUsuarios_Parametros.ObtenerCursor()
        cursor.execute(ejecucion)
        #confirma los cambios realizados en la base de datos 
        #Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def InsertarUsuario(usuario_pension: UsuarioParametrosPension):
        VerificarCedula(usuario_pension.cedula)
        """Recibe una instancia de la clase UsuarioParametrosPension y la inserta en la tabla respectiva"""
        ejecucion = f"""insert into Usuarios_Pension ( Cedula, Edad, Sexo, Estado_civil,
        Salario_actual, Semanas_laboradas, Ahorro_pensional_a_hoy, 
        Rentabilidad_promedio, Tasa_administracion, Edad_pension_total,
        Hereda_pension)
        values ('{usuario_pension.cedula}', '{usuario_pension.edad}', '{usuario_pension.sexo}', '{usuario_pension.estado_civil}', '{usuario_pension.salario_actual}', '{usuario_pension.semanas_laboradas}', '{usuario_pension.ahorro_pensional_a_hoy}',
        '{usuario_pension.rentabilidad_promedio}', '{usuario_pension.tasa_administracion}', '{usuario_pension.edad_pension_total}', '{usuario_pension.hereda_pension}')"""
        cursor = ControladorUsuarios_Parametros.ObtenerCursor()
        cursor.execute(ejecucion)        
        cursor.connection.commit()

    def BuscarUsuarioPorCedula(cedula):
        VerificarCedula(cedula)
        """Trae un usuario de la tabla de Usuarios_Pension por la cedula"""
        ejecucion = f"""select Cedula, Edad, Sexo, Estado_civil, Salario_actual, Semanas_laboradas, Ahorro_pensional_a_hoy,
        Rentabilidad_promedio, Tasa_administracion, Edad_pension_total, Hereda_pension from Usuarios_Pension where Cedula = '{cedula}'"""
        cursor = ControladorUsuarios_Parametros.ObtenerCursor()
        cursor.execute(ejecucion)
        fila = cursor.fetchone()
        usuario_encontrado = UsuarioParametrosPension(cedula=fila[0], edad=fila[1], sexo= fila[2], estado_civil=fila[3], salario_actual=fila[4], semanas_laboradas=fila[5], ahorro_pensional_a_hoy=fila[6], rentabilidad_promedio=fila[7], tasa_administracion=fila[8], edad_pension_total= fila[9], hereda_pension=fila[10])
        return usuario_encontrado
    
    def EliminarUsuarioPorCedula( cedula ):
        VerificarCedula(cedula)
        # Elimina un usuario de la tabla de Usuarios_Pension por la cédula
        ejecucion = f"delete from Usuarios_Pension where Cedula = '{cedula}'"
        cursor = ControladorUsuarios_Parametros.ObtenerCursor()
        cursor.execute(ejecucion)

        cursor.connection.commit()

    def ActualizarUsuarioPorCedula(cedula, salario_nuevo):
        VerificarCedula(cedula)
        #Actualiza un usuario de la tabla de Usuarios_Pension por la cédula
        ejecucion = f"update Usuarios_Pension SET Salario_actual = '{salario_nuevo}' where Cedula = '{cedula}'"
        cursor = ControladorUsuarios_Parametros.ObtenerCursor()

        cursor.execute(ejecucion)

        cursor.connection.commit()

    def ObtenerCursor():
        """Crear la conexión a la base de datos y retorna un cursor para hacer consultas"""
        connection=psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password= SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port= SecretConfig.PGPORT)
        #Todas las instrucciones se ejecutan a través de un cursor
        cursor=connection.cursor()
        return cursor 