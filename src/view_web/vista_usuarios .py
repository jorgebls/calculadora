from flask import Blueprint, request, render_template, redirect, url_for
import sys
sys.path.append("src")

from model.Usuario_Parametros import UsuarioParametrosPension
from controller.ControladorUsuario_ParametrosPension import ControladorUsuarios_Parametros
ControladorUsuarios_Parametros.EliminarTabla()
ControladorUsuarios_Parametros.CrearTabla()

blueprint = Blueprint("vista_usuario", __name__, "templates")

import sys
sys.path.append("src")

@blueprint.route("/")
def Home():
   return render_template("index.html")

@blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        # Asumiendo que tienes un formulario HTML que envía estos datos
        cedula = request.form['cedula']
        edad = request.form['edad']
        sexo = request.form['sexo']
        estado_civil = request.form['estado_civil']
        salario_actual = request.form['salario_actual']
        semanas_laboradas = request.form['semanas_laboradas']
        ahorro_pensional_a_hoy = request.form['ahorro_pensional_a_hoy']
        rentabilidad_promedio = request.form['rentabilidad_promedio']
        tasa_administracion = request.form['tasa_administracion']
        edad_pension_total = request.form['edad_pension_total']
        hereda_pension = request.form['hereda_pension']
        
        usuario = UsuarioParametrosPension(cedula, edad, sexo, estado_civil, salario_actual, semanas_laboradas, ahorro_pensional_a_hoy, rentabilidad_promedio, tasa_administracion, edad_pension_total, hereda_pension)
        ControladorUsuarios_Parametros.InsertarUsuario(usuario)
        return redirect(url_for('usuario.ver_usuario', cedula=cedula))
    return render_template('agregar_usuario.html')

@blueprint.route('/buscar/<cedula>')
def ver_usuario(cedula):
    usuario = ControladorUsuarios_Parametros.BuscarUsuarioPorCedula(cedula)
    return render_template('ver_usuario.html', usuario=usuario)

@blueprint.route('/actualizar/<cedula>', methods=['GET', 'POST'])
def actualizar_usuario(cedula):
    if request.method == 'POST':
        salario_nuevo = request.form['salario_actual']
        ControladorUsuarios_Parametros.ActualizarUsuarioPorCedula(cedula, salario_nuevo)
        return redirect(url_for('usuario.ver_usuario', cedula=cedula))
    usuario = ControladorUsuarios_Parametros.BuscarUsuarioPorCedula(cedula)
    return render_template('actualizar_usuario.html', usuario=usuario)

@blueprint.route('/eliminar/<cedula>', methods=['GET', 'POST'])
def eliminar_usuario(cedula):
    if request.method == 'POST':
        ControladorUsuarios_Parametros.EliminarUsuarioPorCedula(cedula)
        return redirect(url_for('index'))
    return render_template('eliminar_usuario.html', cedula=cedula)
