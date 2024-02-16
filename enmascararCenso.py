import pandas as pd
import validaciones


# leer el fichero
censo = pd.read_csv("censo.csv")
print("CENSO ORIGINAL")
print(censo)

# seleccionar los nombres (columna 'nombre')
#nombres = censo["nombre"] # devuelve objeto de clase pandas.core.serie.Series
#print(nombres.head()) # muestra la lista de nombres

# el atributo shape contiene el numero de rows,cols
#print(censo["nombre"].shape)

# obtener nombres y apellidos
#nombre_ap1_ap2 = censo[["nombre","apellido1","apellido2"]]
#print(nombre_ap1_ap2.head()) # muestra esos valores

# filtrar
#dni_acaba_en_q = censo[censo["id"].str.endswith("Q")]
#print(dni_acaba_en_q.head()) # muestra dni que acaban en Q

# encontrar duplicados (que tengan mismo nombre, apellido1, apellido2
nombres_iguales = censo.duplicated(subset=["nombre","apellido1","apellido2"], keep=False)
#print(nombres_iguales.head())

# hago una copia del censo y la llamo censo_mod
censo_mod=censo.copy()

# anadir nueva columna llamada "nombre_repetido" que estará a True si nombre,apellido1,apellido2 son_iguales
censo_mod["nombre_repetido"] = nombres_iguales
print("\n\nCENSO ENCONTRANDO NOMBRES Y APELLIDOS REPETIDOS")
print(censo_mod)

# si el valor de la columna "nombre_repetido" es False enmascare el id
# modifica el campo "id" para que contenga el valor ""
censo_mod.loc[censo_mod["nombre_repetido"] == False, "id"] = ""

# enmascarar un id
def enmascararID(x):
    v = validaciones.Validaciones()
    if v.isDNI(x):
        return v.enmascararDNI(x)
    else:
        return "*********"  

# si el valor de la columna "nombre_repetido" es True,
# actualiza el campo "id" con el resultado de aplicar a cada fila la funcion enmascararID
censo_mod.loc[censo_mod["nombre_repetido"] == True, "id"] = censo_mod["id"].apply(enmascararID)
mostrar = censo_mod[["id","nombre","apellido1","apellido2"]]
print("\n\nVALORES A MOSTRAR PUBLICAMENTE")
print(mostrar)

