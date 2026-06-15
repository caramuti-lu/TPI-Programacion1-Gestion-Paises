# TPI-Programacion1-Gestion-Paises
Trabajo Práctico Integrador de Programación I - Sistema de Gestión de Países en Python- Aumedes - Caramuti
# 🌎 Sistema de Gestión de Países

## 📖 Descripción

Este proyecto fue desarrollado como Trabajo Práctico Integrador para la materia **Programación I**.

La aplicación permite gestionar información de distintos países almacenada en un archivo CSV, ofreciendo funcionalidades de consulta, búsqueda, filtrado, ordenamiento y generación de estadísticas.

El objetivo principal del proyecto fue aplicar los conocimientos adquiridos durante la cursada, utilizando estructuras de datos, funciones, archivos CSV y técnicas de programación modular en Python.

---

## 🎯 Objetivos

- Aplicar conceptos fundamentales de Programación I.
- Trabajar con estructuras de datos como listas y diccionarios.
- Implementar funciones para organizar y reutilizar código.
- Leer y procesar información almacenada en archivos CSV.
- Realizar búsquedas, filtros y ordenamientos de datos.
- Generar estadísticas básicas a partir de la información almacenada.
- Utilizar GitHub para la gestión y documentación del proyecto.

---

## ⚙️ Funcionalidades

El sistema permite:

✅ Cargar datos desde un archivo CSV.

✅ Visualizar la información almacenada.

✅ Buscar países por nombre.

✅ Filtrar países según distintos criterios.

✅ Ordenar los datos por nombre, población o superficie.

✅ Obtener estadísticas básicas.

✅ Validar los datos ingresados por el usuario.

✅ Navegar mediante un menú interactivo.

---

## 🛠️ Tecnologías Utilizadas

- Python 3
- Módulo CSV
- GitHub
- Listas
- Diccionarios
- Funciones
- Condicionales
- Bucles (`for` y `while`)

---

## 📂 Estructura del Proyecto

```text
Proyecto/
│
├── main.py
├── paises.csv
├── README.md
└── Informe_TPI.pdf
```

---

## 📊 Datos Utilizados

Los datos se almacenan en un archivo CSV que contiene información de distintos países, incluyendo:

- Nombre
- Población
- Superficie
- Continente

Estos datos son cargados en memoria mediante una lista de diccionarios para facilitar su manipulación.

---

## 🧩 Conceptos Aplicados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

- Manejo de listas.
- Uso de diccionarios.
- Programación modular mediante funciones.
- Estructuras condicionales.
- Estructuras repetitivas.
- Lectura y escritura de archivos CSV.
- Ordenamiento de datos.
- Estadísticas básicas.

---

# 🔹 Ejecución del programa

Abrí una terminal o consola en la carpeta donde está guardado el archivo .py ejecutando el código “python nombre_del_archivo.py”, o en su defecto abrir el archivo en algún procesador de código como es el caso de VsCode y ejecutar el programa.

El programa mostrará un menú principal con opciones numeradas.

# 🔹 Opciones del menú principal

**Agregar país**  
Permite ingresar un nuevo país validando que no exista duplicado ni que se ingresen datos incorrectos. Se solicitara que el usuario ingrese nombre, población, superficie y continente.

**Actualizar país**  
Busca un país por nombre exacto y permite modificar su población y/o superficie, en el caso que no se desee modificar alguno de los datos, basta con ingresar enter.

**Buscar país**  
Encuentra países según el nombre que ingrese el usuario, el cual puede coincidir parcial o totalmente con los nombres listados, se informara a su vez si el país ingresado no existe.

**Filtrar países**  
Submundo con tres filtros, que efectuara las opciones según ingrese el usuario, si ingresa un valor que no esta contemplado en las opciones, seguirá consultando que ponga un valor valido hasta que sea ingresado:

- **Por continente.** Esta opción filtrara los países registrados según el dato de continente que ingrese el usuario, en caso de no coincidencia se informara por pantalla.
- **Por rango de población.** Esta opción filtrara los países registrados según su población, pidiendo un numero mínimo y un numero máximo. En el caso que se ingresen datos que no sean números, o que el numero máximo sea menor que el mínimo, se informara por pantalla del error.
- **Por rango de superficie.** Esta opción filtraran los países registrados según su superficie, pidiendo un numero mínimo y un numero máximo. En el caso que se ingresen datos que no sean números, o que el numero máximo sea menor que el mínimo, se informara por pantalla del error.

**Ordenar países**  
Ordena la lista por nombre, población o superficie, en forma ascendente o descendente, según las opciones brindadas que elija el usuario. En caso de que elija una opción fuera del rango brindado, seguirá consultando hasta que ingrese un valor aceptable.

**Mostrar estadísticas**  
Una vez elegida esta opción, se calcula y muestra las siguientes informaciones de los países:

- País con mayor y menor población  
- Promedio de población  
- País con mayor y menor superficie  
- Promedio de superficie  
- Cantidad de países por continente  

**Listar todos los países**  
Una vez seleccionada esta opción, se muestra la lista completa de países cargados en el dataset.

**Salir (0)**  
Finaliza la ejecución del programa.

# 🔹 Notas importantes

- Si el archivo paises.csv no existe, el programa arranca con una lista vacía y lo crea al guardar cambios.
- Los datos ingresados deben ser válidos:
  - Nombre/continente: solo letras, sin números ni símbolos.
  - Población/superficie: números enteros positivos.
- Para la búsqueda de países que contengan acentos en su nombre, sera necesario que según la opción que se elija, que se agregue el acento. En el caso que quiera actualizar el país, al requerirse el nombre completo, se pondrá la letra correspondiente con tilde. En el caso de la búsqueda de país, se podrá poner parcialmente el nombre, o agregar el nombre completo con la tilde correspondiente.
- Los cambios se guardan automáticamente en el archivo CSV.


---

## 👥 Integrantes

- Lucía Caramuti
- Nehuen Aumedes Diez

---

## 🎓 Materia

Programación I

Tecnicatura Universitaria en Programación

Universidad Tecnológica Nacional (UTN)


---

## 📌 Repositorio

Trabajo Práctico Integrador - Programación I

Año 2026
