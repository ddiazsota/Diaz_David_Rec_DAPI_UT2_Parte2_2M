def create_email(nombre,apellido):
    """
    Esta función consiste en concatenar dos str y formar un correo 
    electrónico.
    Parámetros:
    -Dos str con el nombre y el apellido de cada alumno/a
    Salida:
    -Str con el emal resultante
    """
    correo=""
    correo+=nombre[0]
    Long_apellido = len(apellido)
    if Long_apellido>=5:
        for i in range(0,5):
            correo+=apellido[i]
    else:
        for i in range(Long_apellido):
            correo+=apellido[i]

    dominio = "@educacion.navarra.es"
    correo+=dominio
    print(correo)
create_email("cruz","alfonso")