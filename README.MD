# Proyecto calculadora pensional

Consiste en un programa en Python que consulta el ahorro pensional de un fondo privado, permitiendo a los usuarios acceder fácilmente a información actualizada sobre su fondo de pensiones privado. Al ingresar datos como edad, salario actual, ahorro pensional, semanas laboradas, rentabilidad promedio, tasa de interés, etc; le calcula a la persona cuál va a ser el ahorro pensional esperado y el valor de la pensión total. Este tipo de programa simplifica el proceso de seguimiento y gestión de los fondos de pensiones, ofreciendo transparencia y control a los usuarios sobre su futuro financiero. 

## ¿Quién hizo esto?
- Ana Sofía Londoño
- Melissa Foronda
- Tomas Ramírez 

## Estructura del proyecto 
Se tiene la carpeta principal "Proyecto_de_aula_calculadora_pensional", dentro hay otras dos carpetas, una es "test", la cual contiene las pruebas unitarias que ayudan a corroborar si la lógica está correcta y "src", la cual tiene otras seis carpetas, "Console", la cual contiene la consola en donde se va a mostrar la interfaz con la cual va a poder utilizar el usuario, "GUI" es donde se encuentra todo lo relacionado con la interfaz gráfica,  "Logic" la cual contiene la lógica y la fórmula para calcular el ahorro pensional esperado y el valor de la pensión total, "MODEL" se encuentra toda la parte lógica para manejar la información de la base de datos, "CONTROLLER" es donde se controlan todos los datos de la base de datos, "view" es la interacción con el usuario. 

## Prerrequisitos

Instale el paquete psycopg2 con:

    pip install psycopg2
    
## ¿Cómo lo hago funcionar?
- Debe tener los datos de su edad, sexo, estado civil, salario actual, semanas laboradas, ahorro pensional a hoy, rentabilidad promedio del fondo privado, tasa de administración del fondo privado, edad a la que se desea pensionar (legal u otra) y si desea heredar su pensión. A la hora de usar el código, el programa le va a pedir introducir cada dato y el usuario debe ingresar los datos correspondientes.
- Para abrirlo desde la terminal, debes presionar la tecla windows y buscar en la barra, console prompt(cmd), escribe "cd Calculadora_Pensional", y presiona enter:
- Para instalar el paquete necesario para que ejecute, debe escribir el siguiente comando: "pip install psycopg2" y presiona enter.
- Para abrirlo desde la consola, debes buscar el archivo de la siguiente forma: "python src/Console/CalculatorConsole.py" y presionar la tecla enter, luego ingresarás todos los datos solicitados y así apreciarás tu ahorro pensional.
- Para ejecutar las pruebas unitarias debes escribir "python tests\CalculatorTests.py" y presionar la tecla enter.
- Para abrir la interfaz gráfica, debes escribir "python -m pip install kivy[base]", después escribe "python src/GUI/CalculatorGUI.py" y presiona la tecla enter.

Para hacer uso del aplicativo primero debe meterse a "neon tech" e inicar sección o crear una cuenta, luego en la parte izquierda te encuentras con una barra y le das en  "Dashboard" y en la parte de abajo vas a dar click en "connection string" esto te va mostrar un pequeña barra con varias opciones y vas a precionar en "parameters only" una vez te encuentres en esta opción vas a copiar todos los datos que aparecen allí (da click en 'show password' para que se pueda visualizar el PGPASSWORD) y lo vas a pegar en el archivo de "SecretConfig-sample.py" y agregas el PGPORT (puedes usar cualquier puerto 'recomendado usar 5432' ) en este archivo. 

Luego te diriges al neon tech en la parte izquierda te encuentras con una barra y le das en "SQL Editor", te diriges al archivo ControladorUsuario_ParametrosPension y copias la funcion "crear_tabla" en el neon tech y le das en RUN 

- Para ingresar al view por medio de la terminal, debes presionar la tecla windows y buscar en la barra, console prompt(cmd), escribe "cd Calculadora_Pensional", y presiona enter: 
- Para instalar el paquete necesario para que ejecute, debe escribir el siguiente comando: "pip install psycopg2" y presiona enter.
- si deseas actualizar usuarios desde la consola debes escribir "python src\view\actualizar_usuarios.py" y presiona la tecla enter.
- si deseas buscar usuarios desde la consola debes escribir "python src\view\buscar_usuarios.py" y presiona la tecla enter.
- si deseas crear usuarios desde la consola debes escribir "python src\view\crear_usuarios.py" y presiona la tecla enter.
- si deseas eliminar usuario desde la consola debes escribir "python src\view\eliminar_usuarios.py" y presiona la tecla enter.
- si deseas que tu ahorro pensional sea calculado desde la consola debes escribir "python src\view\Ahorro_pensional.py" y presiona la tecla enter. 

Para verificar cualquiera de las anteriores implementaciones que realice debe dirigirse a su "neon tech" y dar clic en "Tables" y actualizas la pagina para mayor seguridad, luego presionas en "Databases" en el nombre del proyecto "calculadora_pensional" y en la parte inferior vas a encontrar el nombre de la tabla donde tambien podras ver la tabla creada con las modificaciones realizadas. 

- Para probar las pruebas unitarias desde la consola debes escribir  "python tests\TestMVC.py" y presiona la tecla enter.

- Entradas: 

Edad actual
Sexo
Estado Civil
Salario actual
Semanas laboradas a hoy
Ahorro pensional a hoy
Rentabilidad promedio de fondo
Tasa de administración del fondo

- Salidas:

Valor ahorro pensional esperado
Pensión total



