

# Importa el modulo csv para leer y escribir archivos CSV
import csv   
import os    # Para verificar si el archivo CSV existe al iniciar

# CONSTANTE: nombre del archivo CSV: obtiene la carpeta donde está guardado este programa

ARCHIVO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "paises.csv.txt")



# Muestra en pantalla la ruta completa del archivo

print("ARCHIVO_CSV =", ARCHIVO_CSV) 



# FUNCIONES DE PERSISTENCIA (lectura y escritura del CSV)

#funcion def cargar 
def cargar_csv():
    #Lee el archivo CSV y devuelve una lista de diccionarios.

    #creamos una lista vacia donde se guardaran los paises
    paises = []

    # Verificamos que el archivo exista antes de intentar abrirlo
    if not os.path.exists(ARCHIVO_CSV):

#muestra un mensaje avisando que el archivo no se encontro
        print(f"[AVISO] No se encontró '{ARCHIVO_CSV}'. Se iniciará con lista vacía.")
#deuelve una lista acia y  termina la funcion 
        return paises
#intenta leer y abrir el archivo 
    try:
 # Abre el archivo CSV en modo lectura,  utf-8-sig evita problemas con caracteres especiales
        with open(ARCHIVO_CSV, newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
#recorre cada fila del archivo
            for numero_fila, fila in enumerate(lector, start=2):
                # Validamos que todos los campos requeridos estén presentes y no esten vacios
                campos_requeridos = ["nombre", "poblacion", "superficie", "continente"]
                if not all(fila.get(campo, "").strip() for campo in campos_requeridos):
                    print(f"[AVISO] Fila {numero_fila} incompleta, se omite: {dict(fila)}")
                    continue

                try:

#creamos un diccionario con los datos del pais
                    pais = {
                        "nombre":      fila["nombre"].strip(),
                        "poblacion":   int(fila["poblacion"].strip()),
                        "superficie":  int(fila["superficie"].strip()),
                        "continente":  fila["continente"].strip()
                    }
                    #agregamos el pais a la lista
                    paises.append(pais)
                except ValueError:
                    # se ejecuta si poblacion o superficie no son numeros enteros validos
                    print(f"[ERROR] Fila {numero_fila}: poblacion/superficie deben ser "
                          f"números enteros. Se omite la fila.")

    except OSError as e:
        #se ejecuta si ocurre un error al abrir el archivo
        print(f"[ERROR] No se pudo leer el archivo: {e}")

    return paises


def guardar_csv(paises):
    
    try:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8-sig") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()        # Escribe la primera línea con los nombres de columna
            escritor.writerows(paises)    # Escribe todas las filas
    except OSError as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")



# FUNCIONES DE VALIDACIÓN DE ENTRADA


def pedir_entero(mensaje, minimo=None, maximo=None):

    #Solicitamos al usuario un número entero y valida el rango si se indica.


    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("  [!] El campo no puede estar vacío.")
            continue
        try:
            numero = int(entrada)
        except ValueError:
            print("  [!] Ingresá un número entero válido (sin decimales ni letras).")
            continue

        if minimo is not None and numero < minimo:
            print(f"  [!] El valor debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f"  [!] El valor debe ser menor o igual a {maximo}.")
            continue

        return numero


def pedir_texto(mensaje):

    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        print("  [!] El campo no puede estar vacío.")


def pedir_opcion(mensaje, opciones_validas):
   
    #Solicita al usuario que elija una opción de una lista válida.

    
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada in opciones_validas:
            return entrada
        print(f" Opción inválida. Opciones disponibles: {', '.join(opciones_validas)}")



# FUNCIONES DE PRESENTACIÓN


def imprimir_separador(caracter="─", longitud=65):
    """Imprime una línea separadora para mejorar la legibilidad."""
    print(caracter * longitud)


def imprimir_pais(pais, numero=None):
    """
    Muestra los datos de un país en formato legible.

    Parámetros:
        pais   (dict): diccionario con los datos del país.
        numero (int):  número de orden opcional (para listar).
    """
    prefijo = f"  {numero}. " if numero is not None else "  "
    print(f"{prefijo}{pais['nombre']}")
    print(f"      Continente : {pais['continente']}")
    print(f"      Población  : {pais['poblacion']:,}".replace(",", "."))
    print(f"      Superficie : {pais['superficie']:,} km²".replace(",", "."))


def imprimir_lista_paises(paises, titulo="Resultado"):
   
    #Muestra una lista de países con título y separadores.

 
    imprimir_separador()
    print(f"  {titulo} ({len(paises)} país/es encontrado/s)")
    imprimir_separador()
    if not paises:
        print("  No se encontraron países.")
    else:
        for i, pais in enumerate(paises, start=1):
            imprimir_pais(pais, numero=i)
            if i < len(paises):
                print()   # Espacio entre paises para mejorar lectura



# FUNCIONES DE OPERACIONES SOBRE EL DATASET


def agregar_pais(paises):
    
    #Solicita los datos de un nuevo país, valida que no exist
    
    print("\n  ── Agregar nuevo país ──")

    nombre = pedir_texto("  Nombre del país: ")

    # Verificamos duplicado (ignorando mayúsculas/minúsculas)
    if any(p["nombre"].lower() == nombre.lower() for p in paises):
        print(f" Ya existe un país llamado '{nombre}'.")
        return

    poblacion  = pedir_entero("  Población (número entero positivo): ", minimo=1)
    superficie = pedir_entero("  Superficie en km² (número entero positivo): ", minimo=1)
    continente = pedir_texto("  Continente: ")

    nuevo_pais = {
        "nombre":     nombre,
        "poblacion":  poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_csv(paises)   
    print(f"\n   '{nombre}' agregado correctamente.")


def actualizar_pais(paises):

# Busca un pais por nombre exacto y permite actualizar su poblacion y/o superficie

    
    print("\n  ── Actualizar pais ──")
    nombre_buscar = pedir_texto("  Nombre exacto del pais a actualizar: ")

    # Buscamos el indice del pais en la lista
    indice = None
    for i, p in enumerate(paises):
        if p["nombre"].lower() == nombre_buscar.lower():
            indice = i
            break

    if indice is None:
        print(f" error! No se encontró ningún país con el nombre '{nombre_buscar}'.")
        return

    pais = paises[indice]
    print(f"\n  Datos actuales de {pais['nombre']}:")
    imprimir_pais(pais)

    print("\n  Ingresá los nuevos valores (Enter para conservar el valor actual):")

    entrada_pob = input(f"  Nueva población [{pais['poblacion']:,}]: ".replace(",", ".")).strip()
    if entrada_pob:
        try:
            nueva_pob = int(entrada_pob)
            if nueva_pob < 1:
                print("error! La población debe ser un entero positivo. No se actualizó.")
            else:
                paises[indice]["poblacion"] = nueva_pob
        except ValueError:
            print("error!  Valor inválido para población. No se actualizó.")

    entrada_sup = input(f"  Nueva superficie [{pais['superficie']:,} km²]: ".replace(",", ".")).strip()
    if entrada_sup:
        try:
            nueva_sup = int(entrada_sup)
            if nueva_sup < 1:
                print(" error! La superficie debe ser un entero positivo. No se actualizó.")
            else:
                paises[indice]["superficie"] = nueva_sup
        except ValueError:
            print(" error! Valor inválido para superficie. No se actualizó.")

    guardar_csv(paises)
    print(f"\n  Datos de '{paises[indice]['nombre']}' actualizados y guardados.")


def buscar_por_nombre(paises):
   
    #Busca países cuyo nombre contenga el texto ingresado(coincidencia parcial, sin importar mayúsculas).

    print("\n  ── Buscar país por nombre ──")
    termino = pedir_texto("  Ingresá el nombre o parte del nombre: ").lower()

    
    resultados = [p for p in paises if termino in p["nombre"].lower()]

    imprimir_lista_paises(resultados, titulo=f"Búsqueda: '{termino}'")


def filtrar_paises(paises):
   
    #Muestra un submenú para filtrar países 
    print("\n  ── Filtrar países ──")
    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")

    opcion = pedir_opcion("  Elegí una opción: ", ["1", "2", "3"])

    if opcion == "1":
        # filtro por continente 
        continente = pedir_texto("  Nombre del continente: ")
        resultados = [
            p for p in paises
            if p["continente"].lower() == continente.lower()
        ]
        imprimir_lista_paises(resultados, titulo=f"Países en {continente.capitalize()}")

    elif opcion == "2":
        # filtro por rango de población
        print("  Ingresá el rango de población:")
        minimo = pedir_entero("    Mínimo: ", minimo=0)
        maximo = pedir_entero("    Máximo: ", minimo=minimo)
        resultados = [
            p for p in paises
            if minimo <= p["poblacion"] <= maximo
        ]
        imprimir_lista_paises(
            resultados,
            titulo=f"Población entre {minimo:,} y {maximo:,}".replace(",", ".")
        )

    elif opcion == "3":
        # filtro por rango de superficie
        print("  Ingresá el rango de superficie en km²:")
        minimo = pedir_entero("    Mínimo (km²): ", minimo=0)
        maximo = pedir_entero("    Máximo (km²): ", minimo=minimo)
        resultados = [
            p for p in paises
            if minimo <= p["superficie"] <= maximo
        ]
        imprimir_lista_paises(
            resultados,
            titulo=f"Superficie entre {minimo:,} y {maximo:,} km²".replace(",", ".")
        )


def ordenar_paises(paises):
    #Muestra los países ordenados por el criterio elegido.


    print("\n  ── Ordenar países ──")
    print("  Ordenar por:")
    print("  1. Nombre")
    print("  2. Población")
    print("  3. Superficie")

    opcion = pedir_opcion("  Elegí una opción: ", ["1", "2", "3"])

    print("  Dirección:")
    print("  a. Ascendente (de menor a mayor / A-Z)")
    print("  d. Descendente (de mayor a menor / Z-A)")
    direccion = pedir_opcion("  Elegí una opción: ", ["a", "d"])
    descendente = (direccion == "d")

    # Diccionario 
    criterios = {
        "1": ("nombre",     "nombre"),
        "2": ("poblacion",  "población"),
        "3": ("superficie", "superficie")
    }
    clave, descripcion = criterios[opcion]

    # sorted
    ordenados = sorted(paises, key=lambda p: p[clave], reverse=descendente)

    sentido = "descendente" if descendente else "ascendente"
    imprimir_lista_paises(ordenados, titulo=f"Ordenado por {descripcion} ({sentido})")


def mostrar_estadisticas(paises):

    #Calcula y muestra indicadores estadísticos del dataset
    if not paises:
        print("\n error! No hay datos para calcular estadísticas.")
        return

    print("\n  ── Estadísticas ──")
    imprimir_separador()

    #  Población:  max() y min() con key
    pais_mayor_pob = max(paises, key=lambda p: p["poblacion"])
    pais_menor_pob = min(paises, key=lambda p: p["poblacion"])

    # Promedio: sum() / cantidad
    total_pob  = sum(p["poblacion"] for p in paises)
    promedio_pob = total_pob // len(paises)   # División entera para mantener tipo int

    print("  POBLACIÓN")
    print(f"    Mayor : {pais_mayor_pob['nombre']} "
          f"({pais_mayor_pob['poblacion']:,})".replace(",", "."))
    print(f"    Menor : {pais_menor_pob['nombre']} "
          f"({pais_menor_pob['poblacion']:,})".replace(",", "."))
    print(f"    Promedio: {promedio_pob:,}".replace(",", "."))

    imprimir_separador("·")

    # ── Superficie ──
    pais_mayor_sup = max(paises, key=lambda p: p["superficie"])
    pais_menor_sup = min(paises, key=lambda p: p["superficie"])
    total_sup      = sum(p["superficie"] for p in paises)
    promedio_sup   = total_sup // len(paises)

    print("  SUPERFICIE")
    print(f"    Mayor : {pais_mayor_sup['nombre']} "
          f"({pais_mayor_sup['superficie']:,} km²)".replace(",", "."))
    print(f"    Menor : {pais_menor_sup['nombre']} "
          f"({pais_menor_sup['superficie']:,} km²)".replace(",", "."))
    print(f"    Promedio: {promedio_sup:,} km²".replace(",", "."))

    imprimir_separador("·")

    # Países por continente: Usamos un diccionario para contar: clave = continente, valor = cantidad
    conteo_continentes = {}
    for pais in paises:
        cont = pais["continente"]
        # Si la clave no existe, la creamos con 0 y sumamos 1
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1

    print("  PAÍSES POR CONTINENTE")
    # Ordenamos por cantidad descendente para mostrar primero el más representado
    for continente, cantidad in sorted(
        conteo_continentes.items(), key=lambda x: x[1], reverse=True
    ):
        barra = "█" * cantidad   # Barra visual proporcional
        print(f"    {continente:<15} : {cantidad:>3}  {barra}")

    imprimir_separador()
    print(f"  Total de países en el dataset: {len(paises)}")


# MENÚ PRINCIPAL

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    imprimir_separador("═")
    print("  GESTIÓN DE DATOS DE PAÍSES")
    imprimir_separador("═")
    print("  1. Agregar país")
    print("  2. Actualizar población y superficie de un país")
    print("  3. Buscar país por nombre")
    print("  4. Filtrar países")
    print("  5. Ordenar países")
    print("  6. Mostrar estadísticas")
    print("  7. Listar todos los países")
    print("  0. Salir")
    imprimir_separador()


def main():
    """
    Función principal: carga el CSV, muestra el menú en bucle
    y llama a la función correspondiente según la opción elegida.

    El bucle while True se rompe solo cuando el usuario elige "0".
    """
    print("\n  Cargando datos desde el CSV...")
    paises = cargar_csv()
    print(f"  ✓ {len(paises)} países cargados.")

    while True:
        mostrar_menu()
        opcion = input("  Elegí una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_por_nombre(paises)

        elif opcion == "4":
            filtrar_paises(paises)

        elif opcion == "5":
            ordenar_paises(paises)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            imprimir_lista_paises(paises, titulo="Todos los países")

        elif opcion == "0":
            print("\n  Hasta luego.\n")
            break

        else:
            print("  [!] Opción inválida. Ingresá un número del 0 al 7.")

        input("\n  Presioná Enter para continuar...")


# PUNTO DE ENTRADA

# Esta condición garantiza que main() solo se ejecute cuando
# el archivo se corre directamente, no cuando se importa
# como módulo desde otro archivo.

if __name__ == "__main__":
    main()
