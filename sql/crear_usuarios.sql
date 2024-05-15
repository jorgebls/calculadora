-- Crea la tabla de Usuarios_Pension
create table Usuarios_Pension (
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
        );