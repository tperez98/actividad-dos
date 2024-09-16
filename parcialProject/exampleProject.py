#Conversión de tipos de datos (Enteros, Decimales y Cadenas)
# Definimos un entero, un decimal y una cadena
entero = 82
decimal = 4.5
cadena = "600"

# Convertir una cadena a un entero
cadena_a_entero = int(cadena)  # Resulta en 600

# Convertir una cadena a un decimal
cadena_a_decimal = float(cadena)  # Resulta en 600.0

print(f"Entero: {entero}, Decimal: {decimal}, Cadena convertida a entero: {cadena_a_entero}, Cadena convertida a decimal: {cadena_a_decimal}")

#Multilíneas de Cadenas
multilinea = """Esto 
es un
ejemplo de 
multilinea"""

print("\nMultilínea:")
print(multilinea)

# Función len()
cadena = "Hola, profe!"
longitud_cadena = len(cadena)
print(f"\nLongitud de la cadena '{cadena}': {longitud_cadena}")

# Subcadenas
n = 6
primeros_n = cadena[:n]  # Obtiene los primeros 5 caracteres
print(f"\nPrimeros {n} caracteres: {primeros_n}")

#Obtener los caracteres del medio:
inicio = 4
fin = 11
medio = cadena[inicio:fin]  # Obtiene los caracteres del índice 6 al 10
print(f"Caracteres del medio: {medio}")

#Obtener los últimos n caracteres:
n = 5
ultimos_n = cadena[-n:]  # Obtiene los últimos 6 caracteres
print(f"Últimos {n} caracteres: {ultimos_n}")

#Función upper() y lower()
cadena = "Toby es grande"
cadena_mayusculas = cadena.upper()  # Convierte a mayúsculas
cadena_minusculas = cadena.lower()  # Convierte a minúsculas
print(f"\nCadena en mayúsculas: {cadena_mayusculas}")
print(f"Cadena en minúsculas: {cadena_minusculas}")

#Función strip()
cadena_con_espacios = "   el sol es bonito   "
cadena_sin_espacios = cadena_con_espacios.strip()
print(f"\nCadena con espacios eliminados: '{cadena_sin_espacios}'")

#Función replace()
cadena = "Jasper es gordito"
cadena_reemplazada = cadena.replace("increíble", "genial")
print(f"\nCadena reemplazada: {cadena_reemplazada}")

# Función split()
cadena = "Toby es bonito"
cadena_split = cadena.split(" ")
print(f"\nCadena dividida por espacios: {cadena_split}")

#Formato de Cadenas (F-String)
nombre = "Tatiana"
edad = 25
cadena_formateada = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(f"\nCadena formateada: {cadena_formateada}")

