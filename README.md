# Test paquete Pandas para Censo unizar

Un test del paquete [Pandas](https://pandas.pydata.org) para censo-unizar


# Descripción detallada
Prueba que:
- Lee el fichero [censo.csv](censo.csv) que tiene los campos id, nombre, apellido1, apellido2, direccion
- Crea un DataFrame
- Crea una copia del DataFrame
- Añade una columna al nuevo DataFrame que indica, con un booleano, si existen personas repetidas (coinciden varias filas con nombre y apellidos iguales)
- Modifica el DataFrame: Para las personas no repetidas reemplaza el campo ID por cadena vacía, solo sus nombres y apellidos
- Modifica el DataFrame: Para las personas repetidas, modifica el campo ID enmascarándolo para solo mostrar algunas posiciones del ID
- Muestra solo algunos campos del DataFrame

# Regulación
* Las instrucciones para publicar actos con una pluralidad de interesados están en [https://ae.unizar.es/?app=touz&opcion=down&id=63035](La instruccion SG2/2019) y dicen:
    * _Cuando existan dos o más personas con mismos nombres y apellidos, se añadirán al nombre y apellidos 4 cifras numéricas aleatorias del documento de identidad_
        * _Los caracteres alfabéticos se sustituirán por un asterisco en cada posición_
        * _Si se trata de un DNI (formato 12345678X) se publicarán los digitos que ocupen posiciones cuarta, quinta, sexta y séptima, p ej ***4567**_
        * _Si se trata de un NIE (formato L1234567X) se publicarán los dígitos que ocupen posiciones cuarta, quinta, sexta y séptima evitando los tres caracteres alfabéticos, p ej ****3456*_
        * _Si se trata de un pasaporte (formato ABC123456) se publicarán los dígitos que ocupen posiciones tercera, cuarta, quinta y sexta, evitando los tres caracteres alfabéticos, p ej *****3456_

    * _En el supuesto en que además del nombre y apellidos coincidieran las cifras resultantes de aplicación de las pautas anteriormente señaladas, se optará por publicar los dígitos que ocupen las posiciones alternas: ****5678*, ***3456**, ****2345*_

# Instalacion

- Crear un venv y usarlo `python3 -m venv venv; source venv/bin/activate`
- Instalar prerequisitos `pip install -r requirements.txt`
- Ejecutar la prueba `python3 enmascararCenso.py`

