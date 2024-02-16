
# Test paquete Pandas para Censo unizar

Un test del paquete Pandas para censo-unizar


# Descripción detallada
Prueba que:
- Lee el fichero [censo.csv](censo.csv) que tiene los campos id, nombre, apellido1, apellido2, direccion
- Crea un DataFrame
- Crea una copia del DataFrame
- Añade una columna al nuevo DataFrame que indica, con un booleano, si existen personas repetidas (coinciden varias filas con nombre y apellidos iguales)
- Modifica el DataFrame: Para las personas no repetidas reemplaza el campo ID por cadena vacía, solo sus nombres y apellidos
- Modifica el DataFrame: Para las personas repetidas, modifica el campo ID enmascarándolo para solo mostrar algunas posiciones del ID
- Muestra solo algunos campos del DataFrame


# Instalacion

- Crear un venv y usarlo `python3 -m venv venv; source venv/bin/activate`
- Instalar prerequisitos `pip install -r requirements.txt`
- Ejecutar la prueba `python3 prueba.py`
